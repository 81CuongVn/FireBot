import discord
from discord.ext import commands
import asyncpg

class AdminCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if isinstance(message.channel, discord.channel.DMChannel) or message.author.bot: return
        channel = message.channel
        if channel.id == 833089755709308988:
            messages = await channel.history(limit=10).flatten()
            for message1 in messages:
                if message1.author.bot and message.author.id == message1.mentions[0].id:
                    await message1.delete()
                    return

            if messages[1].author.bot:
                num = 1
            else:
                num = int(messages[1].content)+1
            if messages[1].author == message.author:
                await channel.send(f"{message.author.mention}, Bruh don't say twice in a row. Give someone else a chance as well. Now we have to start over... From 0 we go.")
                return
            try:
                if int(message.content) != num:
                    await channel.send(f"{message.author.mention}, You just had to do it! Now we have to start over... From 0 we go.")
            except:
                await channel.send(f"{message.author.mention}, You just had to do it! Now we have to start over... From 0 we go.")

        elif channel.id == 833090029193658378:
            messages = await channel.history(limit=10).flatten()
            for message1 in messages:
                if message1.author.bot and message.author.id == message1.mentions[0].id:
                    await message.delete()
                    return

            if len(message.content.split(" ")) > 1:
                await channel.send(f"{message.author.mention}, Bruh how hard is it to only type one word... Okay we are starting a new story, Let me start,\n\nThe")
            elif messages[1].author == message.author:
                await channel.send(f"{message.author.mention}, Bruh don't say a word two times in a row... Okay we are starting a new story, Let me start,\n\nThe")
            elif message.content.lower() not in open("cogs/wordlist.txt", 'r').read().lower().splitlines():
                await channel.send(f"{message.author.mention}, I don't think that's a real word... Okay we are starting a new story, Let me start,\n\nThe")

def setup(client):
    client.add_cog(AdminCommands(client))