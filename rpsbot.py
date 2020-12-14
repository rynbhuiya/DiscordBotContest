import discord
import discord.reaction
import discord.embeds
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
import os
client = commands.Bot(command_prefix = '.') # Change the command prefix

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def rps(ctx):
    await ctx.channel.send('Rock Paper Scissors')



rlist = []
rlist.append(None)
rlist.append(None)

@client.event
async def on_message(message):
    if (message.content[0:4] == '.rps'):

        if on_message.gamestatus == True:
            await message.channel.send('Game in Progress')
            return
        if len(message.mentions) != 1:
            return 

        if message.mentions[0].bot == True:
            return 
        
        on_reaction_add.ulist.append(message.mentions[0])
        on_reaction_add.ulist.append(message.author)

        # on_reaction_add.ulist[0] = message.mentions[0]
        # on_reaction_add.ulist[1] = message.author

        embed = discord.Embed()
        embed.add_field(name = 'Rock, Paper, Scissors!\n'+ on_reaction_add.ulist[0].name + ' vs. ' + on_reaction_add.ulist[1].name, value ='Enter on Go!')
        on_message.m = await message.channel.send(embed = embed)
        await on_message.m.add_reaction('✂')
        await on_message.m.add_reaction('📰')
        await on_message.m.add_reaction('⛰')
        
        await asyncio.sleep(0.5)

        for i in range(3):
            await asyncio.sleep(1)
            embed = discord.Embed()
            embed.add_field(name = 'Rock, Paper, Scissors!\n'+ on_reaction_add.ulist[0].name + ' vs. ' + on_reaction_add.ulist[1].name, value = str(3 - i))

            await on_message.m.edit(embed = embed)
        
        await asyncio.sleep(1)
        embed = discord.Embed()
        embed.add_field(name = 'Rock, Paper, Scissors!\n'+ on_reaction_add.ulist[0].name + ' vs. ' + on_reaction_add.ulist[1].name, value = 'Go!')

        await on_message.m.edit(embed = embed)

        on_message.gamestatus = True
        await asyncio.sleep(5)

        if rlist[0] == None and rlist[1] == None and on_message.gamestatus == True:
            await message.channel.send('Neither players gave an input') 
            rlist[0] = None
            rlist[1] = None
            on_reaction_add.ulist = []
            on_message.gamestatus = False
            on_reaction_add.check = False
            on_reaction_add.react = False
            on_reaction_add.timer = False

on_message.gamestatus = False



@client.event
async def on_reaction_add(reaction, user):
    if on_message.m.id != reaction.message.id:
        return
    if on_message.gamestatus == False:
        return
    if user == client.user:
        return

    if on_reaction_add.ulist[0] == user:
        rlist[0] = reaction.emoji
    elif on_reaction_add.ulist[1] == user:
        rlist[1] = reaction.emoji
        
    #rlist.append(reaction.emoji)
    await asyncio.sleep(2)
    
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
        
        

        await asyncio.sleep(6)
        on_reaction_add.ulist = []
        rlist[0] = None
        rlist[1] = None
        on_message.gamestatus = False
        on_reaction_add.check = False
        on_reaction_add.react = False
        on_reaction_add.timer = False
        return
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

# load_dotenv()
# client.run(os.getenv("DISCORD_TOKEN"))