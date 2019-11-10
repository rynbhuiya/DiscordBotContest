import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.content == 'HOWDY':
            await message.channel.send('H A W Y E E')


client = MyClient()
client.run('NjMwNTg1MTI3MDA4ODYyMjA4.XbSgiA.Cg7Z3Oa7BohiyKqd0U0abjV9ac8')
