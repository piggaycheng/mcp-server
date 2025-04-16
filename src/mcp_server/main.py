import os
from typing import Optional

import httpx
from dotenv import load_dotenv
from fastmcp import FastMCP

from .model.weather import WeatherResponse


# Load environment variables from .env file
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("Demo")


@mcp.tool("Weather forecast", description="Get weather forecast")
async def get_weather_forecast(location: Optional[str]) -> WeatherResponse:
    """
    Get weather forecast for a location.

    Args:
        location: City name or location name.
    Returns:
        Weather forecast data.
    """

    # 取得 API 金鑰
    api_key = os.getenv("OPEN_DATA_WEATHER_API_KEY")
    if not api_key:
        print("API key is missing. Please check your .env file.")
        return

    # API URL 和參數
    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"
    params = {
        "Authorization": api_key,
        "locationName": location,
    }

    # 呼叫 API
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params, headers={"accept": "application/json"})
            response.raise_for_status()  # 檢查 HTTP 狀態碼
            data = response.json()
            print("Weather forecast data:", data)
        except httpx.HTTPStatusError as e:
            print(
                f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        except Exception as e:
            print(f"An error occurred: {e}")

    return data


@mcp.tool("Sum", description="Sum two numbers")
async def sum(a: int, b: int) -> int:
    """
    Sum two numbers.

    Args:
        a: First number.
        b: Second number.
    Returns:
        The sum of a and b.
    """
    return a + b


@mcp.tool("Subtract", description="Subtract two numbers")
async def subtract(a: int, b: int) -> int:
    """
    Subtract two numbers.

    Args:
        a: First number.
        b: Second number.
    Returns:
        The result of subtracting b from a.
    """
    return a - b

print(get_weather_forecast.__doc__)
