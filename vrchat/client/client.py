from typing import Optional, Type

from httpx import AsyncClient

from vrchat.gateway.login import LoginGatewayImpl
from vrchat.interfaces.login import LoginGateway


class VRChat:
    def __init__(
        self,
        *,
        username: Optional[str] = None,
        password: Optional[str] = None,
        token: Optional[str] = None,
        host: str = "https://api.vrchat.cloud/api/1",
        api_key: str = "JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26",
        login_gateway: Type[LoginGateway] = LoginGatewayImpl
    ) -> None:
        if username and password:
            self.username = username
            self.password = password
        elif token:
            self.token = token
        else:
            raise NoAuthInformationException

        self.http_client = AsyncClient(
            base_url=host, params=api_key, headers={"User-Agent": "VRChat.py/0.1.0"}
        )

        self.login_gateway = login_gateway(self.http_client)

    async def login(self) -> None:
        username = getattr(self, "username", None)
        password = getattr(self, "password", None)
        if not (username and password):
            raise NoAuthInformationException

        login_result = await self.login_gateway.do(username, password)

        setattr(self, "token", login_result.token)


class NoAuthInformationException(Exception):
    pass
