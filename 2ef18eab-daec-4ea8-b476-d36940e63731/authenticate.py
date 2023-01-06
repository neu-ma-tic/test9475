
import argparse
import asyncio
import os
import webbrowser
from aiohttp import ClientSession, web

from xbox.webapi.authentication.manager import AuthenticationManager
from xbox.webapi.authentication.models import OAuth2TokenResponse
from xbox.webapi.scripts import TOKENS_FILE

CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = "http://localhost:8080/auth/callback"
TOKENS = ""
from xbox.webapi.scripts import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, TOKENS_FILE

queue = asyncio.Queue(1)



async def async_main():
  async def async_main(
    client_id: str, client_secret: str, redirect_uri: str, token_filepath: str
):

    async with ClientSession() as session:
        auth_mgr = AuthenticationManager(
            session, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
            session, client_id, client_secret, redirect_uri
        )

        # Refresh tokens if we have them
        if os.path.exists(TOKENS):
            with open(TOKENS, mode="r") as f:
        if os.path.exists(token_filepath):
            with open(token_filepath, mode="r") as f:
                tokens = f.read()
            auth_mgr.oauth = OAuth2TokenResponse.parse_raw(tokens)
            await auth_mgr.refresh_tokens()
@@ -55,29 +52,39 @@ async def async_main():
            code = await queue.get()
            await auth_mgr.request_tokens(code)

        with open(TOKENS, mode="w") as f:
        with open(token_filepath, mode="w") as f:
            f.write(auth_mgr.oauth.json())


def main():
    global CLIENT_ID, CLIENT_SECRET, TOKENS
    parser = argparse.ArgumentParser(description="Authenticate with XBL")
    parser.add_argument(
        "--tokens",
        "-t",
        default=TOKENS_FILE,
        help=f"Token filepath. Default: '{TOKENS_FILE}'",
    )
    parser.add_argument("--client-id", "-cid", help="OAuth2 Client ID")
    parser.add_argument("--client-secret", "-cs", help="OAuth2 Client Secret")
    parser.add_argument(
        "--client-id",
        "-cid",
        default=os.environ.get("CLIENT_ID", CLIENT_ID),
        help="OAuth2 Client ID",
    )
    parser.add_argument(
        "--client-secret",
        "-cs",
        default=os.environ.get("CLIENT_SECRET", CLIENT_SECRET),
        help="OAuth2 Client Secret",
    )
    parser.add_argument(
        "--redirect-uri",
        "-ru",
        default=os.environ.get("REDIRECT_URI", REDIRECT_URI),
        help="OAuth2 Redirect URI",
    )

    args = parser.parse_args()

    # pylint: disable=unused-variable
    CLIENT_ID = args.client_id or os.environ.get("CLIENT_ID", "")
    CLIENT_SECRET = args.client_secret or os.environ.get("CLIENT_SECRET", "")
    TOKENS = args.tokens

    app = web.Application()
    app.add_routes([web.get("/auth/callback", auth_callback)])
    runner = web.AppRunner(app)
@@ -86,7 +93,9 @@ def main():
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner, "localhost", 8080)
    loop.run_until_complete(site.start())
    loop.run_until_complete(async_main())
    loop.run_until_complete(
        async_main(args.client_id, args.client_secret, args.redirect_uri, args.tokens)
    )


if __name__ == "__main__":
  6  xbox/webapi/scripts/change_gamertag.py 
"""
Example script that enables using your one-time-free gamertag change
"""
import argparse
import asyncio
import os
import sys
from aiohttp import ClientResponseError, ClientSession
from xbox.webapi.api.client import XboxLiveClient
from xbox.webapi.api.provider.account.models import (
    ChangeGamertagResult,
    ClaimGamertagResult,
)
from xbox.webapi.authentication.manager import AuthenticationManager
from xbox.webapi.authentication.models import OAuth2TokenResponse
from xbox.webapi.scripts import TOKENS_FILE
from xbox.webapi.scripts import CLIENT_ID, CLIENT_SECRET, TOKENS_FILE


async def async_main():
    parser = argparse.ArgumentParser(description="Change your gamertag")
    parser.add_argument(
        "--tokens",
        "-t",
        default=TOKENS_FILE,
        help=f"Token filepath. Default: '{TOKENS_FILE}'",
    )
    parser.add_argument(
        "--client-id",
        "-cid",
        default=os.environ.get("CLIENT_ID", ""),
        default=os.environ.get("CLIENT_ID", CLIENT_ID),
        help="OAuth2 Client ID",
    )
    parser.add_argument(
        "--client-secret",
        "-cs",
        default=os.environ.get("CLIENT_SECRET", ""),
        default=os.environ.get("CLIENT_SECRET", CLIENT_SECRET),
        help="OAuth2 Client Secret",
    )
    parser.add_argument("gamertag", help="Desired Gamertag")
    args = parser.parse_args()
    if len(args.gamertag) > 15:
        print("Desired gamertag exceedes limit of 15 chars")
        sys.exit(-1)
    if not os.path.exists(args.tokens):
        print("No token file found, run xbox-authenticate")
        sys.exit(-1)
    async with ClientSession() as session:
        auth_mgr = AuthenticationManager(
            session, args.client_id, args.client_secret, ""
        )
        with open(args.tokens, mode="r") as f:
            tokens = f.read()
        auth_mgr.oauth = OAuth2TokenResponse.parse_raw(tokens)
        try:
            await auth_mgr.refresh_tokens()
        except ClientResponseError:
            print("Could not refresh tokens")
            sys.exit(-1)
        with open(args.tokens, mode="w") as f:
            f.write(auth_mgr.oauth.json())
        xbl_client = XboxLiveClient(auth_mgr)
        print(
            ":: Trying to change gamertag to '%s' for xuid '%i'..."
            % (args.gamertag, xbl_client.xuid)
        )
        print("Claiming gamertag...")
        try:
            resp = await xbl_client.account.claim_gamertag(
                xbl_client.xuid, args.gamertag
            )
            if resp == ClaimGamertagResult.NotAvailable:
                print("Claiming gamertag failed - Desired gamertag is unavailable")
                sys.exit(-1)
        except ClientResponseError:
            print("Invalid HTTP response from claim")
            sys.exit(-1)
        print("Changing gamertag...")
        try:
            resp = await xbl_client.account.change_gamertag(
                xbl_client.xuid, args.gamertag
            )
            if resp == ChangeGamertagResult.NoFreeChangesAvailable:
                print("Changing gamertag failed - You are out of free changes")
                sys.exit(-1)
        except ClientResponseError:
            print("Invalid HTTP response from change")
            sys.exit(-1)
        print("Gamertag successfully changed to %s" % args.gamertag)
def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())
if __name__ == "__main__":
    main()