import discord
import discord.embeds
import asyncio

running = False #is gameRunning

async def start(channel,num,client):
    global running
    if(running):
        channel.send("The number game is already running!")
        return
    if not num.isdigit() or int(num) <5 or int(num) >50:
        channel.send("There must be a goal value between 5 and 50 \n TRY: !MBG ng <goal number here> ")
        return
    goal = int(num)
    running = True
    game_display = discord.Embed().add_field(name = "Number Game", value = "Goal: "+ str(goal) + "\nAt: 1")
    msg = await channel.send(embed=game_display)
    await msg.add_reaction('⏫')
    await runGame(channel,client,goal,1,msg)

async def runGame(channel,client,goal,current,msg):
    global running
    def check(reaction,user):
        if(user == client.user):
            return False
        return str(reaction.emoji) == '⏫' and reaction.message.id == msg.id
    while(running):
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=7.5, check=check)
        except asyncio.TimeoutError:
            channel.send("Number game stopped due to inactivity")
            running = False
            return
        else:
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=1, check=check)
            except asyncio.TimeoutError:
                current += 1
                game_display = discord.Embed().add_field(name = "Number Game", value = "Goal: "+ str(goal) + "\nAt: " + str(current))
                await msg.edit(embed=game_display)
                if(current>=goal):
                    channel.send("You Won.")
                    running = False
                    return
            else:
                channel.send("You Lost.")
                running = False
                return