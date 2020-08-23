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
from discord.ext import commands

class Owner_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Add Role Command
    @commands.command()
    @commands.has_any_role('Owner')
    async def addrole(self, ctx, member : discord.Member, *, role: discord.Role):
        await member.add_roles(role)
        await ctx.send(f"{member.mention} has been roled {role}.")

    @addrole.error
    async def addrole_error(self, ctx, error):
        if isinstance(error, (commands.MissingAnyRole)):
            await ctx.send(f"{ctx.author.mention} You are not allowed to use owner commands.")

    # Remove Role Command
    @commands.command()
    @commands.has_any_role('Owner')
    async def removerole(self, ctx, member : discord.Member, *, role: discord.Role):
        await member.remove_roles(role)
        await ctx.send(f"{member.mention} had {role} removed from their roles.")

    @removerole.error
    async def removerole_error(self, ctx, error):
        if isinstance(error, (commands.MissingAnyRole)):
            await ctx.send(f"{ctx.author.mention} You are not allowed to use owner commands.")

    # Fire Mods Command
    @commands.command()
    @commands.has_any_role('Owner')
    async def fire(self, ctx, member : discord.Member):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == "Moderator":
                await member.remove_roles(role)
                await ctx.send(f"{member.mention} has been fired from the moderation team.")

    @fire.error
    async def fire_error(self, ctx, error):
        if isinstance(error, (commands.MissingAnyRole)):
            await ctx.send(f"{ctx.author.mention} You are not allowed to use owner commands.")

    # Shutting Down Bot
    @commands.command()
    @commands.has_any_role('Owner')
    async def shutdown(self, ctx):
        await ctx.send(f"Shutting Down...")
        await self.bot.logout()

    @shutdown.error
    async def shutdown_error(self, ctx, error):
        if isinstance(error, (commands.MissingAnyRole)):
            await ctx.send(f"{ctx.author.mention} You are not allowed to use owner commands.")

    # Show Ban List with Reasons (Only in Terminal)
    @commands.command()
    @commands.has_any_role('Owner')
    async def banlist(self, ctx):
        bans = await ctx.guild.bans()
        print(bans)

    @banlist.error
    async def banlist_error(self, ctx, error):
        if isinstance(error, (commands.MissingAnyRole)):
            await ctx.send(f"{ctx.author.mention} You are not allowed to use owner commands.")

def setup(bot):
    bot.add_cog(Owner_Commands(bot))
    print("[owner_commands.py] has been loaded.")