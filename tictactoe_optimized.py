import discord
import discord.reaction
import discord.embeds
import asyncio
from discord.ext import commands
import os
from dotenv import load_dotenv

# Hidden Token from the environment variables file
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix='.')  # Change the command prefix


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#Reset function for repeating games
async def reset():
    on_message.repeat=True
    on_message.won=False
    on_message.gamestatus_ttt = False
    on_reaction_add.j = 0
    on_reaction_add.checks_counter = [0,0,0,0,0,0,0,0]
    on_reaction_add.locals = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2]}
    w = 0
    on_message.userID = []

@client.event
async def on_message(message): #On message 
    if message.author == client.user:
        return
    if message.content.startswith(".ttt"): #Text to start the game. Game starts with two members typing '.ttt'
        if on_message.gamestatus_ttt == True: # Check to see if a game is already on
            await message.channel.send('Game in Progress')
            return
        if len(on_message.userID) < 2: #until two people type .ttt
            on_message.userID.append(message.author.name)
            print(message.author.name)
        if len(on_message.userID) == 2: #Once there are two people ready to play
            # if on_message.userID[0]==on_message.userID[1]: # Checks if the same person typed the message and resets conditions
            #     await message.channel.send('Cannot be the same person')
            #     await reset()
            #     return
            on_message.gamestatus_ttt = True
            tic = discord.Embed(title="{} vs. {}".format(
                str(on_message.userID[0])+"  :x:", str(on_message.userID[1])+"  :o:"), colour=discord.Colour.red())
            on_message.board = [":one:", ":two:", ":three:", ":four:",":five:", ":six:", ":seven:", ":eight:", ":nine:"] #emojis for game board 
            on_message.emarr = [[], [], []]

            b = 0 #Putting the emojis into a 3 x 3 matrix
            while b < 9:
                for i in range(3):
                    for j in range(3):
                        on_message.emarr[i].append(on_message.board[b]) 
                        b += 1
            # making a text board of the emojis seperated by | for the embed
            val = ""
            for i in range(3):
                val += " | "
                for k in range(3):
                    val += on_message.emarr[i][k] + " | "
                val += "\n \n"

            tic.add_field(
                name=("Your turn:  ❌ \n"),
                value=val # The game board made above for the embed 
            )
            msg = await message.channel.send(embed=tic)
            on_message.em = msg # Used to check if we are on the correct game message
            for i in range(2, 11):
                await msg.add_reaction(client.emojis[i]) # Showing the reactions that are buttons to control the board
    on_message.moves=on_reaction_add.j
    await asyncio.sleep(30)            # turn off the game and reset
    if on_message.gamestatus_ttt == True and on_message.em.id != message.id and on_message.moves==on_reaction_add.j:
        await reset()
        await message.channel.send("TicTacToe game stopped due to inactivity")

@client.event
async def on_reaction_add(reaction, user):
    if on_message.gamestatus_ttt == False:
        return
    if on_message.em.id != reaction.message.id:
        return
    if user == client.user:
        return
    # moves=on_reaction_add.j
    # await asyncio.sleep(30)            # turn off the game and reset
    # if on_message.gamestatus_ttt == True and on_message.em.id != reaction.id and moves==on_reaction_add.j:
    #     await reset()
    #     await reaction.channel.send("TicTacToe game stopped due to inactivity")
    count = 0
    for i in range(2, 11):
        if reaction.emoji == client.emojis[i]: #Checks what reaction emoji was clicked
            if on_reaction_add.j % 2 == 0: #Checks what turn we are on
                if user.name == on_message.userID[0]:  #If we are on the first user
                    on_reaction_add.j += 1
                    v = ":x:"
                    t = ":o:"
                else:
                    return
            else:
                if user.name == on_message.userID[1]: #If we are on the second user
                    on_reaction_add.j += 1
                    v = ":o:"
                    t = ":x:"

                else:
                    return

            if (on_message.emarr[on_reaction_add.locals[i-1][0]][on_reaction_add.locals[i-1][1]] not in on_message.board):
                on_reaction_add.j -= 1
                return
            else: # Changes the desired emoji on the desired number emoji of the board with an x or o depending on the turn 
                on_message.emarr[on_reaction_add.locals[i-1][0]][on_reaction_add.locals[i-1][1]]=v

                # Remake val with for the updated emebed board
                val = ""
                for l in range(3):
                    val += " | "
                    for k in range(3):
                        val += on_message.emarr[l][k] + " | "
                    val += "\n \n"
                new = discord.Embed(title="{} vs. {}".format(
                    str(on_message.userID[0])+"  :x:", str(on_message.userID[1])+"  :o:"), colour=discord.Colour.red())
                new.add_field(
                    name=("Your turn: " + t + "\n"), value=val) # Changes to next user
                await on_message.em.edit(embed=new) #send new edited embed to same message 

            # Check the input and the corresponding rows, columns, and/or diagonals to see if a three X's or O's
            if v==":x:":
                add_val = 1
            else:
                add_val = -1

            on_reaction_add.checks_counter[on_reaction_add.locals[i-1][0]]+=add_val
            on_reaction_add.checks_counter[on_reaction_add.locals[i-1][1]+3]+=add_val

            if on_reaction_add.locals[i-1][0] == on_reaction_add.locals[i-1][1]:
                on_reaction_add.checks_counter[6]+=add_val
                    
            if (on_reaction_add.locals[i-1][0] + on_reaction_add.locals[i-1][1] == 2):
                on_reaction_add.checks_counter[7]+=add_val

            if (abs(on_reaction_add.checks_counter[on_reaction_add.locals[i-1][0]]) == 3) or (abs(on_reaction_add.checks_counter[on_reaction_add.locals[i-1][1]+3]) == 3) or (abs(on_reaction_add.checks_counter[7])==3) or  (abs(on_reaction_add.checks_counter[6]) == 3):
                await reaction.message.channel.send(v + " WON!")
                on_reaction_add.won = True
                await reset()
                return  

            if on_reaction_add.j == 9: #If no wins are found for both x and o, then it is a tie!
                await reaction.message.channel.send("TIE!")
                on_reaction_add.won = True
                await reset()
                return


on_message.repeat=True
on_message.won=False
on_message.gamestatus_ttt = False
on_reaction_add.j = 0
on_reaction_add.checks_counter = [0,0,0,0,0,0,0,0]
on_reaction_add.locals = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2]}
w = 0
on_message.userID = []

client.run(token)
