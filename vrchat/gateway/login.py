from __future__ import annotations

from dataclasses import dataclass

from httpx import AsyncClient, Response

from vrchat.interfaces.login import LoginGateway


class LoginGatewayImpl(LoginGateway):
    def __init__(self, http_client: AsyncClient):
        self.http_client = http_client

    async def do(
        self, username: str, password: str, path: str = "/auth/user"
    ) -> LoginResult:
        resp: Response = await self.http_client.get(path, auth=(username, password))
        print(resp.status_code, resp.cookies, resp.content)
        try:
            token = resp.cookies["auth"]
            return LoginResult(token)
        except KeyError as error:
            raise LoginFailedException from error


@dataclass
class LoginResult:
    token: str


class LoginFailedException(Exception):
    pass
