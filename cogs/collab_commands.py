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

class Collab_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    collab_name = "" # Name Format: Name's

    @commands.command()
    async def ctwitch(self, ctx, collab_name):
        await ctx.send(f"{collab_name} Twitch: https://twitch.tv/")

    @commands.command()
    async def cyoutube(self, ctx, collab_name):
        await ctx.send(f"{collab_name} YouTube: ")

    @commands.command()
    async def ctwitter(self, ctx, collab_name):
        await ctx.send(f"{collab_name} Twitter: ")

    @commands.command()
    async def cinstagram(self, ctx, collab_name):
        await ctx.send(f"{collab_name} Instagram: https://instagram.com/")

    @commands.command()
    async def cdiscord(self, ctx, collab_name):
        await ctx.send(f"{collab_name} Discord Server: ")

def setup(bot):
    bot.add_cog(Collab_Commands(bot))
    print("[collab_commands.py] has been loaded.")