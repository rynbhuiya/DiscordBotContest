import discord
import discord.reaction
import discord.embeds
import asyncio
from discord.ext import commands
import os
from dotenv import load_dotenv
import discord.colour

# Hidden Token from the environment variables file
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix = '.') # Change the command prefix

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Rock Paper Scissor 
@client.command()
async def rps(ctx):
    await ctx.channel.send('Rock Paper Scissors')

rlist = []
rlist.append(None)
rlist.append(None)

@client.event
async def on_message(message):
    if (message.content[0:4] == '.rps'):

        #Checks to see if there is a game in progress
        if on_message.gamestatus == True:
            await message.channel.send('Game in Progress')
            return
        #Checks to see if there are 2 players
        if len(message.mentions) != 1:
            return 
        # Bot doesn't know how to play rock paper scissors
        if message.mentions[0].bot == True:
            return 
        
        # Adds the players into the user list
        on_reaction_add.ulist.append(message.mentions[0])
        on_reaction_add.ulist.append(message.author)

        # on_reaction_add.ulist[0] = message.mentions[0]
        # on_reaction_add.ulist[1] = message.author

        # Outputs the rps embed
        embed = discord.Embed()
        embed.add_field(name = 'Rock, Paper, Scissors!\n'+ on_reaction_add.ulist[0].name + ' vs. ' + on_reaction_add.ulist[1].name, value ='Enter on Go!')
        on_message.m = await message.channel.send(embed = embed)
        await on_message.m.add_reaction('✂')
        await on_message.m.add_reaction('📰')
        await on_message.m.add_reaction('⛰')
        
        await asyncio.sleep(0.5)

        # Countdown timer for the rps embed
        for i in range(3):
            await asyncio.sleep(1)
            embed = discord.Embed()
            embed.add_field(name = 'Rock, Paper, Scissors!\n'+ on_reaction_add.ulist[0].name + ' vs. ' + on_reaction_add.ulist[1].name, value = str(3 - i))

            await on_message.m.edit(embed = embed)
        
        await asyncio.sleep(1)
        embed = discord.Embed()
        embed.add_field(name = 'Rock, Paper, Scissors!\n'+ on_reaction_add.ulist[0].name + ' vs. ' + on_reaction_add.ulist[1].name, value = 'Go!')

        await on_message.m.edit(embed = embed)

        # Changes gamestatus to true so that other players can't initiate more games when current players are inputting
        on_message.gamestatus = True
        await asyncio.sleep(5)

        # Checks to see if the game is going on and whether both players gave an input
        # Resets the various checks
        if rlist[0] == None and rlist[1] == None and on_message.gamestatus == True:
            await message.channel.send('Neither players gave an input') 
            rlist[0] = None
            rlist[1] = None
            on_reaction_add.ulist = []
            on_message.gamestatus = False
            on_reaction_add.check = False
            on_reaction_add.react = False
            on_reaction_add.timer = False

# Gamestatus var delcaration
on_message.gamestatus = False


# Outputs the winner of the rps game
@client.event
async def on_reaction_add(reaction, user):
    # Checks to see that the reaction is that of the player
    if on_message.m.id != reaction.message.id:
        return
    # If the the game is over then return
    if on_message.gamestatus == False:
        return
    if user == client.user:
        return

    # Adds the reactions to a list based on the ulist
    if on_reaction_add.ulist[0] == user:
        rlist[0] = reaction.emoji
    elif on_reaction_add.ulist[1] == user:
        rlist[1] = reaction.emoji
        
    #rlist.append(reaction.emoji)
    await asyncio.sleep(2)
    
    # Checks to see if the players inputted
    on_reaction_add.timer = True
    if (on_reaction_add.react == False):
        on_reaction_add.react = True
        
        if rlist[0] == None:
            await reaction.message.channel.send(on_reaction_add.ulist[0].name + ' did not input on time')
        elif rlist[1] == None:
            await reaction.message.channel.send(on_reaction_add.ulist[1].name + ' did not input on time')
        else:
            await reaction.message.channel.send(str(rlist[0]) + ' : ' + str(rlist[1]))
            on_reaction_add.check = True

        

    # Check for win condition
    if on_reaction_add.check:
        if rlist[0] == rlist[1]:
            await reaction.message.channel.send('Tie!')
        elif (str(rlist[0]) == '✂' and str(rlist[1]) == '📰'):
            await reaction.message.channel.send(on_reaction_add.ulist[0].name + ' has won!')
        elif (str(rlist[0]) == '📰' and str(rlist[1]) == '⛰'):
            await reaction.message.channel.send(on_reaction_add.ulist[0].name + ' has won!')
        elif (str(rlist[0]) == '⛰' and str(rlist[1]) == '✂'):
            await reaction.message.channel.send(on_reaction_add.ulist[0].name + ' has won!')
        
        elif (str(rlist[1]) == '✂' and str(rlist[0]) == '📰'):
            await reaction.message.channel.send(on_reaction_add.ulist[1].name + ' has won!')
        elif (str(rlist[1]) == '📰' and str(rlist[0]) == '⛰'):
            await reaction.message.channel.send(on_reaction_add.ulist[1].name + ' has won!')
        elif (str(rlist[1]) == '⛰' and str(rlist[0]) == '✂'):
            await reaction.message.channel.send(on_reaction_add.ulist[1].name + ' has won!')
        
        
        # Resets all the variables
        await asyncio.sleep(6)
        on_reaction_add.ulist = []
        rlist[0] = None
        rlist[1] = None
        on_message.gamestatus = False
        on_reaction_add.check = False
        on_reaction_add.react = False
        on_reaction_add.timer = False
        return

    on_message.gamestatus = False
    
        # on_reaction_add.ulist[0] = None
        # on_reaction_add.ulist[1] = None

# @client.event
# async def on_reaction_add(reaction, user):
#     await reaction.message.channel.send('Duplicate')
on_reaction_add.ulist = []
# on_reaction_add.ulist.append(None)
# on_reaction_add.ulist.append(None)
on_reaction_add.check = False
on_reaction_add.react = False
on_reaction_add.timer = False
on_message.m = 0


# Tic-tac-toe
userID = []
run = []
on = [False]


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(".ttt"):
        if len(userID) < 2:
            userID.append(message.author.name)
        if len(userID) == 2:
            if on[0] == False:
                on[0] = True
                tic = discord.Embed(title="{} vs. {}".format(
                    str(userID[0])+"  :x:", str(userID[1])+"  :o:"), colour=discord.Colour.red())
                on_message.board = [":one:", ":two:", ":three:", ":four:",
                                    ":five:", ":six:", ":seven:", ":eight:", ":nine:"]
                on_message.emarr = [[], [], []]
                b = 0
                while b < 9:
                    for i in range(3):
                        for j in range(3):
                            on_message.emarr[i].append(on_message.board[b])
                            b += 1

                val = ""
                for i in range(3):
                    val += " | "
                    for k in range(3):
                        val += on_message.emarr[i][k] + " | "
                    val += "\n \n"
                tic.add_field(
                    name=("Your turn:  ❌ \n"),
                    value=val
                )
                msg = await message.channel.send(embed=tic)
                on_message.em = msg
                for i in range(2, 11):
                    await msg.add_reaction(client.emojis[i])


@client.event
async def on_reaction_add(reaction, user):
    if on_message.em.id != reaction.message.id:
        return
    count = 0
    if user == client.user:
        return

    for i in range(2, 11):
        if reaction.emoji == client.emojis[i]:
            if on_reaction_add.j % 2 == 0:
                if user.name == userID[0]:
                    on_reaction_add.j += 1
                    v = ":x:"
                    t = ":o:"
                else:
                    return
            else:
                if user.name == userID[1]:
                    on_reaction_add.j += 1
                    v = ":o:"
                    t = ":x:"
                else:
                    return
            for m in range(2, 11):
                if i == m:
                    if (m-1) % 3 == 0:
                        temp = on_message.emarr[int((m-1)/3-1)][int(m % 3+1)]
                    else:
                        temp = on_message.emarr[int((m-1)/3)][(int(m-1) % 3)-1]
                    if (temp not in on_message.board):
                        on_reaction_add.j -= 1
                        return
                    else:
                        if (m-1) % 3 == 0:
                            on_message.emarr[int((m-1)/3-1)][int(m % 3+1)] = v
                        else:
                            on_message.emarr[int(
                                (m-1)/3)][(int(m-1) % 3)-1] = v
                        val = ""
                        for l in range(3):
                            val += " | "
                            for k in range(3):
                                val += on_message.emarr[l][k] + " | "
                            val += "\n \n"
                        new = discord.Embed(title="{} vs. {}".format(
                            str(userID[0])+"  :x:", str(userID[1])+"  :o:"), colour=discord.Colour.red())
                        new.add_field(
                            name=("Your turn: " + t + "\n"), value=val)
                        await on_message.em.edit(embed=new)

            for w in range(2):
                if w == 0:
                    emoji1 = ":x:"
                else:
                    emoji1 = ":o:"
                for r in range(3):
                    for c in range(3):
                        if on_message.emarr[r][c] == emoji1:
                            count += 1
                    if count < 3:
                        count = 0
                    else:
                        await reaction.message.channel.send(emoji1 + " WON!")
                        return
                for c in range(3):
                    for r in range(3):
                        if on_message.emarr[r][c] == emoji1:
                            count += 1
                    if count < 3:
                        count = 0
                    else:
                        await reaction.message.channel.send(emoji1 + " WON!")
                        return
                for r in range(3):
                    if on_message.emarr[r][r] == emoji1:
                        count += 1
                if count < 3:
                    count = 0
                else:
                    await reaction.message.channel.send(emoji1 + " WON!")
                    return

                for r in range(3):
                    r2 = 2
                    if on_message.emarr[r2-r][r2-r] == emoji1:
                        count += 1
                if count < 3:
                    count = 0
                else:
                    await reaction.message.channel.send(emoji1 + " WON!")
                    return
                if on_reaction_add.j == 9:
                    await reaction.message.channel.send("TIE!")
                    return

on_reaction_add.j = 0

client.run(token)