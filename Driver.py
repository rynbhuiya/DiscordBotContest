import os
from dotenv import load_dotenv
from discord.ext import commands
import discord
import NumberGame as ng
# import rpsbot as rps
import TicTacToe as ttt

client = commands.Bot(command_prefix = "!MGB ", self_bot = False)


@client.command(name = 'ng', 
help = "To start: \n!MGB ng <goal number here> \n\n"
+ "The goal of this game is to reach the goal without having people increment the counter at the same time",
brief = "Begin number name")
async def numberGame(ctx,goal):
    if not (ng.running):
        await ng.start(ctx.channel,goal,client)
        
# @client.command(name = 'rps',
#  brief = "Begin rock-paper-scissors", 
#  help =  "To start, do:\n!MGB ng @opponent\n\n"
#  + 'Each player must enter rock, paper or scissors via the reactions right when "GO!" comes up.\n'
#  + "rock > scissors, scissors > paper, paper > rock "
#  )
# async def rockPaperScissors(ctx):
#     if not (ng.running or rps.running  or ttt.running): #idk what params you need
#         await rps.start(ctx.message)
    

@client.command(name = 'ttt',
brief = "Begin tic-tack-toe",
help = "To start, within 15 seconds, both players must do:\n!MGB .ttt\n\n" +
"The goal is to get 3 of your piece in a row. Use the reactions below the board to choose your position!"
)
async def ticTacToe(ctx):
    if not (ng.running or ttt.running):
        await ttt.start(ctx.channel,ctx.author, client)

load_dotenv()
client.run(os.getenv("DISCORD_TOKEN"))