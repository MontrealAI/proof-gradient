from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from proof_gradient.config import settings


class Base(DeclarativeBase):
    pass


connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
engine = create_engine(settings.database_url, pool_pre_ping=True, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)


def init_db() -> None:
    from proof_gradient import models  # noqa: F401

    Base.metadata.create_all(bind=engine)


def reset_db() -> None:
    from proof_gradient import models  # noqa: F401

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
