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
async def reset_ttt():
    on_message_ttt.repeat=True
    on_message_ttt.won=False
    on_message_ttt.gamestatus_ttt = False
    on_reaction_add_ttt.j = 0
    w = 0
    on_message_ttt.userID = []

async def on_message_ttt(message): #On message 
    if message.author == client.user:
        return
    if message.content.startswith(".ttt"): #Text to start the game. Game starts with two members typing '.ttt'
        if on_message_ttt.gamestatus_ttt == True: # Check to see if a game is already on
            await message.channel.send('Game in Progress')
            return
        if len(on_message_ttt.userID) < 2: #until two people type .ttt
            on_message_ttt.userID.append(message.author.name)
        if len(on_message_ttt.userID) == 2: #Once there are two people ready to play
            # if on_message_ttt.userID[0]==on_message_ttt.userID[1]: # Checks if the same person typed the message and resets conditions
            #     await message.channel.send('Cannot be the same person')
            #     await reset_ttt()
            #     return
            on_message_ttt.gamestatus_ttt = True
            tic = discord.Embed(title="{} vs. {}".format(
                str(on_message_ttt.userID[0])+"  :x:", str(on_message_ttt.userID[1])+"  :o:"), colour=discord.Colour.red())
            on_message_ttt.board = [":one:", ":two:", ":three:", ":four:",":five:", ":six:", ":seven:", ":eight:", ":nine:"] #emojis for game board 
            on_message_ttt.emarr = [[], [], []]

            b = 0 #Putting the emojis into a 3 x 3 matrix
            while b < 9:
                for i in range(3):
                    for j in range(3):
                        on_message_ttt.emarr[i].append(on_message_ttt.board[b]) 
                        b += 1
            # making a text board of the emojis seperated by | for the embed
            val = ""
            for i in range(3):
                val += " | "
                for k in range(3):
                    val += on_message_ttt.emarr[i][k] + " | "
                val += "\n \n"

            tic.add_field(
                name=("Your turn:  ❌ \n"),
                value=val # The game board made above for the embed 
            )
            msg = await message.channel.send(embed=tic)
            on_message_ttt.em = msg # Used to check if we are on the correct game message
            for i in range(2, 11):
                await msg.add_reaction(client.emojis[i]) # Showing the reactions that are buttons to control the board
    on_message_ttt.moves=on_reaction_add_ttt.j
    await asyncio.sleep(30)            # turn off the game and reset
    if on_message_ttt.gamestatus_ttt == True and on_message_ttt.em.id != message.id and on_message_ttt.moves==on_reaction_add_ttt.j:
        await reset_ttt()
        await message.channel.send("TicTacToe game stopped due to inactivity")

#Function variables for on_message_ttt
on_message_ttt.userID = [] 
on_message_ttt.gamestatus_ttt = False

async def on_reaction_add_ttt(reaction, user):
    if on_message_ttt.gamestatus_ttt == False:
        return
    if on_message_ttt.em.id != reaction.message.id:
        return
    if user == client.user:
        return
    # moves=on_reaction_add_ttt.j
    # await asyncio.sleep(30)            # turn off the game and reset
    # if on_message_ttt.gamestatus_ttt == True and on_message_ttt.em.id != reaction.id and moves==on_reaction_add_ttt.j:
    #     await reset_ttt()
    #     await reaction.channel.send("TicTacToe game stopped due to inactivity")
    count = 0
    for i in range(2, 11):
        if reaction.emoji == client.emojis[i]: #Checks what reaction emoji was clicked
            if on_reaction_add_ttt.j % 2 == 0: #Checks what turn we are on
                if user.name == on_message_ttt.userID[0]:  #If we are on the first user
                    on_reaction_add_ttt.j += 1
                    v = ":x:"
                    t = ":o:"
                else:
                    return
            else:
                if user.name == on_message_ttt.userID[1]: #If we are on the second user
                    on_reaction_add_ttt.j += 1
                    v = ":o:"
                    t = ":x:"

                else:
                    return
            for m in range(2, 11): #Finds the loction of the corresponding reaction emoji on the numbered board and stores it in temp
                if i == m:
                    if (m-1) % 3 == 0: #Checks if the reaction emoji clicked is a multiple of three
                        temp = on_message_ttt.emarr[int((m-1)/3-1)][int(m % 3+1)]
                    else:
                        temp = on_message_ttt.emarr[int((m-1)/3)][(int(m-1) % 3)-1]
                    if (temp not in on_message_ttt.board):
                        on_reaction_add_ttt.j -= 1
                        return
                    else: # Changes the desired emoji on the desired number emoji of the board with an x or o depending on the turn 
                        if (m-1) % 3 == 0:
                            on_message_ttt.emarr[int((m-1)/3-1)][int(m % 3+1)] = v 
                        else:
                            on_message_ttt.emarr[int((m-1)/3)][(int(m-1) % 3)-1] = v
                        # Remake val with for the updated emebed board
                        val = ""
                        for l in range(3):
                            val += " | "
                            for k in range(3):
                                val += on_message_ttt.emarr[l][k] + " | "
                            val += "\n \n"
                        new = discord.Embed(title="{} vs. {}".format(
                            str(on_message_ttt.userID[0])+"  :x:", str(on_message_ttt.userID[1])+"  :o:"), colour=discord.Colour.red())
                        new.add_field(
                            name=("Your turn: " + t + "\n"), value=val) # Changes to next user
                        await on_message_ttt.em.edit(embed=new) #send new edited embed to same message 
            # Checks win every time and sees if there is any pattern of three x's or o's in a line
            for w in range(2):
                if w == 0: #Checks the code with x first and then o second time.
                    emoji1 = ":x:"
                else:
                    emoji1 = ":o:"
                for r in range(3): #Checks row
                    for c in range(3):
                        if on_message_ttt.emarr[r][c] == emoji1:
                            count += 1
                    if count < 3:
                        count = 0
                    else:
                        await reaction.message.channel.send(emoji1 + " WON!")
                        on_reaction_add_ttt.won = True
                        await reset_ttt()
                        return
                for c in range(3): #Checks Column
                    for r in range(3):
                        if on_message_ttt.emarr[r][c] == emoji1:
                            count += 1
                    if count < 3:
                        count = 0
                    else:
                        await reaction.message.channel.send(emoji1 + " WON!")
                        on_reaction_add_ttt.won = True
                        await reset_ttt()
                        return
                for r in range(3): #Checks Diagonal - upper left to bottom right
                    if on_message_ttt.emarr[r][r] == emoji1:
                        count += 1
                if count < 3:
                    count = 0
                else:
                    await reaction.message.channel.send(emoji1 + " WON!")
                    on_reaction_add_ttt.won = True
                    await reset_ttt()
                    return

                for r in range(3): #Checks Diagnoal upper right to bottom left
                    r2 = 2
                    if on_message_ttt.emarr[r2-r][r2-r] == emoji1:
                        count += 1
                if count < 3:
                    count = 0
                else:
                    await reaction.message.channel.send(emoji1 + " WON!")
                    on_reaction_add_ttt.won = True
                    await reset_ttt()
                    return
                if on_reaction_add_ttt.j == 9: #If no wins are found for both x and o, then it is a tie!
                    await reaction.message.channel.send("TIE!")
                    on_reaction_add_ttt.won = True
                    await reset_ttt()
                    return
on_reaction_add_ttt.j = 0
on_reaction_add_ttt.won = False

client.run(token)
