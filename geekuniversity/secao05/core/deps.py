from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession


from core.database import Session


async def get_session() -> Generator:  # type: ignore
    session: AsyncSession = Session()  # type: ignore

    try:
        yield session
    finally:
        await session.close()
