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
    if message.author == client.user:
        return
    if message.content.startswith("/TTT"):
        if len(userID) < 2:
            userID.append(message.author.name)
        if len(userID) == 2:
            if on[0] == False:
                on[0] = True
                tic = discord.Embed(colour=discord.Colour.red())

                # val =""
                # for i in range (3):
                #     for k in range(3):
                #         val+= arr[i][k] + " | "
                # val+="\n"

                on_message.emarr = [
                    [   ":white_large_square:",
                        ":white_large_square:",
                        ":white_large_square:",
                    ],
                    [
                        ":white_large_square:",
                        ":white_large_square:",
                        ":white_large_square:",
                    ],
                    [
                        ":white_large_square:",
                        ":white_large_square:",
                        ":white_large_square:",
                    ],
                ]
                tic.add_field(
                    name=("{} vs. {}".format(str(userID[0]), str(userID[1]))),
                    value=on_message.emarr[0][0]
                    + " | "
                    + on_message.emarr[0][1]
                    + " | "
                    + on_message.emarr[0][2]
                    + "\n \n"
                    + on_message.emarr[1][0]
                    + " | "
                    + on_message.emarr[1][1]
                    + " | "
                    + on_message.emarr[1][2]
                    + "\n \n"
                    + on_message.emarr[2][0]
                    + " | "
                    + on_message.emarr[2][1]
                    + " | "
                    + on_message.emarr[2][2],
                )
                msg = await message.channel.send(embed=tic)
                on_message.em = msg
                for i in range(2, 11):
                    await msg.add_reaction(client.emojis[i])

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return
    print(on_reaction_add.j)
    on_reaction_add.j += 1
    for i in range(2, 11):
        if reaction.emoji == client.emojis[i]:
            if on_reaction_add.j % 2 == 0:
                if user.name==userID[0]:
                    v = ":x:"
                else:
                    on_reaction_add.j-=1
                    return
            else:
                if user.name==userID[1]:
                    v = ":o:"
                else:
                    on_reaction_add.j-=1
                    return
            print(user.name)
            
            if i == 2:
                if on_message.emarr[0][0] ==":white_large_square:":
                    on_message.emarr[0][0] = v
                    new = discord.Embed()
                    new.add_field(
                        name=("{} vs. {}".format(str(userID[0]), str(userID[1]))),
                        value=on_message.emarr[0][0]
                        + " | "
                        + on_message.emarr[0][1]
                        + " | "
                        + on_message.emarr[0][2]
                        + "\n \n"
                        + on_message.emarr[1][0]
                        + " | "
                        + on_message.emarr[1][1]
                        + " | "
                        + on_message.emarr[1][2]
                        + "\n \n"
                        + on_message.emarr[2][0]
                        + " | "
                        + on_message.emarr[2][1]
                        + " | "
                        + on_message.emarr[2][2],
                    )
                    await on_message.em.edit(embed=new)
            elif i == 3:
                if on_message.emarr[0][1] ==":white_large_square:":
                    on_message.emarr[0][1] = v
                    new = discord.Embed()
                    new.add_field(
                        name=("{} vs. {}".format(str(userID[0]), str(userID[1]))),
                        value=on_message.emarr[0][0]
                        + " | "
                        + on_message.emarr[0][1]
                        + " | "
                        + on_message.emarr[0][2]
                        + "\n \n"
                        + on_message.emarr[1][0]
                        + " | "
                        + on_message.emarr[1][1]
                        + " | "
                        + on_message.emarr[1][2]
                        + "\n \n"
                        + on_message.emarr[2][0]
                        + " | "
                        + on_message.emarr[2][1]
                        + " | "
                        + on_message.emarr[2][2],
                    )
                    await on_message.em.edit(embed=new)
            elif i == 4:
                if on_message.emarr[0][2] ==":white_large_square:":
                    on_message.emarr[0][2] = v
                    new = discord.Embed()
                    new.add_field(
                        name=("{} vs. {}".format(str(userID[0]), str(userID[1]))),
                        value=on_message.emarr[0][0]
                        + " | "
                        + on_message.emarr[0][1]
                        + " | "
                        + on_message.emarr[0][2]
                        + "\n \n"
                        + on_message.emarr[1][0]
                        + " | "
                        + on_message.emarr[1][1]
                        + " | "
                        + on_message.emarr[1][2]
                        + "\n \n"
                        + on_message.emarr[2][0]
                        + " | "
                        + on_message.emarr[2][1]
                        + " | "
                        + on_message.emarr[2][2],
                    )
                    await on_message.em.edit(embed=new)
            elif i == 5:
                if on_message.emarr[1][0] ==":white_large_square:":
                    on_message.emarr[1][0] = v
                    new = discord.Embed()
                    new.add_field(
                        name=("{} vs. {}".format(str(userID[0]), str(userID[1]))),
                        value=on_message.emarr[0][0]
                        + " | "
                        + on_message.emarr[0][1]
                        + " | "
                        + on_message.emarr[0][2]
                        + "\n \n"
                        + on_message.emarr[1][0]
                        + " | "
                        + on_message.emarr[1][1]
                        + " | "
                        + on_message.emarr[1][2]
                        + "\n \n"
                        + on_message.emarr[2][0]
                        + " | "
                        + on_message.emarr[2][1]
                        + " | "
                        + on_message.emarr[2][2],
                    )
                    await on_message.em.edit(embed=new)
            elif i == 6:
                if on_message.emarr[1][1] ==":white_large_square:":
                    on_message.emarr[1][1] = v
                    new = discord.Embed()
                    new.add_field(
                        name=("{} vs. {}".format(str(userID[0]), str(userID[1]))),
                        value=on_message.emarr[0][0]
                        + " | "
                        + on_message.emarr[0][1]
                        + " | "
                        + on_message.emarr[0][2]
                        + "\n \n"
                        + on_message.emarr[1][0]
                        + " | "
                        + on_message.emarr[1][1]
                        + " | "
                        + on_message.emarr[1][2]
                        + "\n \n"
                        + on_message.emarr[2][0]
                        + " | "
                        + on_message.emarr[2][1]
                        + " | "
                        + on_message.emarr[2][2],
                    )
                    await on_message.em.edit(embed=new)
            elif i == 7:
                if on_message.emarr[1][2] ==":white_large_square:":
                    on_message.emarr[1][2] = v
                    new = discord.Embed()
                    new.add_field(
                        name=("{} vs. {}".format(str(userID[0]), str(userID[1]))),
                        value=on_message.emarr[0][0]
                        + " | "
                        + on_message.emarr[0][1]
                        + " | "
                        + on_message.emarr[0][2]
                        + "\n \n"
                        + on_message.emarr[1][0]
                        + " | "
                        + on_message.emarr[1][1]
                        + " | "
                        + on_message.emarr[1][2]
                        + "\n \n"
                        + on_message.emarr[2][0]
                        + " | "
                        + on_message.emarr[2][1]
                        + " | "
                        + on_message.emarr[2][2],
                    )
                    await on_message.em.edit(embed=new)
            elif i == 8:
                if on_message.emarr[2][0] ==":white_large_square:":
                    on_message.emarr[2][0] = v
                    new = discord.Embed()
                    new.add_field(
                        name=("{} vs. {}".format(str(userID[0]), str(userID[1]))),
                        value=on_message.emarr[0][0]
                        + " | "
                        + on_message.emarr[0][1]
                        + " | "
                        + on_message.emarr[0][2]
                        + "\n \n"
                        + on_message.emarr[1][0]
                        + " | "
                        + on_message.emarr[1][1]
                        + " | "
                        + on_message.emarr[1][2]
                        + "\n \n"
                        + on_message.emarr[2][0]
                        + " | "
                        + on_message.emarr[2][1]
                        + " | "
                        + on_message.emarr[2][2],
                    )
                    await on_message.em.edit(embed=new)
            elif i == 9:
                if on_message.emarr[2][1] ==":white_large_square:":
                    on_message.emarr[2][1] = v
                    new = discord.Embed()
                    new.add_field(
                        name=("{} vs. {}".format(str(userID[0]), str(userID[1]))),
                        value=on_message.emarr[0][0]
                        + " | "
                        + on_message.emarr[0][1]
                        + " | "
                        + on_message.emarr[0][2]
                        + "\n \n"
                        + on_message.emarr[1][0]
                        + " | "
                        + on_message.emarr[1][1]
                        + " | "
                        + on_message.emarr[1][2]
                        + "\n \n"
                        + on_message.emarr[2][0]
                        + " | "
                        + on_message.emarr[2][1]
                        + " | "
                        + on_message.emarr[2][2],
                    )
                    await on_message.em.edit(embed=new)
            else:
                if on_message.emarr[2][2] ==":white_large_square:":
                    on_message.emarr[2][2] = v
                    new = discord.Embed()
                    new.add_field(
                        name=("{} vs. {}".format(str(userID[0]), str(userID[1]))),
                        value=on_message.emarr[0][0]
                        + " | "
                        + on_message.emarr[0][1]
                        + " | "
                        + on_message.emarr[0][2]
                        + "\n \n"
                        + on_message.emarr[1][0]
                        + " | "
                        + on_message.emarr[1][1]
                        + " | "
                        + on_message.emarr[1][2]
                        + "\n \n"
                        + on_message.emarr[2][0]
                        + " | "
                        + on_message.emarr[2][1]
                        + " | "
                        + on_message.emarr[2][2],
                    )
                    await on_message.em.edit(embed=new)
on_reaction_add.j = -1


client.run(token)
