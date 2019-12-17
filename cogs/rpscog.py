import discord
from discord.ext import commands, tasks

class Rpsgame(commands.Cog): 
    def __init__(self, client):
        self.client = client
        self._last_member = None

    
    # Events
    @commands.Cog.list
    async def on_ready(self):
        await self.client.change(activity = discord.Game('RPS Ready'))
    # Commands


