import discord
from discord.ext import commands, tasks
from prog_img import process_url
import aiohttp
from io import BytesIO

# class MyCog(commands.Cog):
#     def __init__(self):
#         self.index = 0
#         self.printer.start()

#     def cog_unload(self):
#         self.printer.cancel()

#     @tasks.loop(seconds=5.0)
#     async def printer(self):
#         print(self.index)
#         self.index += 1

class TaskCog(commands.Cog):
    def __init__(self, client):
        self.bot = client
        self.pogger.start()
    
    def cog_unload(self):
        self.pogger.cancel()

    @tasks.loop(hours=24)
    # @commands.command()
    async def pogger(self):
        async with self.bot.http2.get("https://pogchamp.today/data.json") as resp:
            data = await resp.json()
            url = data["img"]["medium"]
            img = await process_url(url, self.bot.http2)
            buff = BytesIO()
            img.save(buff, format="png")
            buff.seek(0)
            
            async for guild in self.bot.fetch_guilds():
                emojis = await guild.fetch_emojis()
                emoji = discord.utils.get(emojis, name="pog")
                if emoji:
                    print(emoji)
                    await emoji.delete()

                print("creating...")
                emoji = await guild.create_custom_emoji(name="pog", image=buff.getvalue())
                if emoji:
                    print(emoji)


def setup(client):
    client.add_cog(TaskCog(client))