FROM python:3.10.5-slim

WORKDIR /app

COPY src.python.blog/main.pex ./

CMD ["/app/main.pex", "blog.main:app", "--port", "8000", "--host", "0.0.0.0"]
