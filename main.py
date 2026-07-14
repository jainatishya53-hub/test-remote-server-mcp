from fastmcp import FastMCP
import random
import json

# Create the FastMCP server instance
mcp = FastMCP("Simple Calculator Server")


# Tool 1 - add two given numbers
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
       
       Args:
         a: first number
         b: second number
        
       Returns:
         sum of the two numbers
    """
    return a + b


# Tool 2 - generate a random number in a given range
@mcp.tool()
def random_number(minimum: int = 1, maximum: int = 100 )  -> int:
    """Generate a random number between minimum and maximum.
       
       Args:
         minimum: minimum value of the range (default : 1)
         maximum: maximum value of the range (default : 100)
        
       Returns:
         random number between minimum and maximum
    
    """
    return random.randint(minimum, maximum)


# Resource - some information about the server
@mcp.resource("info:///server")
def server_info() -> str:
    """Basic information about this server."""

    info = {
        'name': "Simple Calculator Server",
        'version': "1.0.0",
        'description': 'A basic MCP Server with math tools',
        'tools': ["add", "random_number"], 
        'author': "Atishya Jain"
    }
    
    return "Simple Calculator Server - tools: add, random_number"


# THE ONLY REAL CHANGE FOR A REMOTE SERVER
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
    