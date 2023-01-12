import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="help", description="Shows all commands in the bot and what they do.")
    async def help(self, ctx):
        embed = discord.Embed(title="Help", description="Here is a list of all the commands that Shadow Helper has to offer.")
        embed.add_field(name="/cat", value="This command uses thecatapi to display an image of a random cat.", inline=False)
        embed.add_field(name="/dog", value="This command uses dog.ceo to display an image of a random dog.", inline=False)
        embed.add_field(name="/balance", value="Checks the balance of the command runner or a member if specified.", inline=False)
        embed.add_field(name="/beg", value="Puts a random number of coins from 0 to 101 into the command runners wallet balance.", inline=False)
        embed.add_field(name="/withdraw", value="Withdraws the amount of coins the command runner specifies from the command runner's bank", inline=False)
        embed.add_field(name="/deposit", value="Deposits the amount of coins the command runner specifies from the command runner's wallet", inline=False)
        embed.add_field(name="/slots", value="Bets an amount of coins the command runner specifies and doubles them if you win.", inline=False)
        embed.add_field(name="/rob", value="Robs a user that the command issuer specifies from 0 to the amount of the money the mentioned user has in the wallet", inline=False)
        embed.add_field(name="/shop", value="Opens up a shop menu where the command runner can spend their coins. The current things you can buy are an Computer and an Keyboard.", inline=False)
        embed.add_field(name="/kick", value="Kicks a member from the guild that the command runner specifies for the reason the command runner specifies.", inline=False)
        embed.add_field(name="/ban", value="Bans a member from the guild that the command runner specifies for the reason the command runner specifies.", inline=False)
        embed.add_field(name="/timeout", value="Times out a member from the guild that the command runner specifies for the time the command runner specifies for the reason the command runner specifies.", inline=False)
        embed.add_field(name="/untimeout", value="Untimes out a member from the guild that the command runner specifies.", inline=False)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))