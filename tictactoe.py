import discord
import discord.embeds
import asyncio

running = False


async def start(channel, author, client):
    global running
    users = []
    emarr = [[], [], []]
    emojis = {"{}\N{COMBINING ENCLOSING KEYCAP}".format(num):num for num in range(1, 10)}

    users.append(author)

    if(running):
        await channel.send('A TicTacToe game is already running!')
        return
        
    running = True
    
    def check(m):
        return m.content=='!MGB ttt' and m.channel==channel
    
    try:
        msg= await client.wait_for('message', timeout=15, check=check)
    except asyncio.TimeoutError:
        await channel.send("TTT game stopped due to inactivity")
        running = False
        return
    else:
        users.append(msg.author)
 
        if users[0].id == users[1].id:
            await channel.send('Cannot be the same person')
            return

        tic = discord.Embed(title="{} vs. {}".format(
        str(users[0].name)+"  :x:", str(users[1].name)+"  :o:"), colour=discord.Colour.red())
        board = [":one:", ":two:", ":three:", ":four:",":five:", ":six:", ":seven:", ":eight:", ":nine:"] #emojis for game board 

        b = 0 #Putting the emojis into a 3 x 3 matrix
        while b < 9:
            for i in range(3):
                for j in range(3):
                    emarr[i].append(board[b]) 
                    b += 1
        # making a text board of the emojis seperated by | for the embed
        val = ""
        for i in range(3):
            val += " | "
            for k in range(3):
                val += emarr[i][k] + " | "
            val += "\n \n"

        tic.add_field(name=("Your turn:  ❌ \n"),value=val) # The game board made above for the embed
        msg = await channel.send(embed=tic)
        
        for i in range(9):
            await msg.add_reaction(list(emojis.keys())[i]) # Showing the reactions that are buttons to control the board

        await runGame(channel, client, users, emojis, board, emarr, msg)

async def runGame(channel, client, users, emojis, board, emarr, msg):
    global running
    checks_counter = [0,0,0,0,0,0,0,0]
    location = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2]}
    turns=0

    def check(reaction,user):
        if user==client.user:
            return False
        return str(reaction.emoji) in list(emojis.keys()) and reaction.message.id == msg.id

    while (running):
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=30, check=check)
        except asyncio.TimeoutError:
            await channel.send("TTT game stopped due to inactivity")
            running = False
            return
        else:
            idx=emojis[reaction.emoji]
            if turns % 2 == 0: #Checks what turn we are on
                if user.id == users[0].id:  #If we are on the first user
                    turns += 1
                    v = ":x:"
                    t = ":o:"
                else:
                    continue
            else:
                if user.id == users[1].id: #If we are on the second user
                    turns += 1
                    v = ":o:"
                    t = ":x:"
                else:
                    continue

            if (emarr[location[idx][0]][location[idx][1]] not in board):
                turns -= 1
                continue
            else:
                emarr[location[idx][0]][location[idx][1]]=v

            # Remake val with for the updated emebed board
            val = ""
            for l in range(3):
                val += " | "
                for k in range(3):
                    val += emarr[l][k] + " | "
                val += "\n \n"
            new = discord.Embed(title="{} vs. {}".format(
            str(users[0].name)+"  :x:", str(users[1].name)+"  :o:"), colour=discord.Colour.red())
            new.add_field(
                name=("Your turn: " + t + "\n"), value=val) # Changes to next user
            await msg.edit(embed=new) #send new edited embed to same message 

            # Check the input and the corresponding rows, columns, and/or diagonals to see if a three X's or O's
            if v==":x:":
                add_val = 1
            else:
                add_val = -1

            checks_counter[location[idx][0]]+=add_val
            checks_counter[location[idx][1]+3]+=add_val

            if location[idx][0] == location[idx][1]:
                checks_counter[6]+=add_val
                    
            if (location[idx][0] + location[idx][1] == 2):
                checks_counter[7]+=add_val

            if (abs(checks_counter[location[idx][0]]) == 3) or (abs(checks_counter[location[idx][1]+3]) == 3) or (abs(checks_counter[7])==3) or  (abs(checks_counter[6]) == 3):
                await reaction.message.channel.send(v + " WON!")
                running = False
                return  

            if turns== 9: #If no wins are found for both x and o, then it is a tie!
                await reaction.message.channel.send("TIE!")
                running = False
                return