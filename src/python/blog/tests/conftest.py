import asyncio
from typing import AsyncIterator, Iterator

import pytest
from blog.main import app
from httpx import AsyncClient


@pytest.fixture(scope="session")
def event_loop() -> Iterator[asyncio.AbstractEventLoop]:
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def client() -> AsyncIterator[AsyncClient]:
    async with AsyncClient(app=app, base_url="http://test") as _client:
        yield _client
