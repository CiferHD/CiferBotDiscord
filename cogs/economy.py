"""

Made by Cifer
    -> https://twitch.tv/CiferHD
    -> https://discord.gg/HEXssge

MIT License

Copyright (c) 2020 CiferHD
Refer to LICENSE for more information.

"""

import discord
import random
import json
import os
import typing
import asyncio
from discord.ext import commands

class PositiveInt(commands.Converter):
        async def convert(self, ctx, amount: str):
            value = int(amount)
            if value < 0:
                await ctx.send(f"{ctx.author.mention} You must use a positive integer.")
                raise ValueError(f"Argument must be positive!")
            return value

class Economy_System(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.user_lock = False

    path = os.getenv('PATH_TO_FILE')
    os.chdir(path)

    async def get_bank_data(self):
        while self.user_lock:
            await asyncio.sleep(0.1)

        self.user_lock = True
        with open("bank.json", "r") as f:
            users = json.load(f)
        return users

    async def dump_data(self, users):
        with open("bank.json", "w") as f:
            json.dump(users, f, indent = 2, separators = (',', ': '))
        self.user_lock = False

    @commands.command()
    @commands.has_any_role('Owner')
    async def give(self, ctx, member : discord.Member, *, amount: PositiveInt):

        users = await self.get_bank_data()

        if str(member.id) not in users:
            await ctx.send(f"[{ctx.author.mention}] {member.mention} has not created an account yet. He/She can do this by using this command: `;open_account`.")

        users[str(member.id)]["Wallet"] += amount
        await ctx.send(f"{ctx.author.mention} has given {member.mention} ${amount}!")

        await self.dump_data(users)

    @give.error
    async def give_error(self, ctx, error):
        if isinstance(error, (commands.MissingAnyRole)):
            await ctx.send(f"{ctx.author.mention} You are not allowed to use owner commands.")

    @commands.command()
    @commands.has_any_role('Owner')
    async def remove(self, ctx, member : discord.Member, *, amount: PositiveInt):

        users = await self.get_bank_data()

        if str(member.id) not in users:
            await ctx.send(f"[{ctx.author.mention}] {member.mention} has not created an account yet. He/She can do this by using this command: `;open_account`.")

        users[str(member.id)]["Wallet"] -= amount
        await ctx.send(f"{ctx.author.mention} has removed ${amount} from {member.mention}'s account.")

        await self.dump_data(users)

    @remove.error
    async def remove_error(self, ctx, error):
        if isinstance(error, (commands.MissingAnyRole)):
            await ctx.send(f"{ctx.author.mention} You are not allowed to use owner commands.")

    @commands.command()
    async def open_account(self, ctx):

        users = await self.get_bank_data()

        if str(ctx.author.id) in users:
            await ctx.send(f"{ctx.author.mention} You already have an account opened! To check your balance, use this command: `;balance`.")
        else:
            users[str(ctx.author)] = {}
            users[str(ctx.author.id)] = {}
            users[str(ctx.author.id)]["Wallet"] = 0
            users[str(ctx.author.id)]["Bank"] = 50
            await ctx.send(f"{ctx.author.mention} Your account has been created!")

        await self.dump_data(users)

    @commands.command(aliases = ['bal'])
    async def balance(self, ctx, member : typing.Optional[discord.Member]):

        users = await self.get_bank_data()

        if str(ctx.author.id) not in users:
            await ctx.send(f"{ctx.author.mention} You need to create an account. You can do this by using this command: `;open_account`.")

        if member is None:
            member = ctx.author
            wallet_amount = users[str(member.id)]["Wallet"]
            bank_amount = users[str(member.id)]["Bank"]
            embed = discord.Embed(color = discord.Color(0xFFD700), title = f"{member.name}'s Account", description = " ")
            embed.add_field(name = "Wallet", value = f"${wallet_amount}")
            embed.add_field(name = "Bank Account", value = f"${bank_amount}")
            await ctx.send(embed = embed)
        elif str(member.id) not in users:
            await ctx.send(f"{ctx.author.mention} The person who you are trying to find the balance of does not have an account.")
        else:
            wallet_amount = users[str(member.id)]["Wallet"]
            bank_amount = users[str(member.id)]["Bank"]
            embed = discord.Embed(color = discord.Color(0xFFD700), title = f"{member.name}'s Account", description = " ")
            embed.add_field(name = "Wallet", value = f"${wallet_amount}")
            embed.add_field(name = "Bank Account", value = f"${bank_amount}")
            await ctx.send(embed = embed)

        await self.dump_data(users)

    @commands.command(aliases = ['dep'])
    async def deposit(self, ctx, *, amount: PositiveInt):

        users = await self.get_bank_data()

        if str(ctx.author.id) not in users:
            await ctx.send(f"{ctx.author.mention} You need to create an account. You can do this by using this command: `;open_account`.")

        if users[str(ctx.author.id)]["Wallet"] >= amount:
            users[str(ctx.author.id)]["Wallet"] -= amount
            users[str(ctx.author.id)]["Bank"] += amount
            await ctx.send(f"{ctx.author.mention} ${amount} has been deposited into your account!")
        elif users[str(ctx.author.id)]["Wallet"] < amount:
            await ctx.send(f"{ctx.author.mention} You do not have enough money to deposit this amount.")

        await self.dump_data(users)

    @deposit.error
    async def deposit_error(self, ctx, error):
        if isinstance(error, (commands.MissingRequiredArgument)):
            await ctx.send(f"{ctx.author.mention} Make sure to enter an amount. Try: `;deposit <amount>`.")

    @commands.command(aliases = ['with'])
    async def withdraw(self, ctx, *, amount: PositiveInt):

        users = await self.get_bank_data()

        if str(ctx.author.id) not in users:
            await ctx.send(f"{ctx.author.mention} You need to create an account. You can do this by using this command: `;open_account`.")

        if users[str(ctx.author.id)]["Bank"] >= amount:
            users[str(ctx.author.id)]["Bank"] -= amount
            users[str(ctx.author.id)]["Wallet"] += amount
            await ctx.send(f"{ctx.author.mention} ${amount} has been withdrawn from your account!")
        elif users[str(ctx.author.id)]["Bank"] < amount:
            await ctx.send(f"{ctx.author.mention} You do not have enough money to withdraw this amount.")

        await self.dump_data(users)

    @withdraw.error
    async def withdraw_error(self, ctx, error):
        if isinstance(error, (commands.MissingRequiredArgument)):
            await ctx.send(f"{ctx.author.mention} Make sure to enter an amount. Try: `;withdraw <amount>`.")

    @commands.command()
    async def donate(self, ctx, member : discord.Member, *, amount: PositiveInt):

        users = await self.get_bank_data()

        if str(ctx.author.id) not in users:
            await ctx.send(f"{ctx.author.mention} You need to create an account. You can do this by using this command: `;open_account`.")

        if str(member.id) not in users:
            await ctx.send(f"{ctx.author.mention} The person who you are trying to donate to does not have an active account.")
        elif users[str(ctx.author.id)]["Wallet"] >= amount:
            users[str(ctx.author.id)]["Wallet"] -= amount
            users[str(member.id)]["Wallet"] += amount
            await ctx.send(f"{ctx.author.mention} has donated ${amount} to {member.mention}!")
        elif users[str(ctx.author.id)]["Wallet"] < amount:
            await ctx.send(f"{ctx.author.mention} You do not have enough money to donate to {member.mention}.")

        await self.dump_data(users)

    @donate.error
    async def donate_error(self, ctx, error):
        if isinstance(error, (commands.MissingRequiredArgument)):
            await ctx.send(f"{ctx.author.mention} Make sure to enter the correct arguments. Try: `;donate <member> <amount>`.")

    @commands.command()
    async def transfer(self, ctx, member : discord.Member, *, amount: PositiveInt):

        users = await self.get_bank_data()

        if str(ctx.author.id) not in users:
            await ctx.send(f"{ctx.author.mention} You need to create an account. You can do this by using this command: `;open_account`.")

        if str(member.id) not in users:
            await ctx.send(f"{ctx.author.mention} The person who you are trying to e-transfer to does not have an active account.")
        elif users[str(ctx.author.id)]["Bank"] >= amount:
            users[str(ctx.author.id)]["Bank"] -= amount
            users[str(member.id)]["Bank"] += amount
            await ctx.send(f"{ctx.author.mention} has e-tranferred ${amount} to {member.mention}!")
        elif users[str(ctx.author.id)]["Bank"] < amount:
            await ctx.send(f"{ctx.author.mention} You do not have enough money to e-transfer in your account to {member.mention}.")

        await self.dump_data(users)

    @transfer.error
    async def transfer_error(self, ctx, error):
        if isinstance(error, (commands.MissingRequiredArgument)):
            await ctx.send(f"{ctx.author.mention} Make sure to enter the correct arguments. Try: `;transfer <member> <amount>`.")

    @commands.command()
    @commands.cooldown(5, 300, commands.BucketType.user)
    async def work(self, ctx):

        users = await self.get_bank_data()

        if str(ctx.author.id) not in users:
            await ctx.send(f"{ctx.author.mention} You need to create an account. You can do this by using this command: `;open_account`.")

        profit = random.randint(1, 101)
        working = [
            f"{ctx.author.mention} helped someone to fix a broken door, and got paid ${profit}!",
            f"{ctx.author.mention} painted a wall and got paid ${profit}!",
            f"{ctx.author.mention} streamed on Twitch and earned ${profit}!"]
        users[str(ctx.author.id)]["Wallet"] += profit
        await ctx.send(random.choice(working))

        await self.dump_data(users)

    @work.error
    async def work_eror(self, ctx, error):
        if isinstance(error, (commands.CommandOnCooldown)):
            time_remaining = error.retry_after / 60
            await ctx.send(f"{ctx.author.mention} You are currently on cooldown for this command. Time Remaining: {time_remaining:.2f} minutes.")

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def steal(self, ctx, member : discord.Member, *, amount: PositiveInt):

        users = await self.get_bank_data()

        if str(ctx.author.id) not in users:
            await ctx.send(f"{ctx.author.mention} You need to create an account. You can do this by using this command: `;open_account`.")
        elif str(member.id) not in users:
            await ctx.send(f"{ctx.author.mention} The person who you are trying to steal from does not have an active account.")

        bot_choices = ['Yes', 'Caught', 'No']
        randomChoice = random.choice(bot_choices)
        loss = random.randint(1, 501)

        if ctx.author == member:
            await ctx.send(f"{ctx.author.mention} You silly! Why you trying to steal from yourself? What a goof! :D")
            await ctx.send("https://media.discordapp.net/attachments/632249312101007374/742510339656122428/bub.gif")
        elif amount > users[str(member.id)]["Wallet"]:
            await ctx.send(f"{ctx.author.mention} The person who you are trying to steal from does not have the amount of money that you want.")
        elif randomChoice == "Yes":
            users[str(member.id)]["Wallet"] -= amount
            users[str(ctx.author.id)]["Wallet"] += amount
            await ctx.send(f"{ctx.author.mention} has stolen ${amount} from {member.mention}'s wallet!")
        elif randomChoice == "Caught":
            users[str(ctx.author.id)]["Wallet"] -= loss
            await ctx.send(f"{ctx.author.mention} was caught trying to steal money from {member.mention}! His fine: ${loss}.")
        elif randomChoice == "No":
            await ctx.send(f"{ctx.author.mention} tried to steal from {member.mention}, but got nothing.")

        await self.dump_data(users)

    @steal.error
    async def steal_eror(self, ctx, error):
        if isinstance(error, (commands.CommandOnCooldown)):
            time_remaining = error.retry_after
            await ctx.send(f"{ctx.author.mention} You are currently on cooldown for this command. Time Remaining: {time_remaining:.2f} seconds.")
        elif isinstance(error, (commands.MissingRequiredArgument)):
            await ctx.send(f"{ctx.author.mention} Who would you like to steal from? Try: `;steal <member> <amount>`.")
        elif isinstance(error, (commands.BadArgument)):
            await ctx.send(f"{ctx.author.mention} Please ping the person instead of typing their name.")

    @commands.command()
    @commands.cooldown(5, 300, commands.BucketType.user)
    async def rob(self, ctx):

        users = await self.get_bank_data()

        if str(ctx.author.id) not in users:
            await ctx.send(f"{ctx.author.mention} You need to create an account. You can do this by using this command: `;open_account`.")

        profit = random.randint(1, 201)
        loss = random.randint(1, 300)
        choices = ['Yes', 'Justice', 'No']
        bot_choice = random.choice(choices)
        answer_yes = [
            f"{ctx.author.mention} robbed a gas station, and ran out with ${profit}!",
            f"{ctx.author.mention} found ${profit} in someones dentures!  :D",
            f"{ctx.author.mention} robbed a house and found ${profit}!"]
        answer_justice = [
            f"{ctx.author.mention} tried to rob an old lady, but the cops came and arrested you. Your fine: ${loss}.",
            f"{ctx.author.mention} tried to rob a gangster, but she ended up robbing you. She took ${loss}.",
            f"{ctx.author.mention} fell and broke their arm when trying to make an escape on the roof. Hopsital Bill: ${loss}."]
        answer_no = [
            f"{ctx.author.mention} got nothing, nice try.",
            f"{ctx.author.mention} tried to rob an old lady, and she beat him/her up.",
            f"{ctx.author.mention} tried to rob a gas station, but the register would not open."]

        if bot_choice == "Yes":
            users[str(ctx.author.id)]["Wallet"] += int(profit)
            await ctx.send(random.choice(answer_yes))
        elif bot_choice == "Justice":
            users[str(ctx.author.id)]["Wallet"] -= int(loss)
            await ctx.send(random.choice(answer_justice))
        else:
            await ctx.send(random.choice(answer_no))

        await self.dump_data(users)

    @rob.error
    async def rob_eror(self, ctx, error):
        if isinstance(error, (commands.CommandOnCooldown)):
            time_remaining = error.retry_after / 60
            await ctx.send(f"{ctx.author.mention} You are currently on cooldown for this command. Time Remaining: {time_remaining:.2f} minutes.")


def setup(bot):
    bot.add_cog(Economy_System(bot))
    print("[economy.py] has been loaded.")