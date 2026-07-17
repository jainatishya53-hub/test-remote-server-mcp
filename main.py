import random
import json
from fastmcp import FastMCP

mcp = FastMCP('Simple Calculator Server')


# Tool 1 : add two numbers
@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers together and return the result.
    
       Args:
        a: First Number
        b: Second Number
        
       Returns:
        The sum of a and b 
    """
    
    return a + b


# Tool 2 : random number
@mcp.tool
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """Generate a random integer between min_val and max_val, inclusive."""

    return random.randint(min_val, max_val)


# Resource : Server information
@mcp.resource("server://info")
def server_info() -> str:
    """Return information about the server."""
    info = {
        "name": "Simple calculator Server",
        "version": "1.0.0",
        "description": "A remote MCP server providing mathematical utilities.",
        "tools": ["add", "random_number"],
        "author": "Atishya Jain",
    }


# Start the server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port = 8000)