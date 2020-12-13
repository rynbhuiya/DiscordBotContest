from discord.ext import commands

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("HI")

client.run("Nzg3NDcwNjE5Nzg0MzgwNDM2.X9VbKg.t490I-30sP44aTyE_EMEfcjWJkw")