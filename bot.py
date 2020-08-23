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

