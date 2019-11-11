import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import discord.embeds

# Hidden Token from the environment variables file
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix="/")


@client.event
async def on_ready():
    print("Bot is online.")


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     await message.channel.send("I am going to")
#     await message.channel.send(client.emojis[0])
#     await message.channel.send("your world!!!!")

userID = []
run = []
on = [False]


@client.event
async def on_message(message):
    i = 0
    run.append(i)
    if message.author == client.user:
        await message.add_reaction(client.emojis[2])
        await message.add_reaction(client.emojis[3])
        await message.add_reaction(client.emojis[4])
        await message.add_reaction(client.emojis[5])
        await message.add_reaction(client.emojis[6])
        await message.add_reaction(client.emojis[7])
        await message.add_reaction(client.emojis[8])
        await message.add_reaction(client.emojis[9])
        await message.add_reaction(client.emojis[10])
    if message.author == client.user:
        return
    if message.content.startswith("/TTT"):
        if len(userID) < 2:
            userID.append(message.author.name)
        if len(userID) == 2:
            if on[0] == False:
                on[0] = True
                tic = discord.Embed()
                tic.add_field(
                    name=("{} vs. {}".format(str(userID[0]), str(userID[1]))),
                    value=":white_large_square: | :white_large_square: | :white_large_square: \n \n:white_large_square: | :white_large_square: | :white_large_square:  \n \n :white_large_square: | :white_large_square: | :white_large_square:",
                )
                await message.channel.send(embed=tic)


# i = []
# @client.event
# async def on_reaction_add(reaction, user):
#     i.append("1")
#     if len(i) == 2:
#         if client.emojis[2] == reaction.emoji:
#             print("1")
#         if client.emojis[3] == reaction.emoji:
#             print("2")
#         if client.emojis[4] == reaction.emoji:
#             print("3")
#         if client.emojis[5] == reaction.emoji:
#             print("4")
#         if client.emojis[6] == reaction.emoji:
#             print("5")
#         if client.emojis[7] == reaction.emoji:
#             print("6")
#         if client.emojis[8] == reaction.emoji:
#             print("7")
#         if client.emojis[9] == reaction.emoji:
#             print("8")
#         if client.emojis[10] == reaction.emoji:
#             print("9")


client.run(token)
