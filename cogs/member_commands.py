"""

Made by Cifer
    -> https://twitch.tv/CiferHD
    -> https://discord.gg/HEXssge

MIT License

Copyright (c) 2020 CiferHD

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

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