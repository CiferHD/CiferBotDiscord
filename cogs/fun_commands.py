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
import random
from discord.ext import commands

class Fun_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # 8Ball Command
    @commands.command(aliases = ['8ball'])
    async def reply(self, ctx, *, question):
        responses = ["It is certain.", 
        "It is decidedly so.", 
        "Without a doubt.", 
        "Yes - definetly.", 
        "You may rely on it.", 
        "As I see it, yes.", 
        "Most likely.", 
        "Outlook good.", 
        "Yes.", 
        "Signs point to yes.", 
        "Reply hazy, try again.", 
        "Ask again later.", 
        "Better not tell you now.",
        "Can't predict now.", 
        "Concentrate, and ask again.", 
        "Don't count on it.", 
        "My reply is no.", 
        "My sources say no.", 
        "Outlook not so good.", 
        "Very doubtful."]

        allowed_mention = discord.AllowedMentions(everyone = False, roles = False)
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}", allowed_mentions = allowed_mention)

    @reply.error
    async def reply_error(self, ctx, error):
        if isinstance(error, (commands.MissingRequiredArgument)):
            await ctx.send(f"{ctx.author.mention} You did not ask a question. Try: `;8ball <question>`.")

    # Memes Command
    @commands.command(aliases = ['meme'])
    async def respond(self, ctx):
        sendback = ["https://gph.is/1UTvraD", 
        "https://gph.is/1UTCxMn",
        "https://gph.is/1Tbo3rJ",
        "https://gph.is/1TUDOBo",
        "https://gph.is/1nLiiFG",
        "https://gph.is/1X84en7",
        "https://gph.is/1YNavFn",
        "https://gph.is/1QpzoFx",
        "https://gph.is/1RuoP2g",
        "When you meet with the bois: https://gph.is/2dq9ijA",
        "Launching to space in 3.... 2..... https://gph.is/2NXyKPM",
        "Well, hello there! https://gph.is/2ynW7yl",
        "https://gph.is/2n1VsfF",
        "YEET! https://gph.is/1aRALFv",
        "https://giphy.com/gifs/1wqqlaQ7IX3TXibXZE",
        "https://giphy.com/gifs/hQKiGV6MG8WmsHg2yx",
        "https://giphy.com/gifs/JdJuKpEQAw1rO",
        "https://giphy.com/gifs/h2kaUZAxx7y9uYPJfS",
        "https://giphy.com/gifs/1oSK9Etm2edMCMSnGZ",
        "https://giphy.com/gifs/l41lH04BS64jkWA9O"]

        await ctx.send(f"{random.choice(sendback)}")

    # Coinflip Command
    @commands.command(aliases = ['coinflip'])
    async def flipcoin(self, ctx, *, guess):
        choices = ['Heads', 'Tails']
        bot_choice = random.choice(choices)

        if guess.lower() == "heads":
            embed = discord.Embed(color = discord.Color(0xFFD700), title = "Coin Flip", description = " ")
            embed.add_field(name = "User's Choice", value = f"{guess}", inline = True)
            embed.add_field(name = "Bot's Choice", value = f"{bot_choice}", inline = True)
            await ctx.send(embed = embed)
        elif guess.lower() == "tails":
            embed = discord.Embed(color = discord.Color(0xFFD700), title = "Coin Flip", description = " ")
            embed.add_field(name = "User's Choice", value = f"{guess}", inline = True)
            embed.add_field(name = "Bot's Choice", value = f"{bot_choice}", inline = True)
            await ctx.send(embed = embed)
        else:
            await ctx.send(f"{ctx.author.mention} Please guess using heads or tails.")

    @flipcoin.error
    async def flipcoin_error(self, ctx, error):
        if isinstance(error, (commands.MissingRequiredArgument)):
            await ctx.send(f"{ctx.author.mention} Be sure to guess! Heads or Tails? Try: `;coinflip <guess>`.")

    # Random Number Chooser Command
    @commands.command()
    async def numchooser(self, ctx):
        num = random.randint(0, 100)
        await ctx.send(f"{ctx.author.mention} The number that has been chosen is {num}.")

    # Rock Paper Scissors Command
    @commands.command()
    async def rps(self, ctx, *, player_input):
        choices = ['Rock', 'Paper', 'Scissors']
        bot_input = random.choice(choices)

        if player_input.lower() == bot_input.lower():
            embed = discord.Embed(title = "Rock, Paper, Scissors", description = " ")
            embed.add_field(name = "User's Choice", value = f"{player_input}", inline = True)
            embed.add_field(name = "Bot's Choice", value = f"{bot_input}", inline = True)
            embed.add_field(name = "Result", value = "Tie!") 
            await ctx.send(embed = embed)
        elif player_input.lower() == "rock" and bot_input.lower() == "scissors":
            embed = discord.Embed(title = "Rock, Paper, Scissors", description = " ")
            embed.add_field(name = "User's Choice", value = f"{player_input}")
            embed.add_field(name = "Bot's Choice", value = f"{bot_input}")
            embed.add_field(name = "Result", value = "You win! :)")
            await ctx.send(embed = embed)
        elif player_input.lower() == "scissors" and bot_input.lower() == "rock":
            embed = discord.Embed(title = "Rock, Paper, Scissors", description = " ")
            embed.add_field(name = "User's Choice", value = f"{player_input}", inline = True)
            embed.add_field(name = "Bot's Choice", value = f"{bot_input}", inline = True)
            embed.add_field(name = "Result", value = "You lose.")
            await ctx.send(embed = embed)
        elif player_input.lower() == "paper" and bot_input.lower() == "rock":
            embed = discord.Embed(title = "Rock, Paper, Scissors", description = " ")
            embed.add_field(name = "User's Choice", value = f"{player_input}", inline = True)
            embed.add_field(name = "Bot's Choice", value = f"{bot_input}", inline = True)
            embed.add_field(name = "Result", value = "You win! :)")
            await ctx.send(embed = embed)
        elif player_input.lower() == "rock" and bot_input.lower() == "paper":
            embed = discord.Embed(title = "Rock, Paper, Scissors", description = " ")
            embed.add_field(name = "User's Choice", value = f"{player_input}", inline = True)
            embed.add_field(name = "Bot's Choice", value = f"{bot_input}", inline = True)
            embed.add_field(name = "Result", value = "You lose.")
            await ctx.send(embed = embed)
        elif player_input.lower() == "scissors" and bot_input.lower() == "paper":
            embed = discord.Embed(title = "Rock, Paper, Scissors", description = " ")
            embed.add_field(name = "User's Choice", value = f"{player_input}", inline = True)
            embed.add_field(name = "Bot's Choice", value = f"{bot_input}", inline = True)
            embed.add_field(name = "Result", value = "You win! :)")
            await ctx.send(embed = embed)
        elif player_input.lower() == "paper" and bot_input.lower() == "scissors":
            embed = discord.Embed(title = "Rock, Paper, Scissors", description = " ")
            embed.add_field(name = "User's Choice", value = f"{player_input}", inline = True)
            embed.add_field(name = "Bot's Choice", value = f"{bot_input}", inline = True)
            embed.add_field(name = "Result", value = "You lose.")
            await ctx.send(embed = embed)
        else:
            await ctx.send(f"{ctx.author.mention} Be sure to choose an option. Rock, Paper, or Scissors?")

    @rps.error
    async def rps_error(self, ctx, error):
        if isinstance(error, (commands.MissingRequiredArgument)):
            await ctx.send(f"{ctx.author.mention} Be sure to choose an option. Rock, Paper, or Scissors? Try: `;rps <option>`.")

def setup(bot):
    bot.add_cog(Fun_Commands(bot))
    print("[fun_commands.py] has been loaded.")