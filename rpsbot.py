import discord
import random
import os
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def rps(ctx, user1 = discord.user, user2 = discord.user):
    ctx.send('User1 : ', user1.str(x))
    ctx.send('User1 : ', user2.str(x))

# Loading cogs
# @client.command()
# async def load(ctx, extension):
#     client.load_extension(f'cogs.{extension}')

# # Unloading cogs
# @client.command()
# async def unload(ctx, extension):
#     client.unload_extension(f'cogs.{extension}')

# for filename in os.listdir('./cogs'):
#     if filename.endswith('.py'):
#         client.load_extension(f'cogs.{filename[:-3]}')

client.run('NjQyOTE3ODI3MTM2OTc4OTY0.Xcd6cA.BCSLe7pTgjJcUoqT1gZ9p7H6YJc')