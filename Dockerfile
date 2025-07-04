FROM python:3.13.3-slim

WORKDIR /app
COPY . /app
RUN pip install "mcp[cli]" feedparser python-dotenv uv

CMD ["uv", "run", "python", "rss_server.py"]
