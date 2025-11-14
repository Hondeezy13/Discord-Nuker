import discord
from discord.ext import commands

# ---------- INTENTS ----------
intents = discord.Intents.default()
intents.message_content = True     
intents.guilds = True

# Bot Token Here
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = "INSERT TOKEN HERE"  # <-- Replace this with your bot token


# Bot Login
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


# Test Command To Verify Bot Is Ready
@bot.command()
async def ping(ctx):
    await ctx.send("pong")


# Nuking Channels
@bot.command()
@commands.has_permissions(administrator=True)
async def resetchannels(ctx, *, name: str):
    """
    Deletes all channels and creates 10 new channels named NAME.
    Usage: !resetchannels newname
    """
    guild = ctx.guild
    await ctx.send(f"Resetting channels to '{name}'...")

    for channel in guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f"Could not delete {channel.name}: {e}")

    for i in range(30):
        await guild.create_text_channel(f"{name}-{i+1}")

    print("Channel reset complete.")

bot.run(TOKEN)
