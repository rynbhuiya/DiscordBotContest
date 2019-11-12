import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import discord.embeds
import discord.colour

# Hidden Token from the environment variables file
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix="/")


@client.event
async def on_ready():
    print("Bot is online.")

userID = []
run = []
on = [False]


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("/TTT"):
        if len(userID) < 2:
            userID.append(message.author.name)
        if len(userID) == 2:
            if on[0] == False:
                on[0] = True
                tic = discord.Embed(title="{} vs. {}".format(
                    str(userID[0])+"  :x:", str(userID[1])+"  :o:"), colour=discord.Colour.red())

                on_message.emarr = [[], [], []]
                for i in range(3):
                    for j in range(3):
                        on_message.emarr[i].append(":white_large_square:")

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
                    if temp != ":white_large_square:":
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
