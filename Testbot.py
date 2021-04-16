import discord
from discord.ext import commands
import datetime
import requests
import os

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('tula')

@bot.command()
async def suma(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def doge(ctx):
    url = "https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=CLP,USD,EUR"
    response = requests.get(url)
    await ctx.send(response.text)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="tula tula tula tula tula",
    timestamp=datetime.datetime.utcnow(),color=discord.Color.dark_red())
    embed.add_field(name="Fecha de creación del SV", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Creador del SV", value=f"{ctx.guild.owner}")
    await ctx.send(embed=embed)

#events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="eso",url="https://www.twitch.tv/girlofnox"))
    print('hola gente toi on')

bot.run('pQHA7anVygrfPnu1dT4h0mzWvMKycWp7')