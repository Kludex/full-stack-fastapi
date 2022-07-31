python_sources(
    dependencies=[
        "//:root#uvicorn",
        "//:root#uvloop",
        "//:root#httptools",
    ],
)

pex_binary(
    name="main",
    script="uvicorn",
    dependencies=[":blog"],
)
