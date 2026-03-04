import asyncio
import logging
import os

from fastmcp import FastMCP 

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

mcp = FastMCP("MCP Server on Cloud Run")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Use this to add two numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of the two numbers.
    """
    logger.info(f">>> 🛠️ Tool: 'add' called with numbers '{a}' and '{b}'")
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Use this to subtract two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The difference of the two numbers.
    """
    logger.info(f">>> 🛠️ Tool: 'subtract' called with numbers '{a}' and '{b}'")
    return a - b

@mcp.tool()
def validate_account(account_number: str) -> str:
    """Checks if an account number (e.g., 12345) is valid.
     Args:
        account_number: The account number.
        b: The second number.

    Returns:
        userfirstName: The user first name.
        status: Success or error
        account: the account number
    """

    if len(account_number) >= 5:
        #return f"SUCCESS: Account {account_number} is valid."
        return f'{{"status": "SUCCESS", "userfirstName": "Mike", "account": "{account_number}"}}'
    return '{"status": "ERROR", "message": "Account not found or invalid format"}'

if __name__ == "__main__":
    logger.info(f"🚀 MCP server started on port {os.getenv('PORT', 8080)}")
    # Could also use 'sse' transport, host="0.0.0.0" required for Cloud Run.
    asyncio.run(
        mcp.run_async(
            transport="streamable-http",
            host="0.0.0.0",
            port=os.getenv("PORT", 8080),
        )
    )