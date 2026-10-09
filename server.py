
import hashlib
import os

from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_headers

EMAIL = "25ds3000005@ds.study.iitm.ac.in"

mcp = FastMCP("IITM Exam MCP Server")


@mcp.tool(name="solve_challenge")
def solve_challenge() -> str:
    headers = get_http_headers(include_all=True)
    challenge = headers.get("x-exam-challenge")

    if not challenge:
        raise ValueError("Missing X-Exam-Challenge header")

    text = f"{challenge}:{EMAIL}"
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "8000")),
    )
