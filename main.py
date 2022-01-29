import discord
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions ,MissingPermissions
import random
import os 
from keep_alive import keep_alive
import asyncio
from discord_components import DiscordComponents, ComponentsBot,Button,SelectOption,Select
        
client = commands.Bot(command_prefix = ">")
DiscordComponents(client)

owner = [759070461706371103,821790584829902879]
pig = [759070461706371103]

@client.event 
async def on_ready():
  print("ready")
  #DiscordComponents(client, change_discord_methods=True)

@client.command(aliases=["8ball","test","eight","ask"])
async def _8ball(ctx, *,question):
     responses = ["yes","no","maybe","possibly","idk","could be true","only god can tell","have to keep this one hidden ofc"]
     await ctx.send(f"question: {question}\nAnswer: {random.choice(responses)}")
colour=discord.Colour.purple()

@client.command()
async def gm(ctx):
  await ctx.send(f"morning {ctx.author.mention}")

@client.command()
async def welcome(ctx,member:discord.Member):
  await ctx.send(f"{member.mention} Congratulations on joining our team! \n wanna sub to piggie (Y/N)")
  def check(m):
    return m.author.id == ctx.author.id and m.channel == ctx.channel
  msg = await client.wait_for("message",timeout=12.0,check=check)
  if msg.content == "Y":
    await ctx.send("link is here https://youtube.com/c/Piggie1603")
  else:
    await ctx.send("ok i wont")

@client.command(aliases=["inspire"])
async def quote(ctx):
  inspire = ["The way i see it if you want the rainbow you gotta put up with the rain","Not how long, but how well you have lived is the main thing.","Life is not a problem to be solved, but a reality to be experienced.","Turn your wounds into wisdom.","Do all the good you can, for all the people you can, in all the ways you can, as long as you can."]
  await ctx.send(f"{ctx.author.mention} here is a inspiring quote: {random.choice(inspire)}")
"""
@client.command()
async def button(ctx):
    await ctx.send(type=InteractionType.ChannelMessageWithSource, content="why dont you drop a sub?", components=[Button(style=ButtonStyle.URL, label="here", url="https://www.youtube.com/c/Piggie1603"), Button(style=ButtonStyle.blue, label="Default Button", custom_id="button")])
"""
@client.command()
async def gn(ctx):
  await ctx.send(f"night night {ctx.author.mention} :yawning_face:")
  while True:
    await ctx.send("sniper is....")

@client.command()
async def timer(ctx, amt):
  amt = int(amt)
  await asyncio.sleep(amt)
  await ctx.send(f"{ctx.author.mention}Timer has ended!")
  await ctx.send("piggie#1603 suggested dis")

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx,member: discord.Member,*,reason=None):
  await member.ban(reason=reason)
  await ctx.send(f"user {member} has been banned by {ctx.author.mention} for {reason}")

@ban.error
async def kick_error(ctx,error):
 if isinstance(error, commands.MissingPermissions):
    await ctx.send("hey idiot ur no got permssions")

@client.command(aliases = ["bday"])
async def happybirthday(ctx, member: discord.Member):
  await ctx.send(f"happy birthday {member.mention}")


@client.command()
async def hug(ctx, member: discord.Member):
  await ctx.send(f"{ctx.author.mention} hugged {member.mention}")


@client.command()
async def club(ctx):
  #club = "here are club stats"
  await ctx.send(f"https://brawlify.com/stats/club/2Y88R2QC9")

@client.command()
async def diceroll(ctx):
   if ctx.author.id in owner:
     await ctx.send("you rolled max number 100")
     return 
   dice = random.randint(1,100)
   if dice is 100:
    await ctx.send("wow u rolled 100 max number omg omg pro")
   else:
    await ctx.send(f"{ctx.author.mention} rolled {dice}")

@client.command()
async def howgay(ctx, member: discord.Member = None):
  gay = random.randint(0,100)
  if ctx.author.id in owner:
    await ctx.send("this user is not gay")
  else:
   await ctx.send(f"this user is {gay}% gay")


@client.command()
async def slap(ctx, member: discord.Member = None):
  if member.id in owner:
    await ctx.send("this user is to powerful to be slapped you got slapped back OOF")
  if member:
    await ctx.send(f"{ctx.author.mention} slapped {member.mention} OOF")
  else:
    await ctx.send("well u gonna slap urslef u idiot\nmention someone u make me angry man\n back in my day we fought tigers to get to school you have it easy")

words = ["right i told you","brawl stars is cool","rip timbo","bye bye sniper we will miss you","swayswayandbudu","piggie","1 year awakening","ars will be missed","mod server mod","power league","bufebfuebfeygfeygfyegfyeg","spike","come on you thought this was ez hahaha ehfeufhuef"]

@client.command()
async def play(ctx):
  words_msg = await ctx.send(f"{random.choice(words)}")
  await asyncio.sleep(0.3) # wait 7 seconds - import asyncio module if not already imported
  await words_msg.delete() # delete the message
  await ctx.send("copy what you saw")
  def check(m):
    return m.author.id == ctx.author.id and m.channel == ctx.channel
  oof = await client.wait_for("message",timeout=12.0, check=check)
  if oof.content in words:
    await ctx.send(f"{ctx.author.mention} you passed the game well done")
  else:
   await ctx.send(f"{ctx.author.mention} you failed big sad")
truth = ["What is the last lie you told?","When was the last time you cleaned up your room?","Have you ever broken something in the house and blamed a sibling?","What was your most embarrassing moment?","What is the funniest thing you have ever seen?"]
dare = ["tell the 3rd person in ur dms u love them then close the dm","give 10% of your dank coins to someone not an alt","go in a server and get banned","swear at someone in a server ping as well :joy:","drop your phone wherever you are","lose a simulate"]

@client.command(aliases = ["TOD","tod"])
async def truthordare(ctx):
  await ctx.send("__rules__\n1.play with someone\n2,for a dare send ss after\n3.say simulate if you dont wnna do it you can only use 3 times use it wisely\n4. dont abuse truth\ntruth or dare")
  def check(m):
    return m.author.id == ctx.author.id and m.channel == ctx.channel
  poz = await client.wait_for("message",timeout=12.0,check=check)
  if poz.content == "dare":
    await ctx.send(f"{random.choice(dare)}")
  else:
      await ctx.send(f"{random.choice(truth)}")

@client.command()
async def hello(ctx):
    await ctx.send("hello", components = [
        [Button(label="Hi", style="3", emoji = "🥴", custom_id="button1"), Button(label="Bye", style="4", emoji = "😔", custom_id="button2")]
        ])
    interaction = await client.wait_for("button_click", check = lambda i: i.custom_id == "button1")
    await interaction.send(content = "Button clicked!", ephemeral=False)
keep_alive()
client.run(os.getenv("TOKEN"))

