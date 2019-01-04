import discord, logging, json, asyncio, time, random, aiohttp, re, datetime, traceback, os, sys, math, asyncpg
from time import gmtime
from discord.ext import commands

#-------------------DATA---------------------
version = "0.2.12"
owner = ["361534796830081024"]
alowner = ["469150536399323157", "270102554334068747"]
bot = commands.Bot(command_prefix='-', description=None)
bot.remove_command("help")
PRserver = "Lyedlik Újság"
underworking = ":warning: **Nem, ez még nincs kész...** :warning:"
"""timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())"""

#-----------------SETUP----------------------
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="Igen."))

class NoPermError(Exception):
    pass

#------------------MOD-----------------------
@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user : discord.User=None, Day : int=None, *, Reason=None):
    if user is None:
        await bot.reply("**Használat: `-ban {member} {0 - 7 napok, üzenetek törléséhez} {Indoklás}` köcce.**")
    elif Reason is None:
        await bot.reply("**Használat: `-ban {member} {0 - 7 napok, üzenetek törléséhez} {Indoklás}` köcce.**")
    elif Day is None:
        await bot.reply("**Használat: `-ban {member} {0 - 7 napok, üzenetek törléséhez} {Indoklás}` köcce.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**Nem fogom engedni, hogy saját magad bannold :P**")
        else:
            room = ctx.message.channel
            await bot.ban(user, delete_message_days=Day)
            LogRoom = bot.get_channel(id="530825108651114498")
            await bot.say(f"**{ctx.message.author.mention} Bannolta {user.mention}-t. Indoklás: __{Reason}__\nLásd a logokban itt: {LogRoom.mention}**")
            em = discord.Embed(title="BAN", description=None, colour=0xad1457)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {PRserver}`\nBAMM!! A Banhammer lecsapott rád, csaó!**")

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unban(ctx, user : discord.User=None, *, Reason=None):
    if user is None:
        await bot.reply("**Használat: `-unban {member} {Indoklás}` köcce.**")
    elif Reason is None:
        await bot.reply("**Használat: `-unban {member} {Indoklás}` köcce.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**Nem fogom engedni, hogy saját magad bannold :P**")
        else:
            banneds_list = await bot.get_bans(ctx.message.server)
            if user not in banneds_list:
                bot.say("**A megadott felhasználó nincs a bannoltak listájában!**")
            else:
                room = ctx.message.channel
                await bot.unban(ctx.message.server, user)
                LogRoom = bot.get_channel(id="530825108651114498")
                await bot.say(f"**{ctx.message.author.mention} Unbannolta {user.mention}-t. Indoklás: __{Reason}__\nLásd a logokban itt: {LogRoom.mention}**")
                em = discord.Embed(title="UNBAN", description=None, colour=0xe91e63)
                em.add_field(name="User", value=f"{user.mention}")
                em.add_field(name="Moderator", value=f"{ctx.message.author}")
                em.add_field(name="Reason", value=f"{Reason}")
                em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
                timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
                em.set_footer(text=timer)
                await bot.send_message(LogRoom, embed=em)
                Private = await bot.start_private_message(user)
                await bot.send_message(Private, f"**`Server: {PRserver}`\nHello! Unbannoltak téged a {PRserver} discord szerverről, Szeretnél visszajönni? \nhttps://discord.gg/VGqQ76V**")

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user : discord.User=None, *, Reason=None):
    if user is None:
        await bot.reply("**Használat: `-kick {member} {Indoklás}` köcce.**")
    elif Reason is None:
        await bot.reply("**Használat: `-kick {member} {Indoklás}` köcce.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**Nem fogom engedni, hogy saját magad bannold :P**")
        else:
            room = ctx.message.channel
            await bot.kick(user)
            LogRoom = bot.get_channel(id="530825108651114498")
            await bot.say(f"**{ctx.message.author.mention} Kickelte {user.mention}-t. Indoklás: __{Reason}__\nLásd a logokban itt: {LogRoom.mention}**")
            em = discord.Embed(title="KICK", description=None, colour=0xe74c3c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {PRserver}`\nHello! Kirúgtak a {PRserver} szerverről, viszlát!**")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def mute(ctx, user : discord.User=None, duration : int=None, *, Reason=None):
    if user is None:
        await bot.reply("**Használat: `-mute {member} {Időtartam (s)} {Indoklás}` köcce.**")
    elif Reason is None:
        await bot.reply("**Használat: `-mute {member} {Időtartam (s)} {Indoklás}` köcce.**")
    elif duration is None:
        await bot.reply("**Használat: `-mute {member} {Időtartam (s)} {Indoklás}` köcce.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**Nem fogom engedni, hogy saját magad bannold :P**")
        else:
            LogRoom = bot.get_channel(id="530825108651114498")
            room = ctx.message.channel
            MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
            await bot.add_roles(user, MutedRole)
            await bot.say(f"**{ctx.message.author.mention} Muttolta {user.mention}-t {duration} másodpercre. Indoklás: __{Reason}__\nLásd a logokban itt: {LogRoom.mention}**")
            em = discord.Embed(title="MUTE", description=None, colour=0x11806a)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.add_field(name="Duration", value=f"{duration} sec")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {PRserver}`\nHello! Egy {duration} másodperces MUTE appeard. Seems OP, pls nerf.**")
            await asyncio.sleep(duration)
            await bot.remove_roles(user, MutedRole)
            em = discord.Embed(title="UNMUTE", description=None, colour=0x1abc9c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value="Lejárt a megadott időtartam...")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {PRserver}`\nHello! Unmuttoltak a szerveren, de ne izgasd fel magad túlságosan...**")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, user : discord.User=None, *, Reason=None):
    if user is None:
        await bot.reply("**Használat: `-unmute {member} {Indoklás}` köcce.**")
    elif Reason is None:
        await bot.reply("**Használat: `-unmute {member} {Indoklás}` köcce.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**Nem fogom engedni, hogy saját magad bannold :P**")
        else:
            LogRoom = bot.get_channel(id="530825108651114498")
            room = ctx.message.channel
            MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
            await bot.remove_roles(user, MutedRole)
            await bot.say(f"**{ctx.message.author.mention} Unmuttolta {user.mention}-t (he he). Indoklás: __{Reason}__\nLásd a logokban itt: {LogRoom.mention}**")
            em = discord.Embed(title="UNMUTE", description=None, colour=0x1abc9c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {PRserver}`\nHello! Unmuttoltak a szerveren, de ne izgasd fel magad túlságosan...**")

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def lock(ctx, duration : int=None, *, Reason=None):
    if Reason is None:
        await bot.reply("**Használat: `-lock {member} {Időtartam (s)} {Indoklás}` köcce.**")
    elif duration is None:
        await bot.reply("**Használat: `-lock {member} {Időtartam (s)} {Indoklás}` köcce.**")
    else:
        Tag = discord.utils.get(ctx.message.server.roles, name="Tag")
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        await bot.edit_channel_permissions(ctx.message.channel, Tag, overwrite)
        await bot.send_message(ctx.message.channel, f"**{ctx.message.author} lezárta a {ctx.message.channel.mention} szobát. Indoklás: __{Reason}__**")
        LogRoom = bot.get_channel(id="530825108651114498")
        em = discord.Embed(title="LOCK", description=None, colour=0x1f8b4c)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.add_field(name="Duration", value=f"{duration} sec")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)
        await asyncio.sleep(duration)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        await bot.edit_channel_permissions(ctx.message.channel, Tag, overwrite)
        await bot.send_message(ctx.message.channel, f"**{ctx.message.author} feloldotta a {ctx.message.channel.mention} szobát. Indoklás: __{Reason}__**")
        LogRoom = bot.get_channel(id="401752340366884885")
        em = discord.Embed(title="UNLOCK", description=None, colour=0x2ecc71)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, *, Reason=None):
    if Reason is None:
        await bot.reply("**Használat: `-unlock {Indoklás}` köcce.**")
    else:
        Registered = discord.utils.get(ctx.message.server.roles, name="Tag")
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        await bot.edit_channel_permissions(ctx.message.channel, Tag, overwrite)
        await bot.send_message(ctx.message.channel, f"**{ctx.message.author} lezárta a {ctx.message.channel.mention} szobát. Indoklás: __{Reason}__**")
        LogRoom = bot.get_channel(id="401752340366884885")
        em = discord.Embed(title="UNLOCK", description=None, colour=0x2ecc71)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)
    
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number : int=None):
    if number is None:
        await bot.reply("**Használat: `-clear {üzenetek száma}` köcce.**")
    else:
        number += 1
        deleted = await bot.purge_from(ctx.message.channel, limit=number)
        num = number - 1
        LogRoom = bot.get_channel(id="401752340366884885")
        em = discord.Embed(title=None, description=f'{ctx.message.author} törölt __{num}__ üzenetet', colour=0x3498db)
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        msg = await bot.send_message(ctx.message.channel, embed=em)
        await bot.send_message(LogRoom, embed=em)
        await asyncio.sleep(4)
        await bot.delete_message(msg)

@bot.command(pass_context=True)
async def create_adminrole(ctx, *, name=None):
    if ctx.message.author.id in owner:
        role = await bot.create_role(ctx.message.server)
        await bot.edit_role(ctx.message.server, role, name=name, permission="discord.Permissions.administrator", hoist=False, mentionable=False)
        await bot.move_role(ctx.message.server, role, 9)
        await bot.add_roles(ctx.message.author, role)
        await bot.reply("**Kész!**")
    else:
        await bot.reply("**No u**")

@bot.command(pass_context=True)
async def create_role(ctx, position : int=None, *, name=None):
    if ctx.message.author.id in owner:
        role = await bot.create_role(ctx.message.server)
        await bot.edit_role(ctx.message.server, role, name=name, hoist=False, mentionable=False)
        await bot.move_role(ctx.message.server, role, position)
        await bot.reply("**Kész!**")
    else:
        await bot.reply("**No u**")

@bot.command(pass_context=True)
async def give_role(ctx, member : discord.Member=None, *, name):
    if ctx.message.author.id in owner:
        role = discord.utils.get(ctx.message.server.roles, name=name)
        await bot.add_roles(member, role)
        await bot.reply("**Kész!**")
    else:
        await bot.reply("**No u**")

@bot.command(pass_context=True)
async def remove_role(ctx, member : discord.Member=None, *, name):
    if ctx.message.author.id in owner:
        role = discord.utils.get(ctx.message.server.roles, name=name)
        await bot.remove_roles(member, role)
        await bot.reply("**Kész!**")
    else:
        await bot.reply("**No u**")

@bot.command(pass_context=True)
async def delete_role(ctx, *, name=None):
    if ctx.message.author.id in owner:
        role = discord.utils.get(ctx.message.server.roles, name=name)
        await bot.delete_role(ctx.message.server, role)
        await bot.reply("**Kész!**")
    else:
        await bot.reply("**No u**")

#----------------COMMANDS--------------------
@bot.command(pass_context=True)
async def typing(ctx):
    await bot.say("**Typing effect ON!** :ok_hand:")
    await bot.send_typing(ctx.message.channel)

@bot.command(pass_context=True)
async def whoami(ctx):
    msg = [" the Captain, aye aye! <:blobSalute:402168383556157442>", " Sir Lancelot", " gay :couple_mm:", " :regional_indicator_y: :regional_indicator_o: :regional_indicator_u:", " banned <:pepeBanhammer:423892407650877442>", "John Dick", " the Terminator!!", f" nothing, so go to {LemonRoom.mention} and farm lemons", " me", " a Bot", "... aaaaaaaaa!! A SPIDER!!!", " SuperMario", "... Its Raining Man!", " the Deathhh", " a dancing skeleton", " your mom's child", " ( ͡° ͜ʖ ͡°) <- this guy", " your mom and your sister is your dad", " a chicken", " a rabbit xd", " a fucking chicken", " _nothing_  hehe", ", wait, who you?", " a giant penis", " the devil >:)", " Donald Trump", " an Alien", " scared as hell... (ha ha)", " somebody, idk u Lol.", " a fat mouse.", " the Sup-sup-super Grandma!", " uhm, Should i know you??", ", ahhhhhh", " You."]
    smsg = random.choice(msg)
    colours = [0x11806a, 0x1abc9c, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xe67e22, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
    col = random.choice(colours)
    em = discord.Embed(title="WHO AM I?", description=f"**\n{ctx.message.author}, You are{smsg}**", colour=col)
    em.set_thumbnail(url=ctx.message.author.avatar_url)
    await bot.send_message(ctx.message.channel, embed=em)

@bot.command(pass_context=True)
async def slap(ctx, member : discord.Member=None, *, Reason=None):
    if member is None:
        await bot.reply("**Használat: `-slap {member} {Reason}` köcce.**")
    else:
        await bot.say(f"**{ctx.message.author} megpofozta {member.mention}-t, mert __{Reason}__**")

@bot.command(pass_context=True)
async def kill(ctx, user : discord.User=None):
    if user is None:
        await bot.reply("**Használat: `-kill {member}` köcce.**")
    else:
        life = ["Yes", "Yes2" "No", "No2"]
        yourlife = random.choice(life)
        if yourlife == "Yes":
            await bot.say(f"**{user.mention} meghalt {ctx.message.author} által. RIP**")
        elif yourlife == "Yes2":
            await bot.say(f"**{ctx.message.author} leszúrta {user.mention}-t**")
        elif yourlife == "No":
            await bot.say(f"**Ha ha {ctx.message.author}, nagyon vicces xd**")
        else:
            await bot.say(f"**No u, {ctx.message.author}**")

@bot.command(pass_context=True)
async def ping(ctx):
    before = time.monotonic()
    embed = discord.Embed(description=":ping_pong: **...**", colour=0x3498db)
    msg = await bot.say(embed=embed)
    ping = (time.monotonic() - before) * 1000
    pinges = int(ping)
    if 999 > pinges > 400:
        mesg = "Az sok!"
    elif pinges > 1000:
        mesg = "Rohaddddttt lasssúuuúuúúú!!!!"
    elif 399 > pinges > 141:
        mesg = "Ahhh, nem jó!"
    elif pinges < 140:
        mesg = "Tükéletes ;)"
    em = discord.Embed(title=None, description=f":ping_pong: Úgy kb. `{pinges}` MS\n{mesg}", colour=0x3498db)
    em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    em.set_footer(text=timer)
    await bot.edit_message(msg, embed=em)

@bot.command(pass_context=True)
async def roll(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**Használat: `-roll {number} {number}` köcce.**")
    elif y is None:
        await bot.reply("**Használat: `-roll {number} {number}` ty.**")
    else:
        msg = random.randint(x, y)
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Oh, a választásom: {msg}**")

@bot.command(pass_context=True)
async def sub(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**Használat: `-sub {number} {number}` köcce.**")
    elif y is None:
        await bot.reply("**Használat: `-sub {number} {number}` köcce.**")
    else:
        msg = x - y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Oh, az eredmény: {msg}**")
    
@bot.command(pass_context=True)
async def mul(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**Használat: `-mul {number} {number}` köcce.**")
    elif y is None:
        await bot.reply("**Használat: `-mul {number} {number}` köcce.**")
    else:
        msg = x * y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Oh, az eredmény: {msg}**")
    
@bot.command(pass_context=True)
async def div(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**Használat: `-div {number} {number}` köcce.**")
    elif y is None:
        await bot.reply("**Használat: `-div {number} {number}` köcce.**")
    else:
        msg = x / y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Oh, az eredmény: {msg}**")
    
@bot.command(pass_context=True)
async def exp(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**Használat: `-exp {number} {number}` köcce.**")
    elif y is None:
        await bot.reply("**Használat: `-exp {number} {number}` köcce.**")
    else:
        msg = x ** y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Oh, az eredmény: {msg}**")
    
@bot.command(pass_context=True)
async def add(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**Használat: `-add {number} {number}` köcce.**")
    elif y is None:
        await bot.reply("**Használat: `-add {number} {number}` köcce.**")
    else:
        msg = x + y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Oh, az eredmény: {msg}**")
    
@bot.command()
async def game(*, play=None):
    if play is None:
        await bot.reply("**Használat: `-game {valami}` köcce.**")
    else:
        await bot.change_presence(game=discord.Game(name=play))
        em = discord.Embed(title="Game Status", description=f"Game status átállítva: __{play}__!", colour=0x3498db)
        await bot.say(embed=em)

@bot.command(pass_context=True)
async def nick(ctx, *, name=None):
    if name is None:
        await bot.reply("**Használat: `-name {Something to set as your name}` köcce.**")
    else:
        await bot.change_nickname(ctx.message.author, name)
        em = discord.Embed(title="Nickname", description=f"{ctx.message.author} beceneve átállítva: __{name}__!", colour=0x3498db)
        await bot.say(embed=em)

@bot.command(pass_context=True)
async def say(ctx, *, smth=None):
    if smth is None:
        await bot.reply("**Használat: `-say {valami}` köcce.**")
    else:
        await bot.say(f"**{smth}**")

@bot.command(pass_context=True)
async def poll(ctx, option=None, *, text=None):
    if text is None:
        await bot.reply("**Használat: `-poll {valami}` köcce.**")
    else:
        em = discord.Embed(title="Poll", description=text, colour=0x3498db)
        msg = await bot.send_message(ctx.message.channel, embed=em)
        await bot.add_reaction(msg, "👍")
        await bot.add_reaction(msg, "👎")

#-----------------------------------------------
@bot.event
async def on_message(message):
    if message.content.startswith("-time"):
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        await bot.send_message(message.channel, f"**{message.author.mention}, a pontos idő: __{timer}__**")
    if message.content.startswith('-8ball'):
        await bot.send_message(message.channel, random.choice(['**Egyértelműen :8ball:**',
                                                              '**Pffff... :8ball:**',
                                                              '**Kétség kívül :8ball:**',
                                                              '**No u :8ball:**',
                                                              '**Boi, alugyá... :8ball:**',
                                                              '**Ahogy látom, Igen. :8ball:**',
                                                              '**Ahogy látom, *No u*   :8ball:**',
                                                              '**Nem. :8ball:**',
                                                              '**Jó a kilátás :8ball:**',
                                                              '**Igen. :8ball:**',
                                                              '**A jelek azt mutatják: Ja. :8ball:**',
                                                              '**pls Nerf :8ball:**',
                                                              '**Majd máskor, nub. :8ball:**',
                                                              '**Inkább nem mondom el :8ball:**',
                                                              '**`Kávészünet.exe launched` :8ball:**',
                                                              '**Koncentrálj és kérdezd újra! :8ball:**',
                                                              '**`8ball.exe not found` :8ball:**',
                                                              '**Ne gyötörd magad ezen gyermekem. :8ball:**',
                                                              '**A válaszom, Nem. :8ball:**',
                                                              '**Az univerzum szerint magának gondjai vannak a télapóval... :8ball:**',
                                                              '**Az univerzum szerint, Igen. :8ball:**',
                                                              '**Majd ha cigánygyerekek potyognak az égbül! :8ball:**',
                                                              '**Ha! :8ball:**',
                                                              '**Anyádtól kérdezd!\nAnyaaaaa :8ball:**',
                                                              '**Anyaaaaaa :8ball:**',]))
    if message.content.startswith('-lenny'):
        ears = ['q{}p', 'ʢ{}ʡ', '⸮{}?', 'ʕ{}ʔ', 'ᖗ{}ᖘ', 'ᕦ{}ᕥ', 'ᕦ({})ᕥ', 'ᕙ({})ᕗ', 'ᘳ{}ᘰ', 'ᕮ{}ᕭ', 'ᕳ{}ᕲ', '({})', '[{}]', '୧{}୨', '୨{}୧', '⤜({})⤏', '☞{}☞', 'ᑫ{}ᑷ', 'ᑴ{}ᑷ', 'ヽ({})ﾉ', '乁({})ㄏ', '└[{}]┘', '(づ{})づ', '(ง{})ง', '|{}|']
        eyes = ['⌐■{}■', ' ͠°{} °', '⇀{}↼', '´• {} •`', '´{}`', '`{}´', 'ó{}ò', 'ò{}ó', '>{}<', 'Ƹ̵̡ {}Ʒ', 'ᗒ{}ᗕ', '⪧{}⪦', '⪦{}⪧', '⪩{}⪨', '⪨{}⪩', '⪰{}⪯', '⫑{}⫒', '⨴{}⨵', "⩿{}⪀", "⩾{}⩽", "⩺{}⩹", "⩹{}⩺", "◥▶{}◀◤", "≋{}≋", "૦ઁ{}૦ઁ", "  ͯ{}  ͯ", "  ̿{}  ̿", "  ͌{}  ͌", "ළ{}ළ", "◉{}◉", "☉{}☉", "・{}・", "▰{}▰", "ᵔ{}ᵔ", "□{}□", "☼{}☼", "*{}*", "⚆{}⚆", "⊜{}⊜", ">{}>", "❍{}❍", "￣{}￣", "─{}─", "✿{}✿", "•{}•", "T{}T", "^{}^", "ⱺ{}ⱺ", "@{}@", "ȍ{}ȍ", "x{}x", "-{}-", "${}$", "Ȍ{}Ȍ", "ʘ{}ʘ", "Ꝋ{}Ꝋ", "๏{}๏", "■{}■", "◕{}◕", "◔{}◔", "✧{}✧", "♥{}♥", " ͡°{} ͡°", "¬{}¬", " º {} º ", "⍜{}⍜", "⍤{}⍤", "ᴗ{}ᴗ", "ಠ{}ಠ", "σ{}σ"]
        mouth = ['v', 'ᴥ', 'ᗝ', 'Ѡ', 'ᗜ', 'Ꮂ', 'ヮ', '╭͜ʖ╮', ' ͟ل͜', ' ͜ʖ', ' ͟ʖ', ' ʖ̯', 'ω', '³', ' ε ', '﹏', 'ل͜', '╭╮', '‿‿', '▾', '‸', 'Д', '∀', '!', '人', '.', 'ロ', '_', '෴', 'ѽ', 'ഌ', '⏏', 'ツ', '益']
        lenny = random.choice(ears).format(random.choice(eyes)).format(random.choice(mouth))
        await bot.send_message(message.channel, "**Dikh egy lenny:**\n\n\t" + lenny)
    if message.content.startswith('-oof'):
        o = ['o00', 'oo', 'oO', 'o0', 'Oo', '0o', 'OOo', 'O0o', 'ooO', 'oo0', 'oo0oO', 'o0o', '0ooO', 'oo0oOO', 'ooo', '0oo', 'oooo', 'Ooo0', 'O0oo', 'ooo0', ]
        f = ['f', 'ff', 'fff']
        mark = ['!', '!!', '!!', '!1', '!!1', '!1!!', '1!!!', '!1!1!', '1!', '!!1!', '!!!1!', '!!!!', '!11!']
        msg1 = random.choice(o)
        msg2 = random.choice(f)
        msg3 = random.choice(mark)
        await bot.send_message(message.channel, msg1 + msg2 + msg3)
    if message.content.startswith('-leavepls'):
        em5 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n" 
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:", colour=0x3498db)
        msg = await bot.send_message(message.channel, embed=em5)
        await asyncio.sleep(1)
        em4 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                            ":black_circle::large_blue_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:", colour=0x3498db)
        await bot.edit_message(msg,  embed=em4)
        await asyncio.sleep(1)
        em3 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::large_blue_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:", colour=0x3498db)
        await bot.edit_message(msg,  embed=em3)
        await asyncio.sleep(1)
        em2 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::large_blue_circle::black_circle::black_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:", colour=0x3498db)
        await bot.edit_message(msg,  embed=em2)
        await asyncio.sleep(1)
        em1 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n", colour=0x3498db)
        await bot.edit_message(msg,  embed=em1)
        await asyncio.sleep(1)
        em0 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n" 
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:", colour=0x3498db)
        await bot.edit_message(msg,  embed=em0)
        await asyncio.sleep(1)
        em = discord.Embed(title="lol Joke", colour=0x3498db)
        em.set_thumbnail(url="https://cdn.discordapp.com/emojis/423864027610087426.png?v=1")
        await bot.edit_message(msg,  embed=em)
    if message.content.startswith('-commands'):
        emb = discord.Embed(title='Parancsaim', description="", colour=0x3498db)
        emb.add_field(name='--------------------', value='-typing\n'
                            '-whoami\n'
                            '-slap\n'
                            '-kill\n'
                            '-ping\n'
                            '-roll\n'
                            '-add\n'
                            '-suv\n'
                            '-mul\n'
                            '-div\n'
                            '-exp\n'
                            '-game\n'
                            '-nick\n'
                            '-say\n'
                            '-time\n'
                            '-leavepls\n'
                            '-lenny\n'
                            '-oof\n'
                            '-poll\n'
                            '-clear\n'
                            '-8ball', inline=False)
        emb.set_thumbnail(url='https://cdn.discordapp.com/emojis/385152309090451467.png?v=1')
        await bot.send_message(message.channel, embed=emb)
    await bot.process_commands(message) #IMPORTAN

token = os.environ.get('DISCORD_TOKEN')
bot.run(token)
