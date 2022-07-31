from httpx import AsyncClient


async def test_home(client: AsyncClient) -> None:
    res = await client.get("/")
    assert res.status_code == 200
    assert res.json() is None
