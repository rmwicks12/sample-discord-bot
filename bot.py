import discord
import youtube_dl
from discord.enums import ActivityType
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.bot import Bot
import random
import os

from discord.guild import Guild


intents = discord.Intents.default()

intents.members = True
client = commands.Bot(command_prefix="^", intents = intents, activity=discord.Activity(name='ESPORTS', type=discord.ActivityType.watching)) 
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event 
async def on_member_join(member):
    role = member.guild.get_role(857620432566878260)
    await member.add_roles(role)

@client.group(invoke_without_command=True)
async def help(ctx):
    icon = (ctx.guild.icon_url)
    
    embed = discord.Embed ( title='LIST OF COMMANDS', footer='USE HELP <command> FOR MORE HELP')
    embed.set_thumbnail(url=icon)
    embed.add_field(name = ":tools: MODERATION", value="`kick`,`ban`,`blacklist`")
    embed.add_field(name = ":dart: UTILITY", value="`ping`,`serverinfo`", inline=False)
    embed.set_footer(text="USE help <command> FOR MORE INFO")
    embed.colour = 0x00A2E8  
    await ctx.send (embed=embed)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member,*, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed ( description= f'***<:3333:869416291465850932> {member} HAS BEEN KICKED***')
    embed.colour = 0x00A2E8  
    await ctx.send(embed=embed)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member,*, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed ( description= f'***<:3333:869416291465850932> {member} HAS BEEN BANNED***')
    embed.colour = 0x00A2E8   
    await ctx.send(embed=embed)

@client.command(aliases=['ub'])
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name , member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed ( description= f'***<:3333:869416291465850932> {member} HAS BEEN UNBANNED***')
            embed.colour = 0x00A2E8   
            await ctx.send(embed=embed)
            return
            

@client.command(aliases=['bl'])
@commands.has_permissions(kick_members = True)
async def blacklist(ctx,member : discord.Member):
    blacklisted_role = ctx.guild.get_role(859466504851685416)
    await member.add_roles(blacklisted_role)
    embed = discord.Embed ( description= f'***<:3333:869416291465850932> {member} HAS BEEN BLACKLISTED***')
    embed.colour = 0x00A2E8    
    await ctx.send(embed=embed)

@client.command(aliases=['rbl'])
@commands.has_permissions(kick_members = True)
async def removeblacklist(ctx,member : discord.Member):
    removeblacklist_role = ctx.guild.get_role(859466504851685416)
    await member.remove_roles(removeblacklist_role)
    embed = discord.Embed ( description= f'***<:3333:869416291465850932> {member} HAS BEEN REMOVED OF BLACKLIST***')
    embed.colour = 0x00A2E8  
    await ctx.send(embed=embed)

@client.command(help = "Returns Latency")
async def ping(ctx):
    embed = discord.Embed ( description = f'***<:3333:869416291465850932> LATENCY IS {round(client.latency*1000)}ms***' )
    embed.colour = 0x00A2E8  
    await ctx.send (embed=embed)

@client.command()
async def serverinfo(ctx):
    role_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
    icon = (ctx.guild.icon_url)
    banner = ctx.guild.banner_url
    tcount= len(ctx.guild.text_channels)
    vcount= len(ctx.guild.voice_channels)

    embed = discord.Embed(timestamp= ctx.message.created_at, colour=0x00A2E8 )
    embed.set_thumbnail(url=icon)
    embed.set_image(url=banner) 
    embed.add_field(name="SERVER ID:-", value=f"{ctx.guild.id}", inline=False)
    embed.add_field(name="CREATED ON:-", value=f"{ctx.guild.created_at}", inline=False)
    embed.add_field(name="OWNER:-", value=f"<@{ctx.guild.owner_id}>", inline=False)
    embed.add_field(name="MEMBER COUNT:-", value=f"{ctx.guild.member_count}", inline=False)
    embed.add_field(name="TEXT CHANNEL COUNT:-", value=(tcount), inline=False) 
    embed.add_field(name="VOICE CHANNEL COUNT:-", value=(vcount), inline=False)   
    embed.add_field(name="VERIFICATION LEVEL:-", value=f"{ctx.guild.verification_level}", inline=False)
    
    await ctx.send (embed=embed)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('**NO COMMAND IS FOUND, USE** `help` **COMMAND FOR LIST OF COMMANDS**')

    if isinstance(error, commands.MissingPermissions):
        await ctx.send('**I DONT HAVE ENOUGH HIERARCHY TO DO THAT**')


client.run('-')




