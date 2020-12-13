import discord
import discord.embeds
import asyncio

running = False #is gameRunning

async def start(channel, client):
    global running
    if(running):
        channel.send('A TicTacToe game is already running!')
    running = True

#     tic = discord.Embed(title="{} vs. {}".format(
#     str(on_message.userID[0])+"  :x:", str(on_message.userID[1])+"  :o:"), colour=discord.Colour.red())
# on_message.board = [":one:", ":two:", ":three:", ":four:",":five:", ":six:", ":seven:", ":eight:", ":nine:"] #emojis for game board 
# on_message.emarr = [[], [], []]


async def runGame():
    pass

