# 📰 MCP RSS News Aggregator

A Model Context Protocol (MCP) server that provides RSS feed aggregation capabilities for AI assistants. This server allows you to fetch and parse RSS feeds from various news sources and websites.

## 🚀 Features

- 📡 Fetch RSS feeds from any URL
- 🔢 Configurable number of entries to retrieve
- ⏰ Timestamp extraction from published/updated dates
- 🛡️ Error handling for malformed feeds
- 🐳 Docker support for easy deployment
- 🔗 Compatible with VS Code and Cursor AI assistants

## 📋 Prerequisites

- Docker
- VS Code or Cursor IDE

### 📱 VS Code Integration

2. **Install the MCP extension** (if available) or configure MCP client

3. **Add server configuration** to your VS Code settings:

   ```json
   {
     "mcp.servers": {
       "feed": {
                "type": "stdio",
                "command": "docker",
                "args": [
                    "run",
                    "-i",
                    "--rm",
                    "ghcr.io/edersonbadeca/rss-server:latest"
                ],
            }
   }
   ```

4. **Usage in VS Code /Cursor**:
   - Open the command palette (`Cmd+Shift+P` on macOS, `Ctrl+Shift+P` on Windows/Linux)
   - Type "MCP" to access MCP-related commands
   - Use the RSS server tools in your AI assistant interactions

## 🔧 Available Tools

### `get_feed`

Fetches and parses RSS feeds from a given URL.

**Parameters:**

- `url` (string): The RSS feed URL
- `num_entries` (int, optional): Number of entries to retrieve (default: 10)

**Returns:**

- Array of feed entries with title, link, and published timestamp

**Example usage in AI chat:**

```
"Can you fetch the latest 5 articles from https://feeds.feedburner.com/TechCrunch?"
```

## 📚 API Examples

### Basic Feed Fetching

```python
# The tool will be called automatically by the AI assistant
# Example prompt: "Get me the latest news from BBC RSS feed"
```

### Custom Number of Entries

```python
# Example prompt: "Fetch 20 articles from the Reuters RSS feed"
```

## 🐳 Docker Configuration

The included `Dockerfile` provides a containerized environment with:

- Python 3.13.3 slim base image
- All required dependencies pre-installed
- Optimized for production deployment

## 🔍 Troubleshooting

### Common Issues

1. **Feed parsing errors**:
   - Check if the URL is a valid RSS feed
   - The server handles malformed feeds gracefully with warnings

2. **Connection issues**:
   - Verify internet connectivity
   - Check if the RSS URL is accessible

3. **VS Code/Cursor integration**:
   - Ensure the Docker container is running
   - Check the configuration paths in settings
   - Verify Docker is properly installed and accessible

### Debug Mode

Check the Docker container logs for detailed error messages:

```bash
docker logs mcp-rss-server
```

Or run the container in interactive mode to see real-time logs:

```bash
docker run -it mcp-rss-server
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source. Please check the license file for details.

## 🆘 Support

For issues and questions:

- Check the troubleshooting section above
- Review the MCP documentation
- Create an issue in the project repository

## 🎉 Acknowledgments

- Built with [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- Uses [feedparser](https://feedparser.readthedocs.io/) for RSS parsing
- Powered by [FastMCP](https://github.com/jlowin/fastmcp)

---

Made with ❤️ for the AI community