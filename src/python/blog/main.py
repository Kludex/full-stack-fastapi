import uvicorn  # type: ignore[import]
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home() -> None:
    ...


if __name__ == "__main__":  # pragma: no cover
    uvicorn.run(app, host="0.0.0.0", port=8000)
