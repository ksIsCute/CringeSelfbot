import discord, asyncio, random
from discord.ext import commands

prefix = input("What do you want your prefix to be?\n")
token = input("What is your token?\n")

bot = commands.Bot(command_prefix=prefix, self_bot=True, case_insensitive=True)

def cringe(ctx):
  while True:
    await ctx.send(random.choice(cringeness))
    await asyncio.sleep(randint(1,120)

@bot.command(aliases=["on","enab","cringeon","online","turnon"])
async def enable(ctx):
  await ctx.send("**:gear: | Enabling the cringe machine..**") 
  cringe = True

@bot.command(aliases=["off", "shutdown", "d", "quit", "stop"])
async def disable(ctx):
  await ctx.send("**:gears: | Disabling the cringe machine..**")
  cringe = False

bot.run(token, bot=False)
