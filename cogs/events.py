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

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    load_dotenv()

    # Confirmation That Bot Is Ready In Console.
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"\nLogged in as:")
        print(self.bot.user.name)
        print(self.bot.user.id)
        print(f'CiferBot is ready.\n')
        self.bot.start_time = dt.datetime.now()

    # Auto Assign Role and Greeting Message
    @commands.Cog.listener()
    async def on_member_join(self, member : discord.Member):
        role = discord.utils.get(member.guild.roles, name = "Fans") 
        await member.add_roles(role)
        greeting_channel = os.getenv('GREETINGS_CHANNEL')
        channel = self.bot.get_channel(int(greeting_channel))
        embed = discord.Embed( color = discord.Color(0x15f900), title = "Cifer's Server | User Joined", description = f"<:CiferLogo:490993466340540436>  Welcome to Cifer's Server {member.mention}! Enjoy!  <:CiferLogo:490993466340540436>")
        await channel.send(embed = embed)

    # Leave Message (Also checks for kicks or bans done the "Discord way".)
    @commands.Cog.listener()
    async def on_member_remove(self, user):
        greeting_channel = os.getenv('GREETINGS_CHANNEL')
        channel = self.bot.get_channel(int(greeting_channel))
        embed = discord.Embed( color = discord.Color(0xf60000), title = "Cifer's Server | User Left", description = f"<:CiferLogo:490993466340540436> Goodbye {user.mention}! You will be missed! <:CiferLogo:490993466340540436>")
        await channel.send(embed = embed)
        guild = user.guild
        async for entry in guild.audit_logs(limit = 1):
            reason = entry.reason
            logs_channel = os.getenv('MOD_LOGS')
            if entry.action == discord.AuditLogAction.kick:
                embed = discord.Embed(color = discord.Color(0xf60000), title = "Kick | Discord", description = f"{user.mention} has been kicked. Reason = {reason}")
                embed.set_footer(text = f"Action Used by {entry.user}")
                channel = self.bot.get_channel(int(logs_channel))
                await channel.send(embed = embed)
            elif entry.action == discord.AuditLogAction.ban:
                embed = discord.Embed(color = discord.Color(0xf60000), title = "Ban | Discord", description = f"{user.mention} has been banned. Reason = {reason}")
                embed.set_footer(text = f"Action Used by {entry.user}")
                channel = self.bot.get_channel(int(logs_channel))
                await channel.send(embed = embed)

    # Checks When Mods Unban Someone (the "Discord way".)
    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        async for entry in guild.audit_logs(limit = 1):
            if entry.action == discord.AuditLogAction.unban:
                embed = discord.Embed(color = discord.Color(0x15f900), title = "Unban | Discord", description = f"{user} has been unbanned.")
                embed.set_footer(text = f"Action Used by {entry.user}")
                logs_channel = os.getenv('MOD_LOGS')
                channel = self.bot.get_channel(int(logs_channel))
                await channel.send(embed = embed)

    # Changing nicknames of anyone who has Cifer as their name. (Anti-Impersonation Code)
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        guild = before.guild
        if before.top_role < guild.me.top_role:
            nn = after.nick
            if nn:
                if nn.count("Cifer") > 0 or nn.count("cifer") > 0 or nn.count("CIFER") > 0 or nn.count("CiferTTV") > 0 or nn.count("CiferYT") > 0 or nn.count("CiferHD") > 0:
                    last = before.nick
                    if last:
                        await after.edit(nick = last)
                    else:
                        await after.edit(nick = "Change Name.")

    # Command Not Found Event 
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            allowed_mention = discord.AllowedMentions(everyone = False, roles = False)
            await ctx.send(f"{ctx.author.mention} Command '{ctx.message.content}' not found. Please type a valid command.", allowed_mentions = allowed_mention)
        else:
            raise error

def setup(bot):
    bot.add_cog(Events(bot))
    print("[events.py] has been loaded.")