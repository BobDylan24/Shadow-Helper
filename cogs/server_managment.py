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

    role = discord.SlashCommandGroup("role", "Role commands.")

    @role.command(name="add", description="Adds the role you specify from the member you specify.")
    async def add(self, ctx, member: discord.SlashCommandOptionType.user, role: discord.SlashCommandOptionType.role):
        if role in member.roles:
            await ctx.respond(f"{member.mention} already has role {role}")
        else:
            embed = discord.Embed(title="Added Role", description="Successfully added the role!", color=discord.Color.green())
            embed.add_field(name="Member", value=f"{member.mention}")
            embed.add_field(name="Role", value=f"{role}")
            await ctx.respond(embed=embed)
            await member.add_roles(role)

    @role.command(name="remove", description="Removes the role you specify from the member you specify.")
    async def remove(self, ctx, member: discord.SlashCommandOptionType.user, role: discord.SlashCommandOptionType.role):
        if role not in member.roles:
            await ctx.respond(f"{member.mention} doesn't have role {role}!")
        else:
            embed = discord.Embed(title="Removed Role", description="Successfuly removed the role!", color=discord.Color.green())
            embed.add_field(name="Member", value=f"{member.mention}")
            embed.add_field(name="Role", value=f"{role}")
            await ctx.respond(embed=embed)
            await member.remove_roles(role)

    @commands.slash_command(name="welcomemessage", description="Sets the welcome message for when people join your server.")
    @commands.has_guild_permissions(manage_guild=True)
    async def welcomemessage(self, ctx, message: discord.SlashCommandOptionType.string, channel: discord.SlashCommandOptionType.channel):
        channelId = channel.id
        welcome_filter = {"guild_id": ctx.guild.id}
        welcome_data = {"message": message, "channel": channelId}
        await self.bot.welcome.upsert_custom(welcome_filter, welcome_data)
        await ctx.respond("Changed the welcome message! And the channel!")

def setup(bot):
    bot.add_cog(server_managment(bot))