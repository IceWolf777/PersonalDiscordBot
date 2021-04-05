﻿import discord
import json
import random
import os

from discord.ext import commands

Keys = { 
    "clientID" : "825455539399557181",
    "publicKey" : "9198975fb26be78918e25d31e4efdbf1e6f7d4defc83a9d2de191fbe92bd4f52",
    "botToken" : "ODI1NDU1NTM5Mzk5NTU3MTgx.YF-LYA.dfYIofb-fVLbcBMUb22CE3EU_LM",
    "redirect-URL" : "https://www.swtor.com/"
    }

client = commands.Bot(command_prefix='!')
#currentGuild = discord.Guild()
#client = discord.Client()

def readFileJSON():
    if ("discordKeys.json"):
        file = open("discordKeys.json", "r")

def getDiscordUsers():
    guildSize = len(client.users)
    usersList = {}
    print(guildSize)
    for i in client.users:
        usersList[client.users] = client.users[i]
    f = open("users.json", "w")
    f.write(json.dumps(usersList, sort_keys=True))
    f.close()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #getDiscordUsers()

@client.event
async def on_message(ctx):
    if ctx.author == client.user:
        return

    if ctx.content.startswith('!') == False:
        if ctx.content.find("hello") != -1:
            await ctx.channel.send('Hello!')
    await client.process_commands(ctx)

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommmandNotFound):
		await ctx.send('Invalid command')

#COMMAND: hello, will respond with 'world' 
@client.command()
async def hello(ctx):
    """Send text message 'world'"""
    await ctx.send("world")
    return

#COMMAND: knight, will respond with a phrase and knight the user
@client.command()
async def knight(ctx):
    knightString = "By the power granted to me it is the will of the Force, that I Knight you young " + str(ctx.author) + ". Now arise as a new child of the light. You will be the shield that guards innocents against those who would wish to cause harm."
    await ctx.send(knightString)

#COMMAND: happy, will respond with the slight_smile emoji
@client.command()
async def happy(ctx):
    """Send :slight_smile: Emoji"""
    await ctx.send(":slight_smile:")
    return

#COMMAND: dice, will send value found by random generation
@client.command()
async def dice(ctx, arg):
    """Roll Dice(.dice help to see options"""
    dice_result=0
    if arg == "help":
        await ctx.send("!dice <dicetype>")
        await ctx.send("dicetype: d4, d6, d8, d10, d12, d20")
        return
    #d4 roll
    if arg == "d4":
        dice_result = random.randint(1,4)
    #d6 roll
    if arg == "d6":
        dice_result = random.randint(1,6)
    #d8 roll
    if arg == "d8":
        dice_result = random.randint(1,8)
    #d10 roll
    if arg == "d10":
        dice_result = random.randint(1,10)
    #d12 roll
    if arg == "d12":
        dice_result = random.randint(1,12)
    #d20 roll
    if arg == "d20":
        dice_result = random.randint(1,20)
    await ctx.send(dice_result)
    return

#COMMAND: boomerang, will repeat the argument if an argument is sent by the user
@client.command()
async def boomerang(ctx, *, arg):
    if arg:
        await ctx.send(arg)
    return

client.run(discordKeys["botToken"])