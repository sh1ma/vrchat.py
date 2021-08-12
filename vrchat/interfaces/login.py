from abc import ABC


class LoginGateway(ABC):
    async def do(self, username: str, password: str, path: str):
        ...
