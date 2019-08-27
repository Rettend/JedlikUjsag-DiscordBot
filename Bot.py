import discord, aiohttp, asyncio, math, os, random, time, datetime
from discord.ext import commands
from time import gmtime

bot = commands.Bot(command_prefix="-", description="")
bot.remove_command("help")
msg = None
timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
"""underworking = discord.Embed(
        title=":warning: **Nem haver, ez még nincs kész...**",
        description=f"További információt Rettend-től kaphatsz.",
        colour=0xf1c40f,
    )
underworking.set_footer(text=timer)
await ctx.send(embed=underworking)


timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())"""

# -----------------SETUP----------------------
@bot.event
async def on_ready():
    print("Readdy boiii")
    print(discord.__version__)
    await bot.change_presence(
        status=discord.Status.online, activity=discord.Game(name="JSI is tha best")
    )


@bot.event
async def on_member_join(member):
    botserver = bot.get_guild(525316248855117824)
    userrole = botserver.get_role(606769595168063492)
    regisztralatlan = botserver.get_role(602487486853283864)
    await member.add_roles(regisztralatlan, userrole)
    membersroom = bot.get_channel(id=531167973025775627)
    await membersroom.edit(name=f"👥Létszám: {len(botserver.members)}")
    room = bot.get_channel(id=525316248855117826)
    em = discord.Embed(
        title=f"**__{member}__ csatlakozott a szerverhez!\nDA COMRADE!**",
        description="Érezd jól magad és tartsd be a szabályokat!\nRegistrálás után máris nekiláthatsz a chateléshez <:thonkSmile:607970831729033246>",
        colour=0x2ECC71,
    )
    em.set_thumbnail(url="https://cdn.discordapp.com/emojis/391322023739129856.png?v=1")
    await room.send(embed=em)


@bot.event
async def on_member_remove(member):
    botserver = bot.get_guild(525316248855117824)
    membersroom = bot.get_channel(id=531167973025775627)
    await membersroom.edit(name=f"👥Létszám: {len(botserver.members)}")
    room = bot.get_channel(id=606780290248998912)
    await room.send(f"**{member} lelépett...**")


# ------------------MOD-----------------------
@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member = None, Day: int = None, *, Reason=None):
    LogRoom = bot.get_channel(530825108651114498)
    botserver = bot.get_guild(525316248855117824)
    if user is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-ban {member} {0 - 7 napok, üzenetek törléséhez} {Indoklás}` köcce.**"
        )
    elif Reason is None:
        await ctx.sen(
            "**<:logo:542064398672330772> Használat: `-ban {member} {0 - 7 napok, üzenetek törléséhez} {Indoklás}` köcce.**"
        )
    elif Day is None:
        await ctx.sen(
            "**<:logo:542064398672330772> Használat: `-ban {member} {0 - 7 napok, üzenetek törléséhez} {Indoklás}` köcce.**"
        )
    elif user.id == ctx.message.author.id:
        await ctx.send(
            "**<:logo:542064398672330772> Nem fogom engedni, hogy saját magad bannold :P**"
        )
    else:
        await ctx.send(
            f"**{ctx.message.author.mention} Bannolta {user.mention}-t. Indoklás: __{Reason}__\nLásd a logokban itt: {LogRoom.mention}**"
        )
        em = discord.Embed(
            title="<:logo:542064398672330772> BAN", description=None, colour=0xAD1457
        )
        em.add_field(name="User", value=f"{user.name} ID: {user.id}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await LogRoom.send(embed=em)
        Private = await user.create_dm()
        await Private.send(
            f"**`Server: {botserver}`\nBAMM!! A Banhammer lecsapott rád, csaó!**"
        )
        await user.ban()


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx):
    em = discord.Embed(
        title=":octagonal_sign: **Bocsi haver, unbannolni nem fogsz tudni ezzel a parancsal...**",
        description=f"De továbbra is tudsz unbannolni manuálisan a szerver menüből:\nServer Settings > Bans > Kiválasztod a usert > Revoke Ban\n\nTovábbi információt {bot.owner_id}-től kaphatsz.",
        colour=0xE74C3C,
    )
    em.set_thumbnail(url="https://cdn.discordapp.com/emojis/588432140723552289.png?v=1")
    em.set_footer(text=timer)
    await ctx.send(embed=em)


"""@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, userid: int = None, *, Reason=None):
    LogRoom = bot.get_channel(530825108651114498)
    botserver = bot.get_guild(525316248855117824)
    if userid is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-unban {user id-ja} {Indoklás}` köcce.**"
        )
    elif Reason is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-unban {user id-ja} {Indoklás}` köcce.**"
        )
    elif userid == ctx.message.author.id:
        await ctx.send(
            "**<:logo:542064398672330772> Nem fogom engedni, hogy saját magad unbannold :P**"
        )
    else:
        user = await bot.fetch_user(userid)
        await ctx.send(
            f"**{ctx.message.author.mention} Unbannolta {user.mention}-t. Indoklás: __{Reason}__\nLásd a logokban itt: {LogRoom.mention}**"
        )
        em = discord.Embed(
            title="<:logo:542064398672330772> UNBAN", description=None, colour=0xE91E63
        )
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await LogRoom.send(embed=em)
        Private = await user.create_dm()
        await Private.send(
            f"**`Server: {botserver}`\nHello! Unbannoltak téged a {botserver} discord szerverről, Szeretnél visszajönni? \nhttps://discord.gg/VGqQ76V**"
        )
        await ctx.guild.unban(user)"""


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member = None, *, Reason=None):
    LogRoom = bot.get_channel(530825108651114498)
    botserver = bot.get_guild(525316248855117824)
    if user is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-kick {member} {Indoklás}` köcce.**"
        )
    elif Reason is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-kick {member} {Indoklás}` köcce.**"
        )
    elif user.id == ctx.message.author.id:
        await ctx.send(
            "**<:logo:542064398672330772> Nem fogom engedni, hogy saját magad kickeld :P**"
        )
    else:
        await ctx.send(
            f"**{ctx.message.author.mention} Kickelte {user.mention}-t. Indoklás: __{Reason}__\nLásd a logokban itt: {LogRoom.mention}**"
        )
        em = discord.Embed(
            title="<:logo:542064398672330772> KICK", description=None, colour=0xE74C3C
        )
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await LogRoom.send(embed=em)
        Private = await user.create_dm()
        await Private.send(
            f"**`Server: {botserver}`\nHello! Kirúgtak a {botserver} szerverről, viszlát!**"
        )
        await user.kick()


@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, user: discord.Member = None, duration: int = None, *, Reason=None):
    LogRoom = bot.get_channel(530825108651114498)
    botserver = bot.get_guild(525316248855117824)
    if user is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-mute {member} {Időtartam (s)} {Indoklás}` köcce.**"
        )
    elif Reason is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-mute {member} {Időtartam (s)} {Indoklás}` köcce.**"
        )
    elif duration is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-mute {member} {Időtartam (s)} {Indoklás}` köcce.**"
        )
    elif user.id == ctx.message.author.id:
        await ctx.send(
            "**<:logo:542064398672330772> Nem fogom engedni, hogy saját magad muteold :P**"
        )
    else:
        MutedRole = botserver.get_role(530829471909937175)
        await user.add_roles(MutedRole)
        await ctx.send(
            f"**{ctx.message.author.mention} Muttolta {user.mention}-t {duration} másodpercre. Indoklás: __{Reason}__\nLásd a logokban itt: {LogRoom.mention}**"
        )
        em = discord.Embed(
            title="<:logo:542064398672330772> MUTE", description=None, colour=0x11806A
        )
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.add_field(name="Duration", value=f"{duration} sec")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await LogRoom.send(embed=em)
        Private = await user.create_dm()
        await Private.send(
            f"**`Server: {botserver}`\nHello! Egy {duration} másodperces MUTE has appeard. Seems OP, pls nerf.**"
        )
        await asyncio.sleep(duration)
        await user.remove_roles(MutedRole)
        em = discord.Embed(
            title="<:logo:542064398672330772> UNMUTE", description=None, colour=0x1ABC9C
        )
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value="Lejárt a megadott időtartam...")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await LogRoom.send(embed=em)
        Private = await user.create_dm()
        await Private.send(
            f"**`Server: {botserver}`\nHello! Unmuttoltak a szerveren, de ne izgasd fel magad túlságosan...**"
        )


@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, user: discord.Member = None, *, Reason=None):
    LogRoom = bot.get_channel(530825108651114498)
    botserver = bot.get_guild(525316248855117824)
    MutedRole = botserver.get_role(530829471909937175)
    if user is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-unmute {member} {Indoklás}` köcce.**"
        )
    elif Reason is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-unmute {member} {Indoklás}` köcce.**"
        )
    elif MutedRole not in user.roles:
        await ctx.send(
            "**<:logo:542064398672330772> A felhasználó akit megadtál nincs Muteolva.**"
        )
    elif user.id == ctx.message.author.id:
        await ctx.send(
            "**<:logo:542064398672330772> Nem fogom engedni, hogy saját magad unmuteold :P**"
        )
    else:
        await user.remove_roles(MutedRole)
        await ctx.send(
            f"**{ctx.message.author.mention} Unmuttolta {user.mention}-t (he he). Indoklás: __{Reason}__\nLásd a logokban itt: {LogRoom.mention}**"
        )
        em = discord.Embed(
            title="<:logo:542064398672330772> UNMUTE", description=None, colour=0x1ABC9C
        )
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await LogRoom.send(embed=em)
        Private = await user.create_dm()
        await Private.send(
            f"**`Server: {botserver}`\nHello! Unmuttoltak a szerveren, de ne izgasd fel magad túlságosan...**"
        )


@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, duration: int = None, *, Reason=None):
    LogRoom = bot.get_channel(530825108651114498)
    botserver = bot.get_guild(525316248855117824)
    userrole = botserver.get_role(606769595168063492)
    if Reason is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-lock {szoba} {Időtartam (s)} {Indoklás}` köcce.**"
        )
    elif duration is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-lock {szoba} {Időtartam (s)} {Indoklás}` köcce.**"
        )
    else:
        channel = ctx.message.channel
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        await channel.set_permissions(target=userrole, overwrite=overwrite)
        await ctx.send(
            f"**{ctx.message.author.mention} lezárta a {ctx.message.channel.mention} szobát {duration} másodpercre. Indoklás: __{Reason}__**"
        )
        em = discord.Embed(
            title="<:logo:542064398672330772> LOCK", description=None, colour=0x1F8B4C
        )
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.add_field(name="Duration", value=f"{duration} sec")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await LogRoom.send(embed=em)
        await asyncio.sleep(duration)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        await channel.set_permissions(target=userrole, overwrite=overwrite)
        await ctx.send(
            f"**Feloldottam a {ctx.message.channel.mention} szobát, mert __lejárt az idő__.**"
        )
        em = discord.Embed(
            title="<:logo:542064398672330772> UNLOCK", description=None, colour=0x2ECC71
        )
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{bot.user}")
        em.add_field(name="Reason", value=f"lejárt az idő")
        em.set_author(name=bot.user, icon_url=bot.user.avatar_url)
        em.set_footer(text=timer)
        await LogRoom.send(embed=em)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, *, Reason=None):
    LogRoom = bot.get_channel(530825108651114498)
    botserver = bot.get_guild(525316248855117824)
    userrole = botserver.get_role(606769595168063492)
    if Reason is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-unlock {szoba} {Indoklás}` köcce.**"
        )
    else:
        channel = ctx.message.channel
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        await channel.set_permissions(target=userrole, overwrite=overwrite)
        await ctx.send(
            f"**{ctx.message.author} feloldotta a {ctx.message.channel.mention} szobát. Indoklás: __{Reason}__**"
        )
        em = discord.Embed(
            title="<:logo:542064398672330772> UNLOCK", description=None, colour=0x2ECC71
        )
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await LogRoom.send(embed=em)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number: int = None):
    LogRoom = bot.get_channel(530825108651114498)
    if number is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-clear {üzenetek száma}` köcce.**"
        )
    else:
        number += 1
        deleted = await ctx.message.channel.purge(limit=number)
        num = number - 1
        em = discord.Embed(
            title="<:logo:542064398672330772> CLEAR",
            description=f"{ctx.message.author.name} törölt __{deleted}__ üzenetet",
            colour=0x3498DB,
        )
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        msg = await ctx.send(embed=em)
        await LogRoom.send(embed=em)
        await asyncio.sleep(4)
        await msg.delete()


# -----------------COMMANDS--------------------
@bot.command()
async def ping(ctx):
    before = time.monotonic()
    embed = discord.Embed(description=":ping_pong: **...**", colour=0x2ECC71)
    msg = await ctx.send(embed=embed)
    ping = (time.monotonic() - before) * 1000
    pinges = int(ping)
    if 999 > pinges > 400:
        mesg = "Az sok!"
    elif pinges > 1000:
        mesg = "Rohaddddttt lasssúuuúuúúú!!4!44!"
    elif 399 > pinges > 141:
        mesg = "Ahhh, nem jó!"
    elif pinges < 140:
        mesg = "Tükéletes ;)"
    em = discord.Embed(
        title=None,
        description=f":ping_pong: Úgy kb. `{pinges}` MS\n{mesg}",
        colour=0x2ECC71,
    )
    em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    em.set_footer(text=timer)
    await msg.edit(embed=em)


@bot.command()
async def suggest(ctx, pref=None, *, text=None):
    if pref is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-suggest {prefix (Q, S, C)} {szöveg}`\nAz elérhető prefixek:\n`Q: question (kérdés)`\n`S: suggestion (kérés, ötlet)`\n`C: command suggestion (parancs ötlet)`**"
        )
    elif text is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-suggest {prefix (Q, S, C)} {szöveg}`\nAz elérhető prefixek:\n`Q: question (kérdés)`\n`S: suggestion (kérés, ötlet)`\n`C: command suggestion (parancs ötlet)`**"
        )
    else:
        if pref is "S" or "s":
            msg = "SUGGESTION"
        elif pref is "Q" or "q":
            msg = "QUESTION"
        elif pref is "C" or "c":
            msg = "COMMAND SUGGESTION"
        else:
            ctx.send(
                "**<:logo:542064398672330772> A megadott `prefix` nem létezik, kérlek használj egy elérhető prefixet:\n`Q: question (kérdés)`\n`S: suggestion (kérés, ötlet)`\n`C: command suggestion (parancs ötlet)`**"
            )
            msg = None
        if msg is None:
            pass
        else:
            colours = [
                0x11806A,
                0x1ABC9C,
                0x2ECC71,
                0x1F8B4C,
                0x3498DB,
                0x206694,
                0x9B59B6,
                0x71368A,
                0xE91E63,
                0xAD1457,
                0xF1C40F,
                0xC27C0E,
                0xE67E22,
                0xA84300,
                0xE74C3C,
                0x992D22,
                0x95A5A6,
                0x607D8B,
                0x979C9F,
                0x546E7A,
            ]
            col = random.choice(colours)
            em = discord.Embed(
                title=f"<:logo:542064398672330772> {msg}",
                description=f"**Feladó: {ctx.message.author.mention}**\n⋙ {text}",
                colour=col,
            )
            em.set_author(
                name=ctx.message.author, icon_url=ctx.message.author.avatar_url
            )
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            channel = bot.get_channel(id=542060960731627520)
            await ctx.send(f"**:white_check_mark: Elküldve ide: {channel.mention}**")
            mesg = await channel.send(embed=em)
            if pref is "S" or "C":
                await mesg.add_reaction("👍")
                await mesg.add_reaction("👎")


@bot.command()
async def bug(ctx, *, text=None):
    if text is None:
        await ctx.send("**<:logo:542064398672330772> Használat: `-bug {szöveg}`**")
    else:
        em = discord.Embed(
            title=f"<:logo:542064398672330772> Bug jelentés",
            description=f"**Feladó: {ctx.message.author.mention}**\n⋙ {text}",
            colour=0x2ECC71,
        )
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        channel = bot.get_channel(id=542063494271336473)
        await ctx.send(f"**:white_check_mark: Elküldve ide: {channel.mention}**")
        mesg = await channel.send(embed=em)
        await mesg.add_reaction("👍")
        await mesg.add_reaction("👎")


@bot.command()
async def say(ctx, *, smth=None):
    if smth is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-say {szöveg}` köcce.**"
        )
    else:
        await ctx.send(f"**{smth}**")


@bot.command()
async def underworking(ctx):
    underworking = discord.Embed(
        title=":warning: **Nem haver, ez még nincs kész...**",
        description=f"További információt Rettend-től kaphatsz.",
        colour=0xF1C40F,
    )
    underworking.set_footer(text=timer)
    await ctx.send(embed=underworking)


"""@bot.command()
async def boostinfo(ctx):
    botserver = bot.get_guild(525316248855117824)
    em = discord.Embed(
        title=f"<a:nitroBoost:607204993719861269> SZERVER BOOSTOLÁS",
        description="",
        colour=discord.Colour.from_rgb(253, 124, 240),
    )
    em.add_field(
        name="Tudnivalók a Szerver Boostolásról",
        value=":white_small_square: Mindenki aki Nitro előfizetéssel rendelkezik segítheti a szerverünket, azzal hogy Boostolja azt. Ezzel a szerverünknek végtelen kiváltságokat tud szerezni:\n"
        "-Szerver-banner, egyedi URL link, instant invite link egyedi háttérképpel, megnövelt fájl-feltőltési limit, animált szerver ikon, nagyobb audio quality,több emoji férőhely és még több, mert ez a lista folyamatosan bővül!\n\n"
        ":white_small_square: Milyen előnyökkel jár a szerver boostolása számomra?\n"
        "-Azon kívül, hogy eláraszt majd a sok hálálkodás, kapni fogsz egy különleges role-t ami csak Boostereknek érhető el valamint egy testreszabható <:boost:607221518891483157> Nitro Szerver Booster ikont a neved mellé a profilodnál és a tagok listáján.\n\n",
        inline=False,
    )
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    em.set_footer(text=timer)
    await ctx.send(embed=em)
    e = discord.Embed(
        title="", description="", colour=discord.Colour.from_rgb(253, 124, 240)
    )
    e.add_field(
        name="----------------",
        value=":white_small_square: Ha ez önmagában még nem lenne rengeteg, a Nitro előfizetésnek is rengeteg előnye van:\n"
        "-Egyedi discord tag, -animált profilkép, ultra-hiper-szuper képesség, amivel bárhol használhatod az emojikat, magas felbontású képernyőmegosztás, 50MB-ost fájl-feltöltési limit, és végül egy csillogó Nitro jelvény a neved mellé a profilodon.\n\n"
        ":white_small_square: Ezekután le lehet-e írni azt az összeget amibe mindez kerül!?\n"
        "-Naná! Havonta US$9.99, vagy évente US$99.99!\n\n"
        ":white_small_square: Már Boostoltam a szervert, hogyan tudnék még segíteni?\n"
        "<a:pepeBoost:607205032814968863> -A Nitro előfizetést akár el is tudod ajándékozni valakinek a szerveren, hogy Boostoljon minket!\n\n"
        "**További információt kaphatsz a `-boost` paranccsal.**",
        inline=False,
    )
    e.set_footer(text=timer)
    await ctx.send(embed=e)"""


@bot.command()
async def boost(ctx):
    botserver = bot.get_guild(525316248855117824)
    em = discord.Embed(
        title=f"<a:nitroBoost:607204993719861269> SZERVER BOOSTOLÁS",
        description=f"**:gem: A szerverünk Nitro Server Boost szintje: {botserver.premium_tier}\n"
        f"<a:wumpus:607214752090816512> {botserver.emoji_limit} Emoji férőhelyünk van jelenleg, ebből {len(botserver.emojis)}-t használunk\n"
        f":arrow_up: {botserver.filesize_limit / 1024 / 1024} MB A jelenlegi maximum fájl-feltöltési limit mindenki számára\n"
        f"<:logo:542064398672330772> {botserver.premium_subscription_count} extrémen nagyszerű ember boostolja a szerverünket jelenleg\n"
        f"<:blobSalute:588432140710969408> Akik a szerverünket boostolják: {botserver.premium_subscribers}\n\n**",
        colour=discord.Colour.from_rgb(253, 124, 240),
    )
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    em.set_footer(text=timer)
    await ctx.send(embed=em)


@bot.command()
async def submit(
    ctx, name: str = None, colours: str = None, *, description: str = None
):
    if name is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-submit {Témanév} {Szín1-Szín2...} {Megjegyzés}`**"
        )
    elif colours is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-submit {Témanév} {Szín1-Szín2...} {Megjegyzés}`**"
        )
    elif description is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-submit {Témanév} {Szín1-Szín2...} {Megjegyzés}`**"
        )
    else:
        channel = bot.get_channel(604193004852609035)
        em = discord.Embed(
            title="Téma feltöltés",
            description=f"Feladó: {ctx.message.author.mention}\n",
            color=ctx.message.author.color,
        )
        em.add_field(name="Téma neve", value=f"{name}")
        em.add_field(name="Színek", value=f"{colours.replace('-', ' ')}")
        em.add_field(name="Megjegyzés", value=f"{description}")
        em.set_thumbnail(url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        msg = await channel.send(embed=em)
        await ctx.send(f"**:white_check_mark: Elküldve ide: {channel.mention}**")
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")


@bot.command()
async def slap(ctx, member: discord.Member = None, *, Reason=None):
    if member is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-slap {member} {Indoklás}` köcce.**"
        )
    else:
        await ctx.send(
            f"**{ctx.message.author} megpofozta {member.mention}-t, mert __{Reason}__**"
        )


@bot.command()
async def kill(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-kill {member}` köcce.**"
        )
    else:
        if user.id is bot.user.id:
            await ctx.send(
                f"**Oshit valaki a halálom akarja <:thonkEyes:607970832647454721>**"
            )
        elif user.id is ctx.message.author.id:
            await ctx.send(f"**Hogy valakinek milyen suicidal hajlamai vannak...**")
        else:
            await ctx.send(
                f"**{ctx.message.author} kegyetlenül legyilkolta {user.mention}-t. He ded.**"
            )


@bot.command()
async def roll(ctx, x: int = None, y: int = None):
    if x is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-roll {szám1} {szám2}` köcce.**"
        )
    elif y is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-roll {szám1} {szám2}` köcce.**"
        )
    else:
        msg = random.randint(x, y)
        text = await ctx.send("**Hmmm...**")
        await asyncio.sleep(3)
        await text.edit(content=f"**Oh, a választásom: {msg}**")


@bot.command()
async def sub(ctx, x: int = None, y: int = None):
    if x is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-sub {szám1} {szám2}` köcce.**"
        )
    elif y is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-sub {szám1} {szám2}` köcce.**"
        )
    else:
        msg = x - y
        text = await ctx.send("**Hmmm...**")
        await asyncio.sleep(3)
        await text.edit(content=f"**Oh, az eredmény: {msg}**")


@bot.command()
async def mul(ctx, x: int = None, y: int = None):
    if x is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-mul {szám1} {szám2}` köcce.**"
        )
    elif y is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-mul {szám1} {szám2}` köcce.**"
        )
    else:
        msg = x * y
        text = await ctx.send("**Hmmm...**")
        await asyncio.sleep(3)
        await text.edit(content=f"**Oh, az eredmény: {msg}**")


@bot.command()
async def div(ctx, x: int = None, y: int = None):
    if x is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-div {szám1} {szám2}` köcce.**"
        )
    elif y is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-div {szám1} {szám2}` köcce.**"
        )
    else:
        msg = x / y
        text = await ctx.send("**Hmmm...**")
        await asyncio.sleep(3)
        await text.edit(content=f"**Oh, az eredmény: {msg}**")


@bot.command()
async def exp(ctx, x: int = None, y: int = None):
    if x is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-exp {szám1} {szám2}` köcce.**"
        )
    elif y is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-exp {szám1} {szám2}` köcce.**"
        )
    else:
        msg = x ** y
        text = await ctx.send("**Hmmm...**")
        await asyncio.sleep(3)
        await text.edit(content=f"**Oh, az eredmény: {msg}**")


@bot.command()
async def add(ctx, x: int = None, y: int = None):
    if x is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-add {szám1} {szám2}` köcce.**"
        )
    elif y is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-add {szám1} {szám2}` köcce.**"
        )
    else:
        msg = x + y
        text = await ctx.send("**Hmmm...**")
        await asyncio.sleep(3)
        await text.edit(content=f"**Oh, az eredmény: {msg}**")


@bot.command()
async def game(ctx, *, play=None):
    if play is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-game {valami}` köcce.**"
        )
    else:
        await bot.change_presence(
            status=discord.Status.online, activity=discord.Game(name=f"{play}")
        )

        em = discord.Embed(
            title="Game Status",
            description=f"Most épp ezzel játszom: __{play}__!",
            colour=0x2ECC71,
        )
        await ctx.send(embed=em)


@bot.command()
async def nick(ctx, *, name=None):
    if name is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-name {neved}` köcce.**"
        )
    else:
        await ctx.message.author.edit(nick=name)
        em = discord.Embed(
            title="Nickname",
            description=f"{ctx.message.author} beceneve átállítva: __{name}__!",
            colour=0x2ECC71,
        )
        await ctx.send(embed=em)


@bot.command()
async def poll(ctx, option=None, *, text=None):
    if text is None:
        await ctx.reply("**Használat: `-poll {szöveg}` köcce.**")
    else:
        em = discord.Embed(title="Poll", description=text, colour=0x979C9F)
        msg = await ctx.send(embed=em)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")


@bot.command()
async def joined(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send(
            "**<:logo:542064398672330772> Használat: `-joined {member}` köcce.**"
        )
    else:
        await ctx.send(f"**{user} csatlakozási dátuma:\n> {user.joined_at}**")


@bot.command()
async def register(ctx):
    botserver = bot.get_guild(525316248855117824)
    olvaso =  botserver.get_role(602439300948426763)
    regisztralatlan = botserver.get_role(602487486853283864)
    msg = await ctx.send(f">>> Beep.")
    await asyncio.sleep(0.5)
    await msg.edit(content=f">>> Beep.\n__name__ : {ctx.message.author.mention}")
    await asyncio.sleep(1)
    await msg.edit(content=f">>> Beep.\n__name__ : {ctx.message.author.mention}\n__id__ : {ctx.message.author.id}")
    await asyncio.sleep(0.4)
    await msg.edit(content=f">>> Beep.\n__name__ : {ctx.message.author.mention}\n__id__ : {ctx.message.author.id}\nEllenőrzés.")
    await asyncio.sleep(0.3)
    await msg.edit(content=f">>> Beep.\n__name__ : {ctx.message.author.mention}\n__id__ : {ctx.message.author.id}\nEllenőrzés..")
    await asyncio.sleep(0.5)
    await msg.edit(content=f">>> Beep.\n__name__ : {ctx.message.author.mention}\n__id__ : {ctx.message.author.id}\nEllenőrzés...")
    await asyncio.sleep(0.4)
    if regisztralatlan in ctx.message.author.roles:
        await msg.edit(content=f">>> Beep.\nEllenőrzés... `hiba.`")
        await asyncio.sleep(0.8)
        await msg.edit(content=f"**{ctx.message.author.mention}, nagy esély van rá, hogy te már regisztrálva vagy <:Thonk:607970148728569859>**")
    else:
        await msg.edit(content=f">>> Beep.\n__name__ : {ctx.message.author.mention}\n__id__ : {ctx.message.author.id}\nEllenőrzés... `kész.`")
        await asyncio.sleep(0.3)
        await msg.edit(content=f">>> Beep.\n__name__ : {ctx.message.author.mention}\n__id__ : {ctx.message.author.id}\nEllenőrzés... `kész.`\n\nFelhasználó hozzáadása a szobákhoz.")
        await asyncio.sleep(1.4)
        await ctx.message.author.add_roles(olvaso)
        await ctx.message.author.remove_roles(regisztralatlan)
        await msg.edit(content=f">>> Beep.\n__name__ : {ctx.message.author.mention}\n__id__ : {ctx.message.author.id}\nEllenőrzés... `kész.`\n\nFelhasználó hozzáadása a szobákhoz... `kész.`")
        await asyncio.sleep(0.8)
        await msg.edit(content=f">>> Beep.\n__name__ : {ctx.message.author.mention}\n__id__ : {ctx.message.author.id}\nEllenőrzés... `kész.`\n\nFelhasználó hozzáadása a szobákhoz... `kész.`\n\n**{ctx.message.author.mention} regisztrálva!**")



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith("-discord.py"):
        await message.channel.send(f"**Discord.py könyvtár verziója:\n> {discord.__version__}**")

    if message.content.startswith("-8ball"):
        await message.channel.send(
            random.choice(
                [
                    "**Egyértelműen :8ball:**",
                    "**Pffff... :8ball:**",
                    "**Kétség kívül :8ball:**",
                    "**No u :8ball:**",
                    "**Boi, alugyá... :8ball:**",
                    "**Ahogy látom, Igen. :8ball:**",
                    "**Ahogy látom, *No u*   :8ball:**",
                    "**Nem. :8ball:**",
                    "**Jó a kilátás erre :8ball:**",
                    "**Igen. :8ball:**",
                    "**A jelek azt mutatják: Ja. :8ball:**",
                    "**pls Nerf :8ball:**",
                    "**Majd máskor, nub. :8ball:**",
                    "**Inkább nem mondom el :8ball:**",
                    "**`Kávészünet.exe launched` :8ball:**",
                    "**Koncentrálj és kérdezd újra! :8ball:**",
                    "**`8ball.exe not found` :8ball:**",
                    "**Ne gyötörd magad ezen gyermekem. :8ball:**",
                    "**A válaszom, Nem. :8ball:**",
                    "**Az univerzum szerint ön saját magának is hazudik... :8ball:**",
                    "**Az univerzum szerint, Igen. :8ball:**",
                    "**Majd ha cigánygyerekek potyognak az égbül! :8ball:**",
                    "**Ha! :8ball:**",
                    "**Neeeeeeeeeeeeeee :8ball:**",
                    "**Hogyaviharbane :8ball:**",
                    "**<:SherlockBlob:609308824985141249> :8ball:**",
                    "**<:BlobThink:609306167918985218> :8ball:**",
                ]
            )
        )
    if message.content.startswith("-lenny"):
        ears = [
            "q{}p",
            "ʢ{}ʡ",
            "⸮{}?",
            "ʕ{}ʔ",
            "ᖗ{}ᖘ",
            "ᕦ{}ᕥ",
            "ᕦ({})ᕥ",
            "ᕙ({})ᕗ",
            "ᘳ{}ᘰ",
            "ᕮ{}ᕭ",
            "ᕳ{}ᕲ",
            "({})",
            "[{}]",
            "୧{}୨",
            "୨{}୧",
            "⤜({})⤏",
            "☞{}☞",
            "ᑫ{}ᑷ",
            "ᑴ{}ᑷ",
            "ヽ({})ﾉ",
            "乁({})ㄏ",
            "└[{}]┘",
            "(づ{})づ",
            "(ง{})ง",
            "|{}|",
        ]
        eyes = [
            "⌐■{}■",
            " ͠°{} °",
            "⇀{}↼",
            "´• {} •`",
            "´{}`",
            "`{}´",
            "ó{}ò",
            "ò{}ó",
            ">{}<",
            "Ƹ̵̡ {}Ʒ",
            "ᗒ{}ᗕ",
            "⪧{}⪦",
            "⪦{}⪧",
            "⪩{}⪨",
            "⪨{}⪩",
            "⪰{}⪯",
            "⫑{}⫒",
            "⨴{}⨵",
            "⩿{}⪀",
            "⩾{}⩽",
            "⩺{}⩹",
            "⩹{}⩺",
            "◥▶{}◀◤",
            "≋{}≋",
            "૦ઁ{}૦ઁ",
            "  ͯ{}  ͯ",
            "  ̿{}  ̿",
            "  ͌{}  ͌",
            "ළ{}ළ",
            "◉{}◉",
            "☉{}☉",
            "・{}・",
            "▰{}▰",
            "ᵔ{}ᵔ",
            "□{}□",
            "☼{}☼",
            "*{}*",
            "⚆{}⚆",
            "⊜{}⊜",
            ">{}>",
            "❍{}❍",
            "￣{}￣",
            "─{}─",
            "✿{}✿",
            "•{}•",
            "T{}T",
            "^{}^",
            "ⱺ{}ⱺ",
            "@{}@",
            "ȍ{}ȍ",
            "x{}x",
            "-{}-",
            "${}$",
            "Ȍ{}Ȍ",
            "ʘ{}ʘ",
            "Ꝋ{}Ꝋ",
            "๏{}๏",
            "■{}■",
            "◕{}◕",
            "◔{}◔",
            "✧{}✧",
            "♥{}♥",
            " ͡°{} ͡°",
            "¬{}¬",
            " º {} º ",
            "⍜{}⍜",
            "⍤{}⍤",
            "ᴗ{}ᴗ",
            "ಠ{}ಠ",
            "σ{}σ",
        ]
        mouth = [
            "v",
            "ᴥ",
            "ᗝ",
            "Ѡ",
            "ᗜ",
            "Ꮂ",
            "ヮ",
            "╭͜ʖ╮",
            " ͟ل͜",
            " ͜ʖ",
            " ͟ʖ",
            " ʖ̯",
            "ω",
            "³",
            " ε ",
            "﹏",
            "ل͜",
            "╭╮",
            "‿‿",
            "▾",
            "‸",
            "Д",
            "∀",
            "!",
            "人",
            ".",
            "ロ",
            "_",
            "෴",
            "ѽ",
            "ഌ",
            "⏏",
            "ツ",
            "益",
        ]
        lenny = (
            random.choice(ears).format(random.choice(eyes)).format(random.choice(mouth))
        )
        await message.channel.send(f"**{lenny}**")
    if message.content.startswith("-oof"):
        o = [
            "o00",
            "oo",
            "oO",
            "o0",
            "Oo",
            "0o",
            "OOo",
            "O0o",
            "ooO",
            "oo0",
            "oo0oO",
            "o0o",
            "0ooO",
            "oo0oOO",
            "ooo",
            "0oo",
            "oooo",
            "Ooo0",
            "O0oo",
            "ooo0",
        ]
        f = ["f", "ff", "fff"]
        mark = [
            "!",
            "!!",
            "!!",
            "!1",
            "!!1",
            "!1!!",
            "1!!!",
            "!1!1!",
            "1!",
            "!!1!",
            "!!!1!",
            "!!!!",
            "!11!",
        ]
        msg1 = random.choice(o)
        msg2 = random.choice(f)
        msg3 = random.choice(mark)
        await message.channel.send(msg1 + msg2 + msg3)
    await bot.process_commands(message)  # ROHADT FONTOS


"""
@bot.command(name="time")
async def _time(ctx):
    timer = time.strftime("%a, %d %b %Y %I:%M:%S %p", most)
    await ctx.send(f"**{ctx.author.mention}, a pontos idő: __{timer}__ UTC + 2, Közép-európai idő.**")"""


@bot.command()
async def mod(ctx):
    e = discord.Embed(title="Moderátor", description="", colour=0x3498DB)
    e.add_field(
        name="Admin parancsok",
        value=":small_blue_diamond: `-ban {member} {0 - 7 napok, üzenetek törléséhez} {Indoklás}`\n"
        ":black_small_square: Eltávolítja a user-t és kitörli az összes elküldött üzenetét visszamenőleg max. 7 napra. A user nem lesz képes visszacsatlakozni amíg nem Unbannolják.\n"
        "\n"
        ":small_blue_diamond: `-unban {member} {Indoklás}`\n"
        ":black_small_square: :warning: Ez sajnos nem működik mert egy rák... Használj manuális unban-t: Server Settings > Bans > Kiválasztod a user-t > Revoke Ban. ty.\n"
        "\n",
        inline=False,
    )
    em = discord.Embed(title="Moderátor", description="", colour=0x3498DB)
    em.add_field(
        name="Admin parancsok",
        value=":small_blue_diamond: `-lock {Időtartam (másodperc)} {Indoklás}` :information_source: Adminisztrátorokra nem hat! :warning: A privát, titkosított vagy egyéni `channel.Permissions`-el rendelkező szobákban rendellenesen működhet! A parancs csak a user role-all rendelkező felhasználókra hat!\n"
        ":black_small_square: Lelockolja a jelenlegi szobát, ezáltal senki se lesz képes a szobába üzenetet küldeni. A megadott ídőtartam lejárta után a Bot automatikusan Unlockolja a szobát.\n"
        "\n"
        ":small_blue_diamond: `-unlock {Indoklás}`\n"
        ":black_small_square: Unlockolja a jelenlegi szobát, ezáltal visszaállnak a régi `channel.Permission` beállítások. A Lockolásnál megadott időtartam lejárta előtt érdemes használni.\n"
        "\n",
        inline=False,
    )
    emb = discord.Embed(title="Moderátor", description="", colour=0x3498DB)
    emb.add_field(
        name="Moderátor parancsok",
        value=":small_blue_diamond: `-kick {member} {Indoklás}`\n"
        ":black_small_square: Eltávolítja a user-t a szerverről. A user vissza tud lépni a szerverre Instant Invite Link segítségével.\n"
        "\n"
        ':small_blue_diamond: `-mute {member} {Időtartam (másodperc)} {Indoklás}` :information_source: A parancs "Muted" rolet ad a usernek!\n'
        ":black_small_square: Megakadályozza, hogy a user további üzenetet küldjön az összes szobában. A megadott ídőtartam lejárta után a Bot automatikusan Unmuteolja a user-t.\n"
        "\n"
        ":small_blue_diamond: `-unmute {member} {Indoklás}`\n"
        ":black_small_square: Unmuteolja a user-t ezzel a user újra képes lesz üzeneteket küldeni. A Muteolásnál megadott időtartam lejárta előtt érdemes használni.\n"
        "\n",
        inline=False,
    )
    embed = discord.Embed(title="Moderátor", description="", colour=0x3498DB)
    embed.add_field(
        name="Moderátor parancsok",
        value=":small_blue_diamond: `-clear {üzenetek száma}` :information_source: A Bot megerősítő üzenetet küld a jelenlegi szobába is, ezt az üzenetet 4 másodperc múlva kitörli!\n"
        ":black_small_square: Kitörli a legutóbb elküldött megadott mennyiségű üzenetet.\n"
        ":small_blue_diamond: `!warn {member}`\n"
        ":black_small_square: Egy figyelmeztetést logol a felhasználóról, a figyelmeztetések halmozódnak, így aki nem bír magával az egyre súlyosabb bűntetést kap.\n"
        ":small_blue_diamond: `!infractions {member}`\n"
        ":black_small_square: Megmutatja, hogy a felhasználó mikor, miért és mennyi figyelmeztetést kappot.\n",
        inline=False,
    )
    await ctx.send(embed=e)
    await ctx.send(embed=em)
    await ctx.send(embed=emb)
    await ctx.send(embed=embed)


@bot.command()
async def commands(ctx):
    e = discord.Embed(
        title="**Parancsok**",
        description=f"Ezek a parancsok, a szórakoztató kategóriába tartoznak, további parancsokért a `-help` parancsot használd.",
        colour=0xE67E22,
    )
    e.add_field(
        name="Hasznos Parancsok",
        value=":small_orange_diamond: `-say {szöveg}`: A bot megismétli amit mondasz neki.\n"
        ":small_orange_diamond: `-boost`: Információ a Szerver-boostolásról.\n"
        ":small_orange_diamond: `-poll {szöveg}`: Egy gyors szavazást indíthatsz.\n"
        ":small_orange_diamond: `-slap {member} {Indoklás}`: A megnevezett illető egy jó kis sallert kap, amitől talán megjön az esze.\n"
        ":small_orange_diamond: `-kill {member}`: Interaktív parancs. A megadott személyt kegyetlenül le lehet gyilkolni.\n"
        ":small_orange_diamond: `-discord.py`: A használt könyvtár verzióját adja vissza.\n"
        ':small_orange_diamond: `-game {szöveg}`: A Botnak beállít egy Game Status-t amivel a Bot "játszani fog."\n',
        inline=False,
    )
    em = discord.Embed(title="", description="", colour=0x3498DB)
    em.add_field(
        name="Számtani Parancsok",
        value=":diamonds: `-roll {szám1} {szám2}`: Egy véletlenszerű számot ad vissza a megadott számokon belül.\n"
        ":diamonds: `-add {szám1} {szám2}`: szám1 + szám2.\n"
        ":diamonds: `-sub {szám1} {szám2}`: szám1 - szám2.\n"
        ":diamonds: `-mul {szám1} {szám2}`: szám1 * szám2.\n"
        ":diamonds: `-div {szám1} {szám2}`: szám1 / szám2.\n"
        ":diamonds: `-exp {szám1} {szám2}`: szám1 ** szám2.\n",
        inline=False,
    )
    emb = discord.Embed(title="", description="", colour=0xE74C3C)
    emb.add_field(
        name="Vicces Parancsok",
        value=":small_blue_diamond: `-lenny`: Lennyface generátor.\n"
        ":small_blue_diamond: `-oof`: Oof generátor\n"
        ":small_blue_diamond: `-joined {member}`: Megtudhatod, hogy mikor csatlakoztál a szerverhez.\n"
        ":small_blue_diamond: `-8ball {kérdés}`: Feltehetsz egy kérdést az univerzumnak.\n"
        ":small_blue_diamond: `-underworking`: Tesztelő parancs, az Underworking üzenetet adja vissza, amit akkor használunk, ha valami még nincs kész.\n",
        inline=False,
    )
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    emb.set_footer(text=timer)
    await ctx.send(embed=e)
    await ctx.send(embed=em)
    await ctx.send(embed=emb)


@bot.command(name="help")
async def _help(ctx):
    e = discord.Embed(
        title="**SEGíTSÉÉÉÉÉÉÉG**",
        description=f"Az alábbi parancsok biztosan kielégítik információ éhségedet, de ha nem, akkor esetleg Rettendtől kaphatsz választ.",
        colour=0x2ECC71,
    )
    e.add_field(
        name="Fontosabb Parancsok",
        value=":green_book: `-help`\n"
        ":white_small_square: Megkapod ezt a gyönyörű üzenetet.\n"
        ":green_book: `-mod`\n"
        ":white_small_square: A Moderátor parancsok, de ha nem vagy Moderátor akkor minek is nézegetnéd, igaz?\n"
        ":green_book: `-commands`\n"
        ":white_small_square: Az egyéb Fun kategóriába tartozó parancsok.\n",
        inline=False,
    )
    em = discord.Embed(title="", description="", colour=0x2ECC71)
    em.add_field(
        name="Fontos Parancsok",
        value=":green_book: `-suggest {prefix} {szöveg}`: Kérést, ötletet küldetsz nekünk.\n"
        ":green_book: `-bug {szöveg}`: Hibajelentést tehetsz nekünk.\n"
        ":green_book: `-ping`: Lekérheted a pinged, dejóóó.\n"
        ":green_book: `-nick {név}`: Ezzel a paranccsal változtathatod meg a neved.\n"
        "::green_book: `-submit {Témanév} {szín1-szín2...} {megjegyzés}`: Témát tölthetsz fel az oldalnak.\n",
        inline=False,
    )
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    em.set_footer(text=timer)
    await ctx.send(embed=e)
    await ctx.send(embed=em)


# --------------------RUN----------------------
bot.run("DISCORD_TOKEN")
