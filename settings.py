import os
from dataclasses import dataclass

from dotenv import load_dotenv
from pydantic import SecretStr


def _get_secret_str(env_key: str) -> SecretStr | None:
    """
    从环境变量中读取一个 `SecretStr` 实例。
    Parameters
    ----------
    env_key

    Returns
    -------

    """
    env_value = os.getenv(env_key)
    return SecretStr(env_value) if env_value else None

@dataclass
class Settings:
    deepseek_api_key: SecretStr | None


    @classmethod
    def from_env(cls):
        load_dotenv()
        return cls(
            deepseek_api_key = _get_secret_str("DEEPSEEK_API_KEY")
        )


# 单例 settings
settings = Settings.from_env()