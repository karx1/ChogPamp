import asyncio
from discord.ext import commands
from PIL import Image
from io import BytesIO
import aiohttp


async def process_url(url, http):

    try:
        async with http.get(url) as resp:
            img = Image.open(BytesIO(await resp.content.read())).convert("RGB")
    except aiohttp.InvalidURL:
        print("That URL is invalid!!!!")
        return

    return img
