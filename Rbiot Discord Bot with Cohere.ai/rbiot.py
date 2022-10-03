# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 20:10:57 2022

@author: quort
"""

#import os
import discord
# import time
# import pandas as pd
from discord.ext import commands
from token_2 import TOKEN
from functions import classify

intents = discord.Intents.all()
intents.presences = True
intents.members = True
intents.typing = True

client = commands.Bot(command_prefix = "$", intents = intents)

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.event
async def on_presence_update(before, after):
    if after.status.name == 'online' and after.name == 'luckyjalien' and before.status.name != 'online' and str(after.guild) == 'boop' :
        channel = client.get_channel(864249486451802143)
        await channel.send('jackie is online!!')
        
    elif after.status.name == 'online' and after.name == 'nil' and before.status.name != 'online' and str(after.guild) == 'boop' :
        channel = client.get_channel(864249486451802143)
        await channel.send('jun is online!!')
    
    elif after.status.name == 'online' and after.name == 'raphraphraph' and before.status.name != 'online' and str(after.guild) == 'boop' :
        channel = client.get_channel(864249486451802143)
        await channel.send('raph is online!!')
        
@client.command()
async def ha(ctx):
    print(ctx.guild.name)
    print(ctx.guild.id)

@client.command()
async def likeness(ctx, *, arg):
    channel = ctx.channel
    await channel.send('Give me a second for the algorithm to do its thing...')
    name = classify(arg)
    await channel.send('This message is most like ' + str(name))
    
    


client.run(TOKEN)