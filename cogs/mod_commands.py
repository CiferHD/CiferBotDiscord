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
import typing
import os
from dotenv import load_dotenv
from discord.ext import commands

class Mod_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    load_dotenv()

    # Kick Command
    @commands.command()
    @commands.has_any_role('Owner', 'Moderator')
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : typing.Optional[discord.Member], *, reason = None):
        if member is None:
            embed = discord.Embed(color = discord.Color(0xf60000), title = "Kick", description = """
            `;kick <member> <reason>`

            This command is used to kick people out of the server.
            """)
            await ctx.send(embed = embed)

        guild = ctx.guild
        logs_channel = os.getenv('MOD_LOGS')
        mod_id = os.getenv('MOD_ID')
        if member.top_role < guild.get_role(int(mod_id)):
            await member.kick(reason = reason)
            embed = discord.Embed(color = discord.Color(0xf60000), title = "Kick", description = f"{member.mention} has been kicked. Reason = {reason}")
            embed.set_footer(text = f"Command Used by {ctx.author}")
            channel = self.bot.get_channel(int(logs_channel))
            await channel.send(embed = embed)
            await ctx.send(f"{member.mention} has been kicked from the server. Reason = {reason}")
            return

    # You're not a mod! (Error Handling for Kick Command ^^) 
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, (commands.MissingPermissions, commands.MissingAnyRole)):
            await ctx.send(f"{ctx.author.mention} You are not allowed to use moderation commands.")

    # Ban Command
    @commands.command()
    @commands.has_any_role('Owner', 'Moderator')
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : typing.Optional[discord.Member], *, reason = None):
        if member is None:
            embed = discord.Embed(color = discord.Color(0xf60000), title = "Ban", description = """
            `;ban <member> <reason>`

            This command is used to ban people from the server.
            """)
            await ctx.send(embed = embed)

        guild = ctx.guild
        logs_channel = os.getenv('MOD_LOGS')
        mod_id = os.getenv('MOD_ID')
        if member.top_role < guild.get_role(int(mod_id)):
            await member.ban(reason = reason)
            embed = discord.Embed(color = discord.Color(0xf60000), title = "Ban", description = f"{member.mention} has been banned. Reason = {reason}")
            embed.set_footer(text = f"Command Used by {ctx.author}")
            channel = self.bot.get_channel(int(logs_channel))
            await channel.send(embed = embed)
            await ctx.send(f"{member.mention} has been banned from the server. Reason = {reason}")
            return

    # You're not a mod! (Error Handling for Ban Command ^^) 
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, (commands.MissingPermissions, commands.MissingAnyRole)):
            await ctx.send(f"{ctx.author.mention} You are not allowed to use moderation commands.")

    # Unban Command
    @commands.command()
    @commands.has_any_role('Owner', 'Moderator')
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(color = discord.Color(0x15f900), title = "Unban", description = f"{member} has been unbanned.")
                embed.set_footer(text = f"Command Used by {ctx.author}")
                logs_channel = os.getenv('MOD_LOGS')
                channel = self.bot.get_channel(int(logs_channel))
                await channel.send(embed = embed)
                await ctx.send(f"{member} has been unbanned from the server.")

    # You're not a mod! (Error Handling for Unban Command ^^) 
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, (commands.MissingPermissions, commands.MissingAnyRole)):
            await ctx.send(f"{ctx.author.mention} You are not allowed to use moderation commands.")

    # Talk Through Bot Command
    @commands.command()
    @commands.has_any_role('Owner', 'Moderator')
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(f"{msg}")
        embed = discord.Embed(color = discord.Color(0x15f900), title = "Say", description = f"{ctx.author.mention} has used the say command. Message: {msg}")
        logs_channel = os.getenv('MOD_LOGS')
        channel = self.bot.get_channel(int(logs_channel))
        await channel.send(embed = embed)

    # You're not a mod! (Error Handling for Say Command ^^) 
    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, (commands.MissingPermissions, commands.MissingAnyRole)):
            await ctx.send(f"{ctx.author.mention} You are not allowed to use moderation commands.")

    # Purge Command
    @commands.command()
    @commands.has_any_role('Owner', 'Moderator')
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, amount = 10):
        await ctx.message.delete()
        await ctx.channel.purge(limit = amount)

    # You're not a mod! (Error Handling for Purge Command ^^) 
    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, (commands.MissingPermissions, commands.MissingAnyRole)):
            await ctx.send(f"{ctx.author.mention} You are not allowed to use moderation commands.")

    # Mute Command
    @commands.command()
    @commands.has_any_role('Owner', 'Moderator')
    @commands.has_permissions(manage_messages = True)
    async def mute(self, ctx, member : typing.Optional[discord.Member], *, reason = None):
        if member is None:
            embed = discord.Embed(color = discord.Color(0xfcba03), title = "Mute", description = """
            `;mute <member> <reason>`

            This command is used to prohibit people from talking in normal chats and voice chats.
            """)
            await ctx.send(embed = embed)

        guild = ctx.guild
        logs_channel = os.getenv('MOD_LOGS')
        for role in guild.roles:
            if role.name == "Muted":
                await member.add_roles(role)
            if role.name == "DJ":
                await member.remove_roles(role)
                embed = discord.Embed(color = discord.Color(0xfcba03), title = "Mute", description = f"{member.mention} has been muted. Reason = {reason}")
                embed.set_footer(text = f"Command Used by {ctx.author}")
                channel = self.bot.get_channel(int(logs_channel))
                await channel.send(embed = embed)
                await ctx.send(f"{member.mention} has been muted. Reason = {reason}")
                return

    # You're not a mod! (Error Handling for Mute Command ^^) 
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, (commands.MissingPermissions, commands.MissingAnyRole)):
            await ctx.send(f"{ctx.author.mention} You are not allowed to use moderation commands.")

    @commands.command()
    @commands.has_any_role('Owner', 'Moderator')
    @commands.has_permissions(manage_messages = True)
    async def unmute(self, ctx, member : typing.Optional[discord.Member]):
        if member is None:
            embed = discord.Embed(color = discord.Color(0xfcba03), title = "Unmute", description = """
            `;unmute <member>`

            This command is used to allow people to talk in normal chats and voice chats after serving their mute time.
            """)
            await ctx.send(embed = embed)

        guild = ctx.guild
        logs_channel = os.getenv('MOD_LOGS')
        for role in guild.roles:
            if role.name == "Muted":
                await member.remove_roles(role)
                embed = discord.Embed(color = discord.Color(0xfcba03), title = "Unmute", description = f"{member.mention} has been un-muted.")
                embed.set_footer(text = f"Command Used by {ctx.author}")
                channel = self.bot.get_channel(int(logs_channel))
                await channel.send(embed = embed)
                await ctx.send(f"{member.mention} has been unmuted.")
                return

    # You're not a mod! (Error Handling for Unmute Command ^^) 
    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, (commands.MissingPermissions, commands.MissingAnyRole)):
            await ctx.send(f"{ctx.author.mention} You are not allowed to use moderation commands.")

def setup(bot):
    bot.add_cog(Mod_Commands(bot))
    print("[mod_commands.py] has been loaded.")