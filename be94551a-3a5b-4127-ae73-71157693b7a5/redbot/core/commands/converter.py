"""
commands.converter
==================
This module contains useful functions and classes for command argument conversion.

Some of the converters within are included provisionally and are marked as such.
"""
import functools
import re
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from typing import (
    TYPE_CHECKING,
    Generic,
    Optional,
    Optional as NoParseOptional,
    Tuple,
    List,
    Dict,
    Type,
    TypeVar,
    Union as UserInputOptional,
)

import discord
from discord.ext import commands as dpy_commands
from discord.ext.commands import BadArgument

from ..i18n import Translator
from ..utils.chat_formatting import humanize_timedelta, humanize_list

if TYPE_CHECKING:
    from .context import Context

__all__ = [
    "RawUserIdConverter",
    "DictConverter",
    "UserInputOptional",
    "NoParseOptional",
    "RelativedeltaConverter",
    "TimedeltaConverter",
    "get_dict_converter",
    "get_timedelta_converter",
    "parse_relativedelta",
    "parse_timedelta",
    "CommandConverter",
    "CogConverter",
]

_ = Translator("commands.converter", __file__)

ID_REGEX = re.compile(r"([0-9]{15,20})")
USER_MENTION_REGEX = re.compile(r"<@!?([0-9]{15,21})>$")


# Taken with permission from
# https://github.com/mikeshardmind/SinbadCogs/blob/816f3bc2ba860243f75112904b82009a8a9e1f99/scheduler/time_utils.py#L9-L19
TIME_RE_STRING = r"\s?".join(
    [
        r"((?P<years>\d+?)\s?(years?|y))?",
        r"((?P<months>\d+?)\s?(months?|mo))?",
        r"((?P<weeks>\d+?)\s?(weeks?|w))?",
        r"((?P<days>\d+?)\s?(days?|d))?",
        r"((?P<hours>\d+?)\s?(hours?|hrs|hr?))?",
        r"((?P<minutes>\d+?)\s?(minutes?|mins?|m(?!o)))?",  # prevent matching "months"
        r"((?P<seconds>\d+?)\s?(seconds?|secs?|s))?",
    ]
)

TIME_RE = re.compile(TIME_RE_STRING, re.I)


def _parse_and_match(string_to_match: str, allowed_units: List[str]) -> Optional[Dict[str, int]]:
    """
    Local utility function to match TIME_RE string above to user input for both parse_timedelta and parse_relativedelta
    """
    matches = TIME_RE.fullmatch(string_to_match)
    if matches:
        params = {k: int(v) for k, v in matches.groupdict().items() if v is not None}
        for k in params.keys():
            if k not in allowed_units:
                raise BadArgument(
                    _("`{unit}` is not a valid unit of time for this command").format(unit=k)
                )
        return params
    return None


def parse_timedelta(
    argument: str,
    *,
    maximum: Optional[timedelta] = None,
    minimum: Optional[timedelta] = None,
    allowed_units: Optional[List[str]] = None,
) -> Optional[timedelta]:
    """
    This converts a user provided string into a timedelta

    The units should be in order from largest to smallest.
    This works with or without whitespace.

    Parameters
    ----------
    argument : str
        The user provided input
    maximum : Optional[datetime.timedelta]
        If provided, any parsed value higher than this will raise an exception
    minimum : Optional[datetime.timedelta]
        If provided, any parsed value lower than this will raise an exception
    allowed_units : Optional[List[str]]
        If provided, you can constrain a user to expressing the amount of time
        in specific units. The units you can chose to provide are the same as the
        parser understands. (``weeks``, ``days``, ``hours``, ``minutes``, ``seconds``)

    Returns
    -------
    Optional[datetime.timedelta]
        If matched, the timedelta which was parsed. This can return `None`

    Raises
    ------
    BadArgument
        If the argument passed uses a unit not allowed, but understood
        or if the value is out of bounds.
    """
    allowed_units = allowed_units or [
        "weeks",
        "days",
        "hours",
        "minutes",
        "seconds",
    ]
    params = _parse_and_match(argument, allowed_units)
    if params:
        try:
            delta = timedelta(**params)
        except OverflowError:
            raise BadArgument(
                _("The time set is way too high, consider setting something reasonable.")
            )
        if maximum and maximum < delta:
            raise BadArgument(
                _(
                    "This amount of time is too large for this command. (Maximum: {maximum})"
                ).format(maximum=humanize_timedelta(timedelta=maximum))
            )
        if minimum and delta < minimum:
            raise BadArgument(
                _(
                    "This amount of time is too small for this command. (Minimum: {minimum})"
                ).format(minimum=humanize_timedelta(timedelta=minimum))
            )
        return delta
    return None


def parse_relativedelta(
    argument: str, *, allowed_units: Optional[List[str]] = None
) -> Optional[relativedelta]:
    """
    This converts a user provided string into a datetime with offset from NOW

    The units should be in order from largest to smallest.
    This works with or without whitespace.

    Parameters
    ----------
    argument : str
        The user provided input
    allowed_units : Optional[List[str]]
        If provided, you can constrain a user to expressing the amount of time
        in specific units. The units you can chose to provide are the same as the
        parser understands. (``years``, ``months``, ``weeks``, ``days``, ``hours``, ``minutes``, ``seconds``)

    Returns
    -------
    Optional[dateutil.relativedelta.relativedelta]
        If matched, the relativedelta which was parsed. This can return `None`

    Raises
    ------
    BadArgument
        If the argument passed uses a unit not allowed, but understood
        or if the value is out of bounds.
    """
    allowed_units = allowed_units or [
        "years",
        "months",
        "weeks",
        "days",
        "hours",
        "minutes",
        "seconds",
    ]
    params = _parse_and_match(argument, allowed_units)
    if params:
        try:
            delta = relativedelta(**params)
        except OverflowError:
            raise BadArgument(
                _("The time set is way too high, consider setting something reasonable.")
            )
        return delta
    return None


class RawUserIdConverter(dpy_commands.Converter):
    """
    Converts ID or user mention to an `int`.

    Useful for commands like ``[p]ban`` or ``[p]unban`` where the bot is not necessarily
    going to share any servers with the user that a moderator wants to ban/unban.

    This converter doesn't check if the ID/mention points to an actual user
    but it won't match IDs and mentions that couldn't possibly be valid.

    For example, the converter will not match on "123" because the number doesn't have
    enough digits to be valid ID but, it will match on "12345678901234567" even though
    there is no user with such ID.
    """

    async def convert(self, ctx: "Context", argument: str) -> int:
        # This is for the hackban and unban commands, where we receive IDs that
        # are most likely not in the guild.
        # Mentions are supported, but most likely won't ever be in cache.

        if match := ID_REGEX.match(argument) or USER_MENTION_REGEX.match(argument):
            return int(match.group(1))

        raise BadArgument(_("'{input}' doesn't look like a valid user ID.").format(input=argument))


# Below this line are a lot of lies for mypy about things that *end up* correct when
# These are used for command conversion purposes. Please refer to the portion
# which is *not* for type checking for the actual implementation
# and ensure the lies stay correct for how the object should look as a typehint

if TYPE_CHECKING:
    DictConverter = Dict[str, str]
else:

    class DictConverter(dpy_commands.Converter):
        """
        Converts pairs of space separated values to a dict
        """

        def __init__(self, *expected_keys: str, delims: Optional[List[str]] = None):
            self.expected_keys = expected_keys
            self.delims = delims or [" "]
            self.pattern = re.compile(r"|".join(re.escape(d) for d in self.delims))

        async def convert(self, ctx: "Context", argument: str) -> Dict[str, str]:
            ret: Dict[str, str] = {}
            args = self.pattern.split(argument)

            if len(args) % 2 != 0:
                raise BadArgument()

            iterator = iter(args)

            for key in iterator:
                if self.expected_keys and key not in self.expected_keys:
                    raise BadArgument(_("Unexpected key {key}").format(key=key))

                ret[key] = next(iterator)

            return ret


if TYPE_CHECKING:

    def get_dict_converter(*expected_keys: str, delims: Optional[List[str]] = None) -> Type[dict]:
        ...

else:

    def get_dict_converter(*expected_keys: str, delims: Optional[List[str]] = None) -> Type[dict]:
        """
        Returns a typechecking safe `DictConverter` suitable for use with discord.py
        """

        class PartialMeta(type(DictConverter)):
            __call__ = functools.partialmethod(
                type(DictConverter).__call__, *expected_keys, delims=delims
            )

        class ValidatedConverter(DictConverter, metaclass=PartialMeta):
            pass

        return ValidatedConverter


if TYPE_CHECKING:
    TimedeltaConverter = timedelta
else:

    class TimedeltaConverter(dpy_commands.Converter):
        """
        This is a converter for timedeltas.
        The units should be in order from largest to smallest.
        This works with or without whitespace.

        See `parse_timedelta` for more information about how this functions.

        Attributes
        ----------
        maximum : Optional[datetime.timedelta]
            If provided, any parsed value higher than this will raise an exception
        minimum : Optional[datetime.timedelta]
            If provided, any parsed value lower than this will raise an exception
        allowed_units : Optional[List[str]]
            If provided, you can constrain a user to expressing the amount of time
            in specific units. The units you can choose to provide are the same as the
            parser understands: (``weeks``, ``days``, ``hours``, ``minutes``, ``seconds``)
        default_unit : Optional[str]
            If provided, it will additionally try to match integer-only input into
            a timedelta, using the unit specified. Same units as in ``allowed_units``
            apply.
        """

        def __init__(self, *, minimum=None, maximum=None, allowed_units=None, default_unit=None):
            self.allowed_units = allowed_units
            self.default_unit = default_unit
            self.minimum = minimum
            self.maximum = maximum

        async def convert(self, ctx: "Context", argument: str) -> timedelta:
            if self.default_unit and argument.isdecimal():
                argument = argument + self.default_unit

            delta = parse_timedelta(
                argument,
                minimum=self.minimum,
                maximum=self.maximum,
                allowed_units=self.allowed_units,
            )

            if delta is not None:
                return delta
            raise BadArgument()  # This allows this to be a required argument.


if TYPE_CHECKING:

    def get_timedelta_converter(
        *,
        default_unit: Optional[str] = None,
        maximum: Optional[timedelta] = None,
        minimum: Optional[timedelta] = None,
        allowed_units: Optional[List[str]] = None,
    ) -> Type[timedelta]:
        ...

else:

    def get_timedelta_converter(
        *,
        default_unit: Optional[str] = None,
        maximum: Optional[timedelta] = None,
        minimum: Optional[timedelta] = None,
        allowed_units: Optional[List[str]] = None,
    ) -> Type[timedelta]:
        """
        This creates a type suitable for typechecking which works with discord.py's
        commands.

        See `parse_timedelta` for more information about how this functions.

        Parameters
        ----------
        maximum : Optional[datetime.timedelta]
            If provided, any parsed value higher than this will raise an exception
        minimum : Optional[datetime.timedelta]
            If provided, any parsed value lower than this will raise an exception
        allowed_units : Optional[List[str]]
            If provided, you can constrain a user to expressing the amount of time
            in specific units. The units you can choose to provide are the same as the
            parser understands: (``weeks``, ``days``, ``hours``, ``minutes``, ``seconds``)
        default_unit : Optional[str]
            If provided, it will additionally try to match integer-only input into
            a timedelta, using the unit specified. Same units as in ``allowed_units``
            apply.

        Returns
        -------
        type
            The converter class, which will be a subclass of `TimedeltaConverter`
        """

        class PartialMeta(type(DictConverter)):
            __call__ = functools.partialmethod(
                type(DictConverter).__call__,
                allowed_units=allowed_units,
                default_unit=default_unit,
                minimum=minimum,
                maximum=maximum,
            )

        class ValidatedConverter(TimedeltaConverter, metaclass=PartialMeta):
            pass

        return ValidatedConverter


if TYPE_CHECKING:
    RelativedeltaConverter = relativedelta
else:

    class RelativedeltaConverter(dpy_commands.Converter):
        """
        This is a converter for relative deltas.

        The units should be in order from largest to smallest.
        This works with or without whitespace.

        See `parse_relativedelta` for more information about how this functions.

        Attributes
        ----------
        allowed_units : Optional[List[str]]
            If provided, you can constrain a user to expressing the amount of time
            in specific units. The units you can choose to provide are the same as the
            parser understands: (``years``, ``months``, ``weeks``, ``days``, ``hours``, ``minutes``, ``seconds``)
        default_unit : Optional[str]
            If provided, it will additionally try to match integer-only input into
            a timedelta, using the unit specified. Same units as in ``allowed_units``
            apply.
        """

        def __init__(self, *, allowed_units=None, default_unit=None):
            self.allowed_units = allowed_units
            self.default_unit = default_unit

        async def convert(self, ctx: "Context", argument: str) -> relativedelta:
            if self.default_unit and argument.isdecimal():
                argument = argument + self.default_unit

            delta = parse_relativedelta(argument, allowed_units=self.allowed_units)

            if delta is not None:
                return delta
            raise BadArgument()  # This allows this to be a required argument.


if not TYPE_CHECKING:

    class NoParseOptional:
        """
        This can be used instead of `typing.Optional`
        to avoid discord.py special casing the conversion behavior.

        .. seealso::
            The `ignore_optional_for_conversion` option of commands.
        """

        def __class_getitem__(cls, key):
            if isinstance(key, tuple):
                raise TypeError("Must only provide a single type to Optional")
            return key


_T = TypeVar("_T")

if not TYPE_CHECKING:
    #: This can be used when user input should be converted as discord.py
    #: treats `typing.Optional`, but the type should not be equivalent to
    #: ``typing.Union[DesiredType, None]`` for type checking.
    #:
    #: Note: In type checking context, this type hint can be passed
    #: multiple types, but such usage is not supported and will fail at runtime
    #:
    #: .. warning::
    #:    This converter class is still provisional.
    UserInputOptional = Optional

if TYPE_CHECKING:
    CommandConverter = dpy_commands.Command
    CogConverter = dpy_commands.Cog
else:

    class CommandConverter(dpy_commands.Converter):
        """Converts a command name to the matching `redbot.core.commands.Command` object."""

        async def convert(self, ctx: "Context", argument: str):
            arg = argument.strip()
            command = ctx.bot.get_command(arg)
            if not command:
                raise BadArgument(_('Command "{arg}" not found.').format(arg=arg))
            return command

    class CogConverter(dpy_commands.Converter):
        """Converts a cog name to the matching `redbot.core.commands.Cog` object."""

        async def convert(self, ctx: "Context", argument: str):
            arg = argument.strip()
            cog = ctx.bot.get_cog(arg)
            if not cog:
                raise BadArgument(_('Cog "{arg}" not found.').format(arg=arg))
            return cog
