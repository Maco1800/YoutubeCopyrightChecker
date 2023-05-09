import discord
from discord.ext import commands

channel_id = 1104008065335967784

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    if message.channel.id == channel_id and message.attachments and message.attachments[0].filename.endswith('.mp4'):
        attachment = message.attachments[0]
        filename = attachment.filename
        await attachment.save(fp=filename)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')


# Start the Discord bot
bot.run('')