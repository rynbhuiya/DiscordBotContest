import discord
from discord.ext import commands
import discord.embeds
import asyncio

client = commands.Bot(command_prefix=".")

def reset():
    on_message.game_on = False      #reset all needed values to allow the game to be played again
    on_message.curr_num = 0         #not async so that game evalutations/prints aren't made as game resets
    on_message.curr_goal = 0        #avoids a small possibility of multiple evaluations
    on_reaction_add.reaction_counter = 0

@client.event
async def on_message(message):
    if message.author == client.user:   #don't check bot's msg's
        return
    if message.content[0:3] != ".NG":   #check if calling the number game
        return
    if on_message.game_on == True:                 #if number game already running don't start
        await message.channel.send("The number game is already running!")
        return   #if no goal paramter or incorrect goal paramter don't start
    if message.content[4:].isdigit() == False or int(message.content[4:]) < 5 or int(message.content[4:]) > 50:
        await message.channel.send("There must be a goal value between 5 and 50, TRY: .NG <goal number here> ")
        return
    on_message.curr_goal = int(message.content[4:])#the goal will be after .NG and a space
    on_message.game_on = True                      #update variable to true, game will be running soon 
    game_display = discord.Embed()
    game_display.add_field(name = "Number Game", value = "Goal: "+ str(on_message.curr_goal) + "\nAt: "+ str(on_message.curr_num) )
                                        #created and initalized embed instance to send in
    on_message.curr_msg = await message.channel.send(embed=game_display) #set a refrence to our message that will hold and display the game
    await on_message.curr_msg.add_reaction('⏫')
    c = on_message.curr_num                        # create temporary variables, if after 7.5s,
    m = on_message.curr_msg                        # the num does not change or a new game isn't started(msg would change)
    await asyncio.sleep(7.5)            # turn of the game and reset variables: only for if no initial reactions
    if c == on_message.curr_num and m.id == on_message.curr_msg.id and on_message.game_on == True:
        reset()                                                   # reset game, why it's not async explained in func
        await message.channel.send("Number game stopped due to inactivity")

@client.event
async def on_reaction_add(reaction,user):
    if user == client.user:             #ignore the bot's reactions
        return
    if on_message.game_on == False:     # don't worry about reactions if game is off
        return
    if reaction.message.id != on_message.curr_msg.id:    #only worry about reactnons pertaining to the msg that holds our game
        return
    if str(reaction.emoji) != '⏫':         #only worry about the increaser reaction
        return
    on_reaction_add.reaction_counter +=1
    await asyncio.sleep(1)             # increase counter by one sleep one second to wait for other entries
    if on_reaction_add.reaction_counter > 1 and on_message.game_on == True:  #if more than one person clicks in the ~1 second, result in a loss, and reset game
        reset()
        await reaction.message.channel.send("You Lost.")
        return
    elif on_reaction_add.reaction_counter == 1:         #only one person enetered increase curr_num by 1
        if on_message.curr_num+1 == on_message.curr_goal and on_message.game_on == True:
            reset()
            await reaction.message.channel.send("You Won.")         #win condition if the current num gets to the goal they win, reset after
            return
        await on_message.curr_msg.clear_reactions()
        on_message.curr_num += 1
        game_display = discord.Embed()
        game_display.add_field(name = "Number Game", value = "Goal: "+ str(on_message.curr_goal) + "\nAt: "+ str(on_message.curr_num) )
        await on_message.curr_msg.edit(embed = game_display)
        await on_message.curr_msg.add_reaction('⏫')     #create new embed, put in format from before with updated curent num and edit msg
        on_reaction_add.reaction_counter = 0 
    c = on_message.curr_num                        # create temporary variables, if after 7.5s,
    m = on_message.curr_msg                        # the num does not change or a new game isn't started(msg would change)
    await asyncio.sleep(7.5)            # turn off the game and reset
    if c == on_message.curr_num and m.id == on_message.curr_msg.id and on_message.game_on == True:
        reset()
        await reaction.message.channel.send("Number game stopped due to inactivity")


on_message.game_on = False  # if game is running or not
on_message.curr_num = 0     # current number game is at, 0 if game not running            #initiial values
on_message.curr_goal = 0    # current goal of the game
on_reaction_add.reaction_counter = 0    #number of reactions for this number

client.run('NjMwNTg1MTI3MDA4ODYyMjA4.XcpjTw.UEDYGSsnwwNUnL63hwUNYRfIF4A')

