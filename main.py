from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Trox_Calculator")


@mcp.tool()
def trox_tool(a: int, b: int) -> int:
    """Add two numbers using Trox_Calculator."""
    return a + b + 100


if __name__ == "__main__":
    mcp.run()
