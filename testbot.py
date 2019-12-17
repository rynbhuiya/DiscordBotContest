import discord
import random
import os
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '/')

# @client.event
# async def on_ready():
#     print('Bot is ready')

# @client.event
# async def on_member_join(member):
#     print('Howdy', f'{member}', '!')

# @client.event
# async def on_member_remove(member):
#     print(f'{member} has left the cult.')

# @client.command()
# async def ping(ctx):
#     await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

# @client.command(aliases = ['8ball'])
# async def _8ball(ctx, *, question):
#     responses = ['My reply is no', 'Very doubtful', 'Most likely', 'Yes', 'Outlook not so good']
#     await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

# @client.command()
# @commands.has_permissions(manage_messages=True)
# async def clear(ctx, amount=10):
#     await ctx.channel.purge(limit=amount)

# Loading cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

# Unloading cogs
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NjQyOTE3ODI3MTM2OTc4OTY0.Xcd6cA.BCSLe7pTgjJcUoqT1gZ9p7H6YJc')

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as', self.user)

#     async def on_message(self, message):
#         # don't respond to ourselves
#         if message.author == self.user:
#             return

#         if message.content == 'Howdy':
#             await message.channel.send('Y E E H A W')

#client = MyClient()
#client.run('NjMwNTk0MTc1NzM3MjY2MTk2.XcdswQ.vsWFyk5KCvoA5IevBGTkNH-lhlo')