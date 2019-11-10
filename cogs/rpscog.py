import discord
from discord.ext import commands, tasks

class rps(commands.Cog): 

    def __init__(self, client):
        self.client = client
    
    # Events
    @commands.Cog.list
    async def on_ready(self):
        await self.client.change(activity = discord.Game('RPS Ready'))
    # Commands

