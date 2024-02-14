from pathlib import Path
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

PATH_TO_HOME = Path(__file__).parent.parent.parent


class DBSetting(BaseSettings):
    model_config = SettingsConfigDict(env_file=f'{PATH_TO_HOME}/.env',
                                      env_prefix='DB_',
                                      case_sensitive=False)
    user: str
    port: int
    host: str
    password: str
    name: str
    uri: str

    @property
    def get_url(self) -> str:
        return self.uri.format(user=self.user,
                               password=self.password,
                               host=self.host,
                               port=self.port,
                               name=self.name
                               )


class AuthJWT(BaseSettings):
    private_key_path: Path = Path(__file__).parent.parent.parent / ".certs" / "jwt-private.pem"
    public_key_path: Path = Path(__file__).parent.parent.parent / ".certs" / "jwt-public.pem"
    ALGORITHM: str = "RS256"


class Settings(BaseSettings):
    db_setting: DBSetting = DBSetting()
    auth_jwt: AuthJWT = AuthJWT()


@lru_cache
def load_setting() -> Settings:
    return Settings()
