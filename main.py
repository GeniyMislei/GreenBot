import disnake
from disnake.ext import commands
import os

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, test_guilds=[1250863812936990881])
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot started!")

@bot.command()
async def test(ctx):
    await ctx.send("test")


for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

bot.run("Ты правда думаешь что я солью токен своего бота? Нет бро ты ошибаешься.")