import discord
from discord.ext import commands, tasks
import config
import os
import asyncio
import random


intents = discord.Intents.all()
intents.message_content = True


activity = discord.Activity(type=discord.ActivityType.watching, name=f"Over /help")

bot = commands.Bot(intents=intents, command_prefix="!", owner_id=866285734808780812, activity=activity)

bot.remove_command("help")

@bot.event
async def on_ready():
    print(f"Logged into {bot.user}")

@bot.event
async def on_ready():
    print(f"Logged into {bot.user}")
    channel = bot.get_channel(1062908409646694440)
    await channel.purge(limit=1)
    class MyView(discord.ui.View):
        @discord.ui.button(label="Bot Updates", style=discord.ButtonStyle.success)
        async def first_button_callback(self, button, interaction):
            role_id = 1062902392162619442
            role = discord.utils.get(ctx.guild.roles, id=role_id)
            await interaction.response.send_message("Added you to the Bot Updates Role.", ephemeral=True)
            await interaction.user.add_roles(role)
            return
        @discord.ui.button(label="Github Updates", style=discord.ButtonStyle.secondary)
        async def second_button_callback(self, button, interaction):
            role_id = 1062902911018999858
            role = discord.utils.get(ctx.guild.roles, id=role_id)
            await interaction.response.send_message("Added you to the Github Updates Role.", ephemeral=True)
            await interaction.user.add_roles(role)
            return
        @discord.ui.button(label="Giveaway Ping", style=discord.ButtonStyle.blurple)
        async def third_button_callback(self, button, interaction):
            role_id = 1062903246097743902
            role = discord.utils.get(ctx.guild.roles, id=role_id)
            await interaction.response.send_message("Added you to the Giveaway Ping Role.", ephemeral=True)
            await interaction.user.add_roles(role)
            return
        @discord.ui.button(label="Announcement Ping", style=discord.ButtonStyle.danger)
        async def fourth_button_callback(self, button, interaction):
            role_id = 1062903604937232474
            role = discord.utils.get(ctx.guild.roles, id=role_id)
            await interaction.response.send_message("Added you to the Announcement Ping Role.", ephemeral=True)
            await interaction.user.add_roles(role)
            return
    
    embed = discord.Embed(title="Reaction Roles", description="Click the buttons below to assign your self the roles you want.", color=discord.Color.blurple())
    await channel.send(embed=embed, view=MyView())

@bot.slash_command(name="load", description="Loads the cog that you specify.", guild_ids=[1062880883423584298])
@commands.is_owner()
async def load(ctx, extension: discord.SlashCommandOptionType.string):
    bot.load_extension(f"cogs.{extension}")
    await ctx.respond(f"Loaded cog `{extension}`")

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.respond("You are not the owner of the bot!")
        return
    else:
        print(error)
        await ctx.respond(f"```{error}```\nPlease report this error to Bob Dylan#4886 if this error continues.")
        return

@bot.slash_command(name="unload", description="Unloads the cog that you specify.", guild_ids=[1062880883423584298])
@commands.is_owner()
async def unload(ctx, extension: discord.SlashCommandOptionType.string):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.respond(f"Unloaded cog `{extension}`")

@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.respond("You are not the owner of the bot!")
        return
    else:
        print(error)
        await ctx.respond(f"```{error}```\nPlease report this error to Bob Dylan#4886 if this error continues.")
        return

@bot.slash_command(name="reload", description="Reloads the cog that you specify.", guild_ids=[1062880883423584298])
@commands.is_owner()
async def reload(ctx, extension: discord.SlashCommandOptionType.string):
    bot.reload_extension(f"cogs.{extension}")
    await ctx.respond(f"Reloaded cog `{extension}`")

@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.respond("You are not the owner of the bot!")
        return
    else:
        print(error)
        await ctx.respond(f"```{error}```\nPlease report this error to Bob Dylan#4886 if this error continues.")
        return

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded Cog {filename[:-3]}")
    else:
        print(f"Failed to load cog {filename[:-3]}\n if the cog if __pycach then you may ignore it.")

bot.run(config.token)