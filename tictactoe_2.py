import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import discord.embeds
import discord.colour

# Hidden Token from the environment variables file
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix=".") # Change the command prefix

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


#Reset function for repeating games
async def reset():
    on_message.repeat=True
    on_message.won=False
    on_message.gamestatus_ttt = False
    on_reaction_add.j = 0
    w = 0
    on_message.userID  = []
    on_reaction_add.checks_counter = []

@client.event
async def on_message(message): #On message 
    if message.author == client.user: 
        return
    if message.content.startswith(".ttt"): #Text to start the game. Game starts with two members typing '.ttt'
        if on_message.gamestatus_ttt == True: # Check to see if a game is already on
            await message.channel.send('Game in Progress')
            return
        if len(on_message.userID  ) < 2: #until two people type .ttt
            on_message.userID.append(message.author.name)
        if len(on_message.userID) == 2: #Once there are two people ready to play
            # if on_message.userID[0]==on_message.userID[1]: # Checks if the same person typed the message and resets conditions
            #     await message.channel.send('Cannot be the same person')
            #     await reset()
            #     return
            on_message.gamestatus_ttt = True
            tic = discord.Embed(title="{} vs. {}".format(
                str(on_message.userID[0])+"  :x:", str(on_message.userID[1])+"  :o:"), colour=discord.Colour.red())
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
    if user == client.user:
        return
    count = 0


    for i in range(2, 11):
        if reaction.emoji == client.emojis[i]:
            if on_reaction_add.j % 2 == 0:
                if user.name == on_message.userID [0]:
                    on_reaction_add.j += 1
                    v = ":x:"
                    t = ":o:"
                else:
                    return
            else:
                if user.name == on_message.userID [1]:
                    on_reaction_add.j += 1
                    v = ":o:"
                    t = ":x:"
                else:
                    return
            if (i-1) % 3 == 0:
                temp = on_message.emarr[int((i-1)/3-1)][int(i % 3+1)]
            else:
                temp = on_message.emarr[int((i-1)/3)][(int(i-1) % 3)-1]
            if (temp not in on_message.board):
                on_reaction_add.j -= 1
                return
            else:
                if (i-1) % 3 == 0:
                    on_message.emarr[int((i-1)/3-1)][int(i % 3+1)] = v
                else:
                    on_message.emarr[int(
                        (i-1)/3)][(int(i-1) % 3)-1] = v
                val = ""
                for l in range(3):
                    val += " | "
                    for k in range(3):
                        val += on_message.emarr[l][k] + " | "
                    val += "\n \n"
                new = discord.Embed(title="{} vs. {}".format(
                    str(on_message.userID [0])+"  :x:", str(on_message.userID [1])+"  :o:"), colour=discord.Colour.red())
                new.add_field(
                    name=("Your turn: " + t + "\n"), value=val)
                await on_message.em.edit(embed=new)

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
w = 0
on_message.userID  = []
client.run(token)
