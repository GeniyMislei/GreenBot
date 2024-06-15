from disnake.ext import commands
import disnake

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command()
    async def ban(self, interaction, user: disnake.User, *, reason=None):
        await interaction.guild.ban(user, reason=reason)
        await interaction.response.send_message(f"{user.mention} был забанен по причине {reason}")


def setup(bot):
    bot.add_cog(Ban(bot))