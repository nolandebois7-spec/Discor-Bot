import discord
from discord.ext import commands
from datetime import datetime, timezone, timedelta
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_member_join(member):
    age = datetime.now(timezone.utc) - member.created_at
    if age < timedelta(days=15):
        await member.kick(reason="Account too new")

bot.run(os.environ["MTQ1ODE4ODg3MTMxMjYwNTM0NQ.GZL0VJ.cICLvmRzYXUYfCQ8u-E29O08VWdybkkbxACmXBg"])
