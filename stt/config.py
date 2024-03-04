import dataclasses
import json
import os
from distutils.util import strtobool

from dotenv import load_dotenv

load_dotenv()


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class AppConfig:
    db_engine: str = "django.db.backends.postgresql"
    db_name: str = "postgres"
    db_host: str = "localhost"
    db_port: int = 5432
    db_user: str = "postgres"
    db_password: str = "postgres"
    allowed_hosts: list[str | None] = dataclasses.field(default_factory=list)
    secret_key: str
    debug: bool = False


def get_config() -> AppConfig:
    return AppConfig(
        db_engine=os.environ["DB_ENGINE"],
        db_name=os.environ["DB_NAME"],
        db_host=os.environ["DB_HOST"],
        db_port=int(os.environ["DB_PORT"]),
        db_user=os.environ["DB_USER"],
        db_password=os.environ["DB_PASSWORD"],
        secret_key=os.environ["DJANGO_SECRET_KEY"],
        debug=bool(strtobool(os.getenv("DEBUG", "false"))),
        allowed_hosts=json.loads(os.environ["ALLOWED_HOSTS"]),
    )


config = get_config()
