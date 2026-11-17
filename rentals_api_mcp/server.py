from mcp.server import MCPServer
from mcp.types import ToolAnnotations
from typing import Annotated
from pydantic import Field, BaseModel
import sqlite3


mcp = MCPServer(
    name = "rentals_api_mcp",
    title = "rentals_api_mcp",
    version="1.0.0",
    instructions= (
        "On-call assistant for the Magic stones Rentals API, Start with service_overview, then narrow down"
        "with compare_windows, latency_trend, error_breakdown, search_logs, rencent_deploys and"
        "errors_by_version, Quote every number with its time window, Ask the person before rollback deploy"

    )
)

@mcp.tool()
def healthz():
    pass