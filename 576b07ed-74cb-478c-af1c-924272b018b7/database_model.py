from globals import client
import datetime


class Bdate:
    def __init__(self, m, d):
        try:
            datetime.datetime(1999, m, d)
        except Exception as e:
            raise ValueError(e)
        self._month = m
        self._day = d

    def getMonth(self):
        return self._month

    def getDay(self):
        return self._day

    def __str__(self):
        month = str(self._month) if self._month > 9 else "0" + str(self._month)
        day = str(self._day) if self._day > 9 else "0" + str(self._day)
        return month + "/" + day

    def __add__(self, other):
        return self.__str__() + other

    def __radd__(self, other):
        return other + self.__str__()


class Birthday:
    def __init__(self, user_id, month, day, guild_id, greeted=False):
        self._user_id = user_id
        self._birthday = Bdate(int(month), int(day))
        self._guild_id = guild_id
        self._greeted_this_year = greeted

    def setGreetedThisYear(self, boolean):
        self._greeted_this_year = boolean

    def greetedThisYear(self):
        return self._greeted_this_year

    def getBirthday(self):
        return self._birthday

    def getUser(self):
        return self._user_id

    def getGuild(self):
        return self._guild_id

    def __str__(self):
        member = client.get_guild(self._guild_id).get_member(self._user_id)
        name = member.nick if member.nick != None else member.name
        bd = name + ("'" if name[-1].lower() == "s" else "'s")
        greeted = " birthday " + ("was on " if self._greeted_this_year else
                                  "is on ") + self._birthday
        return bd + greeted

    def __add__(self, other):
        return self.__str__() + other

    def __radd__(self, other):
        return other + self.__str__()


class Birthdays:
    def __init__(self):
        self._records = []

    def getRecords(self):
        return self._records

    def append(self, birthday) -> bool:
        for bd in self._records:
            if bd.getUser() == birthday.getUser() and bd.getGuild(
            ) == birthday.getGuild():
                return False
        self._records.append(birthday)
        return True

    def delete(self, user_id, guild_id) -> bool:
        for birthday in self._records:
            if birthday.getUser() == user_id and birthday.getGuild(
            ) == guild_id:
                self._records.remove(birthday)
                return True
        return False

    def resetGreets(self):
        for birthday in self._records:
            if birthday.greetedThisYear():
                birthday.setGreetedThisYear(False)

    def list(self, guild_id):
        msg = ""
        empty = True
        for bd in self._records:
            if bd.getGuild() == guild_id:
                empty = False
                msg += bd + "\n"
        if empty:
            msg = "There were no birthdays found."
        return msg

    def __str__(self):
        return "You should use the list(guild_id) method to stringify this object."
