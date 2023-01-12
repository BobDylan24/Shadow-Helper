import discord
from discord.ext import commands

class server_managment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="announce", description="Sends an announcement that you specify into the channel you specify, and pings the role you specify.")
    @commands.has_guild_permissions(manage_messages=True)
    async def announce(self, ctx, channel: discord.SlashCommandOptionType.channel, role: discord.SlashCommandOptionType.role):
        class MyModal(discord.ui.Modal):
            def __init__(self, *args, **kwargs) -> None:
                super().__init__(*args, **kwargs)

                self.add_item(discord.ui.InputText(label="Title Of Announcement.", style=discord.InputTextStyle.short))
                self.add_item(discord.ui.InputText(label="The Announcement Description.", style=discord.InputTextStyle.long))
            async def callback(self, interaction: discord.Interaction):
                embed = discord.Embed(title=self.children[0].value, color=discord.Color.red())
                embed.add_field(name="Description Of Announcement", value=f"{self.children[1].value}", inline=False)
                await channel.send(f"<@&{role.id}>", embed=embed)
                await interaction.response.send_message("Announcement Sent!", ephemeral=True)
        modall = MyModal(title="Announcement")
        await ctx.send_modal(modall)

def setup(bot):
    bot.add_cog(server_managment(bot))