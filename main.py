from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Trox_Calculator")


@mcp.tool()
def trox_tool(a: int, b: int) -> int:
    """Add two numbers using trox calculator."""
    return a + b + 100


if __name__ == "__main__":
    mcp.run()
