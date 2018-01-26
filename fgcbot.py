#!/usr/python3

# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.

import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
from smashgg import *
from functions import *


# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Basic Bot by Habchy#1665", command_prefix="-fgc ", pm_help = False)



# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print('--------')
    print('Support Discord Server: https://discord.gg/FNNNgqb')
    print('Github Link: https://github.com/Habchy/BasicBot')
    print('--------')
    print('You are running BasicBot v2.1') #Do not change this. This will really help us support you, if you need support.
    print('Created by Habchy#1665')
    return await client.change_presence(game=discord.Game(name='-fgc info')) #This is buggy, let us know if it doesn't work.



# This is a basic example of a call and response command. You tell it do "this" and it does it.

# -fgc playerid gamertag ## need a list of gamertag-to-playerid
# -fgc <tournament> <game> results
# -fgc <tournament> <game> seed
# -fgc playerid stats  ##compile w/l for all tournaments/games/events/groups

@client.command()
async def info(*args):
    info_info = discordify(["Hello I am FGCBot.  I interface with websites like smash.gg to give you stats on your tournaments", "type '-fgc commands' for commands'"])
    info_github = discordify(["BasicBot: https://github.com/Habchy/BasicBot", "FGCBot: https://github.com/walkerboh8806/FGCBot"])
    messages = [info_info, info_github]
    await client.say(combine_discordify(messages))

@client.command()
async def commands():
    command_add = discordify(["add: add a tournament's raw data to database", "usage: -fgc add <tournament_name>"])
    command_list = discordify(["list: list things", "usage: -fgc list tournaments, -fgc list players"])
    messages = [command_add, command_list]
    await client.say(combine_discordify(messages))

@client.command()
async def list(*args):
    try:
        if args[0] == "tournaments":
            await client.say(list_tournaments())
        elif args[0] == "players":
            await client.say(discordify(["Still under development"]))
    except IndexError:
        await client.say(discordify(["usage: -fgc list tournaments, -fgc list players"]))


@client.command()
async def add(*args):
    try:
        #check = discordify([tournament_check(args[0])])
        add = tournament_add_raw(args[0])
        message = discordify(add)
        await client.say(message)
    except IndexError:
        await client.say(discordify(["usage: -fgc add <tournament_name>"]))
#async def tournament(*args):


#run the client
client.run('NDA2MzQ0MDM3MTIyMDQ4MDAy.DUxk6A.MN7828IEU9YL_lwOQQyc4cUsLC8')
