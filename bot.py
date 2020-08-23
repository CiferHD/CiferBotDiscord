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
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

bot = commands.Bot(command_prefix = ';', activity = discord.Activity(type = discord.ActivityType.watching, name = "over Cifer's Sever!"), case_insensitive = True)

bot.remove_command('help')

@bot.command()
@commands.has_any_role('Owner')
async def push(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send("[L]: Extension has been pushed successfully.")

@push.error
async def push_error(ctx, error):
    if isinstance(error, (commands.MissingAnyRole)):
        await ctx.send(f"{ctx.author.mention} You are not allowed to use owner commands.")

@bot.command()
@commands.has_any_role('Owner')
async def fork(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send("[U]: Extension has been unloaded successfully.")
    print(f"[U]: {extension} has been unloaded/forked successfully.")

@fork.error
async def fork_error(ctx, error):
    if isinstance(error, (commands.MissingAnyRole)):
        await ctx.send(f"{ctx.author.mention} You are not allowed to use owner commands.")

@bot.command()
@commands.has_any_role('Owner')
async def pull(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send("[R]: Extension has been uploaded successfully.")

@pull.error
async def pull_error(ctx, error):
    if isinstance(error, (commands.MissingAnyRole)):
        await ctx.send(f"{ctx.author.mention} You are not allowed to use owner commands.")

path = os.getenv('PATH_TO_FILE')
for filename in os.listdir(path):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# Bot Run
token = os.getenv('BOT_TOKEN')
bot.run(token)

