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

userID = []


def reset():
    on_message.gamestatus_ttt = False
    on_reaction_add.j = 0
    w = 0
    userID = []


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(".ttt"):
        if on_message.gamestatus_ttt == True:
            await message.channel.send('Game in Progress')
            return
        if len(userID) < 2:
            userID.append(message.author.name)
        if len(userID) == 2:
            if on_message.gamestatus_ttt == False:
                on_message.gamestatus_ttt = True
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

on_message.gamestatus_ttt = False


@client.event
async def on_reaction_add(reaction, user):
    if on_message.em.id != reaction.message.id:
        return
    count = 0
    if user == client.user:
        return
    print(on_reaction_add.won)
    if on_reaction_add.won == False:
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
                            temp = on_message.emarr[int(
                                (m-1)/3-1)][int(m % 3+1)]
                        else:
                            temp = on_message.emarr[int(
                                (m-1)/3)][(int(m-1) % 3)-1]
                        if (temp not in on_message.board):
                            on_reaction_add.j -= 1
                            return
                        else:
                            if (m-1) % 3 == 0:
                                on_message.emarr[int(
                                    (m-1)/3-1)][int(m % 3+1)] = v
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
                            on_reaction_add.won = True
                            reset()
                            return
                    for c in range(3):
                        for r in range(3):
                            if on_message.emarr[r][c] == emoji1:
                                count += 1
                        if count < 3:
                            count = 0
                        else:
                            await reaction.message.channel.send(emoji1 + " WON!")
                            on_reaction_add.won = True
                            reset()
                            return
                    for r in range(3):
                        if on_message.emarr[r][r] == emoji1:
                            count += 1
                    if count < 3:
                        count = 0
                    else:
                        await reaction.message.channel.send(emoji1 + " WON!")
                        on_reaction_add.won = True
                        reset()
                        return

                    for r in range(3):
                        r2 = 2
                        if on_message.emarr[r2-r][r2-r] == emoji1:
                            count += 1
                    if count < 3:
                        count = 0
                    else:
                        await reaction.message.channel.send(emoji1 + " WON!")
                        on_reaction_add.won = True
                        reset()
                        return
                    if on_reaction_add.j == 9:
                        await reaction.message.channel.send("TIE!")
                        on_reaction_add.won = True
                        reset()
                        return

on_reaction_add.j = 0
on_reaction_add.won = False

client.run(token)
