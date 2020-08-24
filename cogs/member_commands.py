"""

Made by Cifer
    -> https://twitch.tv/CiferHD
    -> https://discord.gg/HEXssge

MIT License

Copyright (c) 2020 CiferHD
Refer to LICENSE for more information.

"""

import discord
import os
import datetime as dt
from dotenv import load_dotenv
from discord.ext import commands

class Member_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    load_dotenv()

    # Support Command
    @commands.command()
    @commands.cooldown(1, 600, commands.BucketType.user)
    async def support(self, ctx):
        guild = ctx.guild
        mod_id = os.getenv('MOD_ID')
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages = False),
            guild.get_role(int(mod_id)): discord.PermissionOverwrite(read_messages = True),
            ctx.author: discord.PermissionOverwrite(read_messages = True)
    }

        await ctx.send(f"{ctx.author.mention} Your ticket has been created.")
        channel = await guild.create_text_channel(f"Support = {ctx.author}", overwrites = overwrites)
        await channel.send(f"{ctx.author.mention}. One of the members from the {guild.get_role(int(mod_id)).mention} team will be with you soon.")

    @support.error
    async def support_eror(self, ctx, error):
        if isinstance(error, (commands.CommandOnCooldown)):
            time_remaining = error.retry_after / 60
            await ctx.send(f"{ctx.author.mention} You are currently on cooldown for this command. Time Remaining: {time_remaining:.2f} minutes.")

    # Uptime Command
    @commands.command()
    async def uptime(self, ctx):
        current_time = dt.datetime.now()
        time = int((current_time - self.bot.start_time).total_seconds())
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        await ctx.send(f"{ctx.author.mention} The bot has been up for {hours:d}:{minutes:02d}:{seconds:02d}. (Format: HOURS : MINUTES : SECONDS)")

    # Prefix Command
    @commands.command()
    async def prefix(self, ctx):
        await ctx.send(f"{ctx.author.mention} The prefix for this bot is ; (semi-colon).")

    # Ping Command
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{ctx.author.mention}   :ping_pong:   Pong! The bot's latency is {round(self.bot.latency * 1000)}ms.")

    # GitHub Command
    @commands.command()
    async def github(self, ctx):
        await ctx.send(f"{ctx.author.mention} Cifer's GitHub: https://github.com/CiferHD")

    # Twitch Command
    @commands.command()
    async def twitch(self, ctx):
        await ctx.send(f"{ctx.author.mention} Cifer's Twitch: https://twitch.tv/CiferHD")

    # YouTube Command
    @commands.command()
    async def youtube(self, ctx):
        await ctx.send(f"{ctx.author.mention} Cifer's YouTube: https://www.youtube.com/channel/UC5FXU2hW9fRPHyU32mvBLjw?subconfirmation=1")

    # Instagram Commnad
    @commands.command()
    async def instagram(self, ctx):
        await ctx.send(f"{ctx.author.mention} Cifer's Instagram: https://www.instagram.com/ciferhd")

    # Discord Server Invite Command
    @commands.command()
    async def invite(self, ctx):
        await ctx.send(f"{ctx.author.mention} You can invite your friends to this server by using: https://discord.gg/HEXssge")

    # Amount of Members Command
    @commands.command()
    async def members(self, ctx):
        guild = ctx.guild
        await ctx.send(f"{ctx.author.mention} The server has {len(guild.members)} members!")

def setup(bot):
    bot.add_cog(Member_Commands(bot))
    print("[member_commands.py] has been loaded.")