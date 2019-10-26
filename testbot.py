import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'Hello there':
            await message.channel.send('General Kenobi')

client = MyClient()
client.run('NjMwNTg1MTI3MDA4ODYyMjA4.XbSkOw.GO-rY6fixBPrywp-hkaKtNtZqRY')