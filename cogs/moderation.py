import discord
from discord.ext import commands
import os
import asyncio
import config
import datetime

today = datetime.datetime.today()

list_time = [300,600,900,1200]

async def time_searcher(ctx: discord.AutocompleteContext):
    return [
        time for time in list_time
    ]

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(name="kick", description="Kicks the user you specify for the reason you specify.")
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.SlashCommandOptionType.user):
        class MyModal(discord.ui.Modal):
            def __init__(self, *args, **kwargs) -> None:
                super().__init__(*args, **kwargs)
            
                self.add_item(discord.ui.InputText(label="Reason", style=discord.InputTextStyle.long))
            async def callback(self, interaction: discord.Interaction):
                embed = discord.Embed(title="Kicked Member", description="I have kicked the member from the guild.", color=discord.Color.green())
                embed.add_field(name="Member Kicked", value=f"{member.mention}", inline=False)
                embed.add_field(name="Reason", value=self.children[0].value, inline=False)
                await ctx.respond(embed=embed)
                embed = discord.Embed(title="You Have Been Kicked", description=f"You have been kicked from guild {ctx.guild.name}.", color=discord.Color.red())
                embed.add_field(name="Staff Member", value=f"{ctx.author.mention}", inline=False)
                embed.add_field(name="Reason", value=self.children[0].value, inline=False)
                embed.add_field(name="Date", value=today, inline=False)
                await member.send(embed=embed)
                await member.kick()
        modall = MyModal(title=f"Why do you want to kick this user?")
        await ctx.send_modal(modall)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond(f"You are missing the `kick_members` permission.")
            return
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.respond("The user you are trying to kick has private messages turned off.\nThe user has been kicked but has not been sent a message in dms.")
            return
        else:
            print(error)
            await ctx.respond(f"```{error}```\nPlease report the error to Bob Dylan#4886 if this error continues.")
            return

    @commands.slash_command(name="ban", description="Bans the user you specify for the reason you specify.")
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.SlashCommandOptionType.user):
        class MyModal(discord.ui.Modal):
            def __init__(self, *args, **kwargs) -> None:
                super().__init__(*args, **kwargs)
            
                self.add_item(discord.ui.InputText(label="Reason", style=discord.InputTextStyle.long))
            async def callback(self, interaction: discord.Interaction):
                embed = discord.Embed(title="Banned Member", description="I have banned the member from the guild.", color=discord.Color.green())
                embed.add_field(name="Member Banned", value=f"{member.mention}", inline=False)
                embed.add_field(name="Reason", value=self.children[0].value, inline=False)
                await ctx.respond(embed=embed)
                embed = discord.Embed(title="You Have Been Banned", description=f"You have been banned from guild {ctx.guild.name}.", color=discord.Color.red())
                embed.add_field(name="Staff Member", value=f"{ctx.author.mention}", inline=False)
                embed.add_field(name="Reason", value=self.children[0].value, inline=False)
                embed.add_field(name="Date", value=today, inline=False)
                await member.send(embed=embed)
                await member.ban(reason=self.children[0].value)
        modall = MyModal(title=f"Why do you want to ban this user?")
        await ctx.send_modal(modall)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond(f"You are missing the `ban_members` permission.")
            return
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.respond("The user you are trying to ban has private messages turned off.\nThe user has been banned but has not been sent a message in dms.")
            return
        else:
            print(error)
            await ctx.respond(f"```{error}```\nPlease report the error to Bob Dylan#4886 if this error continues.")
            return

    @commands.slash_command(name="timeout", description="Times out the user you specify for the time you specify for the reason you specify.")
    @commands.has_guild_permissions(kick_members=True)
    async def timeout(self, ctx, member : discord.SlashCommandOptionType.user, time: discord.Option(int, "Select a time to time the person out for.", autocomplete=time_searcher)):
        class MyModal(discord.ui.Modal):
            def __init__(self, *args, **kwargs) -> None:
                super().__init__(*args, **kwargs)

                self.add_item(discord.ui.InputText(label="Reason", style=discord.InputTextStyle.long))
            async def callback(self, interaction: discord.Interaction):
                embed = discord.Embed(title="Timed out Member", description="I have timed out the member from the guild.", color=discord.Color.green())
                embed.add_field(name="Member Timed out", value=f"{member.mention}", inline=False)
                embed.add_field(name="Reason", value=self.children[0].value, inline=False)
                await ctx.respond(embed=embed)
                embed = discord.Embed(title="You Have Been Timed out", description=f"You have been timed out from guild {ctx.guild.name}.", color=discord.Color.red())
                embed.add_field(name="Staff Member", value=f"{ctx.author.mention}", inline=False)
                embed.add_field(name="Reason", value=self.children[0].value, inline=False)
                timeout_time = datetime.timedelta(seconds=time)
                embed.add_field(name="Time", value=f"{time} seconds")
                embed.add_field(name="Date", value=today, inline=False)
                await member.send(embed=embed)
                await member.timeout_for(timeout_time)
        modall = MyModal(title="Why do you want to time this user out?")
        await ctx.send_modal(modall)

    @timeout.error
    async def timeout_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond("You are missing the `kick_members` permission.")
            return
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.respond("The user you are trying to time out has private messages turned off.\nThe user has been timed out but has not been sent a message in dms.")
            return
        else:
            print(error)
            await ctx.respond(f"```{error}```\nPlease report the error to Bob Dylan#4886 if this error continues.")
            return
                

    @commands.slash_command(name="untimeout", description="Untimes out the user you specify.")
    @commands.has_guild_permissions(kick_members=True)
    async def untimeout(self, ctx, member : discord.SlashCommandOptionType.user):
        embed = discord.Embed(title="Untimed out Member", description="I have untimed out the member from the guild.", color=discord.Color.green())
        embed.add_field(name="Member untimed out", value=f"{member.mention}", inline=False)
        await ctx.respond(embed=embed)
        embed = discord.Embed(title="You Have Been Untimed out", description=f"You have been untimed out from guild {ctx.guild.name}", color=discord.Color.red())
        embed.add_field(name="Staff Member", value=f"{ctx.author.mention}", inline=False)
        timeout_time = datetime.timedelta(seconds=0)
        embed.add_field(name="Date", value=today, inline=False)
        await member.send(embed=embed)
        await member.timeout_for(timeout_time)

    @untimeout.error
    async def untimeout_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond("You are missing the `kick_members` permission.")
            return
        else:
            print(error)
            await ctx.respond(f"```{error}```\nPlease report the error to Bob Dylan#4886 if this error continues.")
            return

def setup(bot):
    bot.add_cog(moderation(bot))