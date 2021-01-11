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
        # self.pogger.start()
    
    # def cog_unload(self):
    #     self.printer.cancel()

    # @tasks.loop(hours=24)
    @commands.command()
    async def pogger(self, ctx):
        async with self.bot.http2.get("https://pogchamp.today/data.json") as resp:
            data = await resp.json()
            img = await process_url(data["img"]["medium"], self.bot.http2)
            buff = BytesIO()
            img.save(buff, format="png")
            buff.seek(0)
            await ctx.send(file=discord.File(buff, "out.png"))
            

def setup(client):
    client.add_cog(TaskCog(client))