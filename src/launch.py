from mcp_server.main import mcp


if __name__ == "__main__":
    mcp.run(transport='sse')
