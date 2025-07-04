import sys
import json
import feedparser
from mcp.server.fastmcp import FastMCP
import time

server = FastMCP("AI Newsletter RSS Server")

@server.tool()
def get_feed(context: dict, url: str, num_entries: int = 10) -> dict:
    print(f"INFO: Fetching feed from {url}", file=sys.stderr)
    try:
        feed = feedparser.parse(url)

        if feed.bozo:
            bozo_exception = feed.bozo_exception
            print(
                f"WARNING: Feed at {url} is malformed. Error: {bozo_exception}",
                file=sys.stderr,
            )

        entries_data = []
        for entry in feed.entries[:num_entries]:
            title = entry.get("title", "No Title")
            link = entry.get("link", "")

            published_timestamp = 0
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                published_timestamp = int(time.mktime(entry.published_parsed))
            elif hasattr(entry, "updated_parsed") and entry.updated_parsed:
                published_timestamp = int(time.mktime(entry.updated_parsed))

            entries_data.append(
                {
                    "title": title,
                    "link": link,
                    "published_timestamp": published_timestamp,
                }
            )

        return {
            "result": entries_data,
            "context": context
        }

    except Exception as e:
        print(
            f"ERROR: Failed to fetch or parse feed from {url}. Error: {e}",
            file=sys.stderr,
        )
        return {
            "result": [],
            "context": context
        }

if __name__ == "__main__":
    print("INFO: RSS MCP Server starting...", file=sys.stderr)
    server.run()
