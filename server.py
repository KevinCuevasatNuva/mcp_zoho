import asyncio
import os
from fastmcp import FastMCP

mcp = FastMCP("MCP-CloudRun-Server")

@mcp.tool()
def calcular_descuento(precio: float, porcentaje: float) -> float:
    """
    Calcula el precio final aplicando un porcentaje de descuento.
    Utilízame cuando el usuario quiera calcular rebajas o promociones.
    """
    return precio * (1 - (porcentaje / 100))

if __name__ == "__main__":
    puerto = int(os.getenv("PORT", 8080))
    asyncio.run(
        mcp.run_async(
            transport="streamable-http",
            host="0.0.0.0",
            port=puerto
        )
    )
    