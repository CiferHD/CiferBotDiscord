"""

Made by Cifer
    -> https://twitch.tv/CiferHD
    -> https://discord.gg/HEXssge

MIT License

Copyright (c) 2020 CiferHD
Refer to LICENSE for more information.

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