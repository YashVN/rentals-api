from mcp.server import MCPServer

mcp = MCPServer(
    name = "rentals_api_mcp",
    title = "rentals_api_mcp",
    version="1.0.0"
)

@mcp.tool()
def healthz():
    pass