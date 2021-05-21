
import discord
import aiohttp
import json
import requests
from discord.ext.commands import Bot
from discord.ext import commands
clinet = commands.Bot(command_prefix = ".")
@clinet.event
async def on_ready():
    print("KM Codes")
@clinet.command()
async def w(ctx, arg1):
    async with aiohttp.ClientSession() as session:
        apiurl = f"http://api.weatherstack.com/current?access_key=82658b49a57b43e125c050225d48c55c&query={arg1}"
        r = requests.get(apiurl)
        print(r)
        print(r.text)
        kingman = json.loads(r.text)
        city = kingman['request']['query']
        localtime = kingman['current']['observation_time']
        wind_speed = kingman['current']['wind_speed']
        wind_degree = kingman['current']['wind_degree']
        temperature = kingman['current']['temperature']
        weather_icons = kingman['current']['weather_icons'][0]
        weather_descriptions = kingman['current']['weather_descriptions'][0]
        humidity = kingman['current']['humidity'] 
        print(city)
        print(localtime)
        print(wind_speed)
        print(wind_degree)
        print(temperature)
        print(weather_icons)
        print(weather_descriptions)
        print(humidity)
        embed=discord.Embed(title="درجة الحرارة", description=f"{temperature}", color=0x31364c)
        embed.set_author(name="Weather Bot By KM Codes", icon_url=f"{weather_icons}")
        embed.add_field(name="سرعة الرياح", value=f"{wind_speed}", inline=True)
        embed.add_field(name="درجة الرياح ", value=f"{wind_degree}", inline=True)
        embed.add_field(name="وصف الحالة الجوية ", value=f"{weather_descriptions}", inline=True)
        embed.add_field(name="معدل الرطوية ", value=f"{humidity}", inline=True)
        embed.set_footer(text=f"Time Now in this city is {localtime}")
        await ctx.send(embed=embed)
clinet.run("")
