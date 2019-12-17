import discord
from discord.ext import commands
import discord.embeds
import asyncio
import os
from dotenv import load_dotenv

# Hidden Token from the environment variables file
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

def reset():
    on_message_ng.game_on = False      #reset all needed values to allow the game to be played again
    on_message_ng.curr_num = 0         #not async so that game evalutations/prints aren't made as game resets
    on_message_ng.curr_goal = 0        #avoids a small possibility of multiple evaluations
    on_reaction_add_ng.reaction_counter = 0


async def on_message_ng(message):
    if message.author == client.user:   #don't check bot's msg's
        return
    if message.content[0:3] != ".NG":   #check if calling the number game
        return
    if on_message_ng.game_on == True:                 #if number game already running don't start
        await message.channel.send("The number game is already running!")
        return   #if no goal paramter or incorrect goal paramter don't start
    if message.content[4:].isdigit() == False or int(message.content[4:]) < 5 or int(message.content[4:]) > 50:
        await message.channel.send("There must be a goal value between 5 and 50, TRY: .NG <goal number here> ")
        return
    on_message_ng.curr_goal = int(message.content[4:])#the goal will be after .NG and a space
    on_message_ng.game_on = True                      #update variable to true, game will be running soon 
    game_display = discord.Embed()
    game_display.add_field(name = "Number Game", value = "Goal: "+ str(on_message_ng.curr_goal) + "\nAt: "+ str(on_message_ng.curr_num) )
                                        #created and initalized embed instance to send in
    on_message_ng.curr_msg = await message.channel.send(embed=game_display) #set a refrence to our message that will hold and display the game
    await on_message_ng.curr_msg.add_reaction('⏫')
    c = on_message_ng.curr_num                        # create temporary variables, if after 7.5s,
    m = on_message_ng.curr_msg                        # the num does not change or a new game isn't started(msg would change)
    await asyncio.sleep(7.5)            # turn of the game and reset variables: only for if no initial reactions
    if c == on_message_ng.curr_num and m.id == on_message_ng.curr_msg.id and on_message_ng.game_on == True:
        reset()                                                   # reset game, why it's not async explained in func
        await message.channel.send("Number game stopped due to inactivity")


async def on_reaction_add_ng(reaction,user):
    if user == client.user:             #ignore the bot's reactions
        return
    if on_message_ng.game_on == False:     # don't worry about reactions if game is off
        return
    if reaction.message.id != on_message_ng.curr_msg.id:    #only worry about reactnons pertaining to the msg that holds our game
        return
    if str(reaction.emoji) != '⏫':         #only worry about the increaser reaction
        return
    on_reaction_add_ng.reaction_counter +=1
    await asyncio.sleep(1)             # increase counter by one sleep one second to wait for other entries
    if on_reaction_add_ng.reaction_counter > 1 and on_message_ng.game_on == True:  #if more than one person clicks in the ~1 second, result in a loss, and reset game
        reset()
        await reaction.message.channel.send("You Lost.")
        return
    elif on_reaction_add_ng.reaction_counter == 1:         #only one person enetered increase curr_num by 1
        if on_message_ng.curr_num+1 == on_message_ng.curr_goal and on_message_ng.game_on == True:
            reset()
            await reaction.message.channel.send("You Won.")         #win condition if the current num gets to the goal they win, reset after
            return
        await on_message_ng.curr_msg.clear_reactions()
        on_message_ng.curr_num += 1
        game_display = discord.Embed()
        game_display.add_field(name = "Number Game", value = "Goal: "+ str(on_message_ng.curr_goal) + "\nAt: "+ str(on_message_ng.curr_num) )
        await on_message_ng.curr_msg.edit(embed = game_display)
        await on_message_ng.curr_msg.add_reaction('⏫')     #create new embed, put in format from before with updated curent num and edit msg
        on_reaction_add_ng.reaction_counter = 0 
    c = on_message_ng.curr_num                        # create temporary variables, if after 7.5s,
    m = on_message_ng.curr_msg                        # the num does not change or a new game isn't started(msg would change)
    await asyncio.sleep(7.5)            # turn off the game and reset
    if c == on_message_ng.curr_num and m.id == on_message_ng.curr_msg.id and on_message_ng.game_on == True:
        reset()
        await reaction.message.channel.send("Number game stopped due to inactivity")


on_message_ng.game_on = False  # if game is running or not
on_message_ng.curr_num = 0     # current number game is at, 0 if game not running            #initiial values
on_message_ng.curr_goal = 0    # current goal of the game
on_reaction_add_ng.reaction_counter = 0    #number of reactions for this number



############################RPSRPSRPSRPSRPSRPSRPS#####################
rlist = []

rlist.append(None)

rlist.append(None)




async def on_message_rps(message):

    if (message.content[0:4] == '.rps'):



        if on_message_rps.gamestatus == True:

            await message.channel.send('Game in Progress')

            return

        if len(message.mentions) != 1:

            return 



        if message.mentions[0].bot == True:

            return 

        

        on_reaction_add_rps.ulist.append(message.mentions[0])

        on_reaction_add_rps.ulist.append(message.author)



        # on_reaction_add_rps.ulist[0] = message.mentions[0]

        # on_reaction_add_rps.ulist[1] = message.author



        embed = discord.Embed()

        embed.add_field(name = 'Rock, Paper, Scissors!\n'+ on_reaction_add_rps.ulist[0].name + ' vs. ' + on_reaction_add_rps.ulist[1].name, value ='Enter on Go!')

        on_message_rps.m = await message.channel.send(embed = embed)

        await on_message_rps.m.add_reaction('✂')

        await on_message_rps.m.add_reaction('📰')

        await on_message_rps.m.add_reaction('⛰')

        

        await asyncio.sleep(0.5)



        for i in range(3):

            await asyncio.sleep(1)

            embed = discord.Embed()

            embed.add_field(name = 'Rock, Paper, Scissors!\n'+ on_reaction_add_rps.ulist[0].name + ' vs. ' + on_reaction_add_rps.ulist[1].name, value = str(3 - i))



            await on_message_rps.m.edit(embed = embed)

        

        await asyncio.sleep(1)

        embed = discord.Embed()

        embed.add_field(name = 'Rock, Paper, Scissors!\n'+ on_reaction_add_rps.ulist[0].name + ' vs. ' + on_reaction_add_rps.ulist[1].name, value = 'Go!')



        await on_message_rps.m.edit(embed = embed)



        on_message_rps.gamestatus = True

        await asyncio.sleep(5)



        if rlist[0] == None and rlist[1] == None and on_message_rps.gamestatus == True:

            await message.channel.send('Neither players gave an input') 

            rlist[0] = None

            rlist[1] = None

            on_reaction_add_rps.ulist = []

            on_message_rps.gamestatus = False

            on_reaction_add_rps.check = False

            on_reaction_add_rps.react = False

            on_reaction_add_rps.timer = False



on_message_rps.gamestatus = False









async def on_reaction_add_rps(reaction, user):

    if on_message_rps.m.id != reaction.message.id:

        return

    if on_message_rps.gamestatus == False:

        return

    if user == client.user:

        return



    if on_reaction_add_rps.ulist[0] == user:

        rlist[0] = reaction.emoji

    elif on_reaction_add_rps.ulist[1] == user:

        rlist[1] = reaction.emoji

        

    #rlist.append(reaction.emoji)

    await asyncio.sleep(2)

    

    on_reaction_add_rps.timer = True

    if (on_reaction_add_rps.react == False):

        on_reaction_add_rps.react = True

        

        if rlist[0] == None:

            await reaction.message.channel.send(on_reaction_add_rps.ulist[0].name + ' did not input on time')

        elif rlist[1] == None:

            await reaction.message.channel.send(on_reaction_add_rps.ulist[1].name + ' did not input on time')

        else:

            await reaction.message.channel.send(str(rlist[0]) + ' : ' + str(rlist[1]))

            on_reaction_add_rps.check = True



        



    # Check for win condition

    if on_reaction_add_rps.check:

        if rlist[0] == rlist[1]:

            await reaction.message.channel.send('Tie!')

        elif (str(rlist[0]) == '✂' and str(rlist[1]) == '📰'):

            await reaction.message.channel.send(on_reaction_add_rps.ulist[0].name + ' has won!')

        elif (str(rlist[0]) == '📰' and str(rlist[1]) == '⛰'):

            await reaction.message.channel.send(on_reaction_add_rps.ulist[0].name + ' has won!')

        elif (str(rlist[0]) == '⛰' and str(rlist[1]) == '✂'):

            await reaction.message.channel.send(on_reaction_add_rps.ulist[0].name + ' has won!')

        

        elif (str(rlist[1]) == '✂' and str(rlist[0]) == '📰'):

            await reaction.message.channel.send(on_reaction_add_rps.ulist[1].name + ' has won!')

        elif (str(rlist[1]) == '📰' and str(rlist[0]) == '⛰'):

            await reaction.message.channel.send(on_reaction_add_rps.ulist[1].name + ' has won!')

        elif (str(rlist[1]) == '⛰' and str(rlist[0]) == '✂'):

            await reaction.message.channel.send(on_reaction_add_rps.ulist[1].name + ' has won!')

        

        



        await asyncio.sleep(6)

        on_reaction_add_rps.ulist = []

        rlist[0] = None

        rlist[1] = None

        on_message_rps.gamestatus = False

        on_reaction_add_rps.check = False

        on_reaction_add_rps.react = False

        on_reaction_add_rps.timer = False

        return

        # on_reaction_add_rps.ulist[0] = None

        # on_reaction_add_rps.ulist[1] = None

# @client.event

# async def on_reaction_add_rps(reaction, user):

#     await reaction.message.channel.send('Duplicate')

on_reaction_add_rps.ulist = []

# on_reaction_add_rps.ulist.append(None)

# on_reaction_add_rps.ulist.append(None)

on_reaction_add_rps.check = False

on_reaction_add_rps.react = False

on_reaction_add_rps.timer = False

on_message_rps.m = 0

##########################################################TTTTTTTTTTTTTTTTTTTTTTTTT######################

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
            if on_message_ttt.userID[0]==on_message_ttt.userID[1]: # Checks if the same person typed the message and resets conditions
                await message.channel.send('Cannot be the same person')
                await reset_ttt()
                return
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


on_message_ng.curr_msg = None
on_message_rps.m = None
on_message_ttt.em = None
@client.event
async def on_message(message):
    if message.author == client.user:   #don't check bot's msg's
        return
    if message.content[0:3] == ".NG":   #check if calling the number game
        await on_message_ng(message)
    if message.content[0:4] == ".rps":   #check if calling the number game
        await on_message_rps(message)
    if message.content[0:4] == ".ttt":   #check if calling the number game
        await on_message_ttt(message)

@client.event
async def on_reaction_add(reaction,user):
    if user == client.user:             #ignore the bot's reactions
        return
    if on_message_ng.curr_msg != None and reaction.message.id == on_message_ng.curr_msg.id:    #only worry about reactnons pertaining to the msg that holds our game
        await on_reaction_add_ng(reaction,user)
    if on_message_rps.m != None and on_message_rps.m.id == reaction.message.id:
        await on_reaction_add_rps(reaction,user)
    if on_message_ttt.em != None and on_message_ttt.em.id == reaction.message.id:
        await on_reaction_add_ttt(reaction,user)

client.run(token)