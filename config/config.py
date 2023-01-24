from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str # access token

@dataclass
class Config:
    tg_bot: TgBot  


def load_config(path: str or None) -> Config:
    env: Env = Env()
    env.read_env()
    return Config(tg_bot=TgBot(token=env('TOKEN')))