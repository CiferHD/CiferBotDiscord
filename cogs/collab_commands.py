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