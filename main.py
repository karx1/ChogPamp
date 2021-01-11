import aiohttp
import discord
from discord.ext import commands


class customBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.http2 = None

        super().__init__(*args, **kwargs)

    async def on_ready(self):
        if not self.http2:
            self.http2 = aiohttp.ClientSession()
        print("Servers:")
        async for guild in self.fetch_guilds():
            print(guild.name)
        self.load_extension("task")
        self.load_extension("jishaku")

        print(
            discord.utils.oauth_url(
                self.user.id, permissions=discord.Permissions(1073742848)
            )
        )


bot = customBot(command_prefix="pog_", description="Changes the server's pog emote every 24 hours.", intents=discord.Intents.all())

token_file = open("token.txt", "r")
token_string = token_file.read()
token = "".join(token_string.split())
bot.run(token)
