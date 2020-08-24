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

class Display_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Command Categories
    @commands.command(aliases = ['help'])
    async def cmds(self, ctx):
        embed = discord.Embed(color = discord.Color(0x0000CC), title = "Commands", description = "Here are the categories of commands. Be sure to read the descriptions!")
        embed.add_field(name = "Member Commands", value = "These command can be used by anyone. To look at a list of these commands, type `;cmdsmember` in chat.", inline = True)
        embed.add_field(name = "Fun Commands", value = "These command can be used by anyone. To look at a list of these commands, type `;cmdsfun` in chat.", inline = True)
        embed.add_field(name = "Economy Commands", value = "These commands can be used by anyone. To look at a list of these commands, type `;cmdseco` in chat.", inline = True)
        embed.add_field(name = "Moderator Commands", value = "These command can be used by moderators only. To look at a list of these commands, type `;cmdsmod` in chat.", inline = True)
        await ctx.send(embed = embed)

    # Member Commands
    @commands.command()
    async def cmdsmember(self, ctx):
        embed = discord.Embed(color = discord.Color(0x0000CC), title = "Member Commands", description = " ")
        embed.add_field(name = ";support", value = "This command will create a private chat in this server with the moderation team. Must only be used for problems or questions relating to the server.", inline = True)
        embed.add_field(name = ";uptime", value = "This command will tell you the amount of time that the bot has been running for.", inline = True)
        embed.add_field(name = ";prefix", value = "This command tells you the prefix used for this bot.", inline = True)
        embed.add_field(name = ";ping", value = "This command tells you the latency of the bot.", inline = True)
        embed.add_field(name = ";github", value = "This command will send the link to my GitHub account.", inline = True)
        embed.add_field(name = ";youtube", value = "This command will send the link to my YouTube channel. Be sure to subscribe! :)", inline = True)
        embed.add_field(name = ";twitch", value = "This command will send the link to my Twitch channel. Be sure to follow! :)", inline = True)
        embed.add_field(name = ";instagram", value = "This command will send the link to my Instagram account. Be sure to follow! :)", inline = True)
        embed.add_field(name = ";invite", value = "This command will send a link to this server that you can use to invite your friends.", inline = True)
        embed.add_field(name = ";members", value = "This command will tell you the amount of people there are in the server.", inline = True)
        await ctx.send(embed = embed)

    # Fun Commands
    @commands.command()
    async def cmdsfun(self, ctx):
        embed = discord.Embed(color = discord.Color(0x0000CC), title = "Fun Commands", description = " ")
        embed.add_field(name = ";8ball", value = "This command is a virutal magic 8 ball that is used for fortune telling or seeking advice.", inline = True)
        embed.add_field(name = ";meme", value = "This command will make you laugh. Memes are added to the bot everyday.", inline = True)
        embed.add_field(name = ";coinflip", value = "This command is a virtual coin flip.", inline = True)
        embed.add_field(name = ";numchooser", value = "This command will give you a number that is between 1-100.", inline = True)
        embed.add_field(name = ";rps", value = "This command will let you play 'Rock, Paper, Scissors' with the bot!", inline = True)
        await ctx.send(embed = embed)

    # Economy Commands
    @commands.command()
    async def cmdseco(self, ctx):
        embed = discord.Embed(color = discord.Color(0x0000CC), title = "Economy Commands", description = " ")
        embed.add_field(name = ";open_account", value = "This command will allow you to create an account in CiferEconomy.", inline = True)
        embed.add_field(name = ";balance", value = "This command will show you the amount of money that you have in your wallet and bank account.", inline = True)
        embed.add_field(name = ";deposit", value = "This command will transfer the specified amount of money from your wallet into your bank account.", inline = True)
        embed.add_field(name = ";withdraw", value = "This command will transfer the specified amount of money from your bank account into your wallet.", inline = True)
        embed.add_field(name = ";transfer", value = "This command will securely transfer the specified amount of money from your bank account to another member's bank account.", inline = True)
        embed.add_field(name = ";donate", value = "This command will give the specified amount of money from your wallet to another member's wallet.", inline = True)
        embed.add_field(name = ";work", value = "This command will allow you to work and make money legally! The money that you earn will be put into your wallet.", inline = True)
        embed.add_field(name = ";rob", value = "This command will allow you to make money illegally. The money that you earn will be put into your wallet.", inline = True)
        embed.add_field(name = ";steal", value = "This command will allow you to steal money from other members! The money that you earn will be put into your wallet.", inline = True)
        await ctx.send(embed = embed)

    # Moderator Commands
    @commands.command()
    async def cmdsmod(self, ctx):
        embed = discord.Embed(color = discord.Color(0x0000CC), title = "Moderator Commands", description = " ")
        embed.add_field(name = ";purge", value = "This command helps to delete multiple messages at one time.", inline = True)
        embed.add_field(name = ";mute", value = "This command is used to prohibit people from talking in normal chats and voice chats.", inline = True)
        embed.add_field(name = ";unmute", value = "This command is used to allow people to talk in normal chats and voice chats after serving their mute time.", inline = True)
        embed.add_field(name = ";kick", value = "This command is used to kick people out of the server.", inline = True)
        embed.add_field(name = ";ban", value = "This command is used to ban people from the server.", inline = True)
        embed.add_field(name = ";unban", value = "This command is used to unban people who were banned.", inline = True)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Display_Commands(bot))
    print("[display_commands.py] has been loaded.")