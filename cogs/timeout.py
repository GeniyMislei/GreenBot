import disnake
import datetime
from disnake.ext import commands

class Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def timeout(self, interaction, member: disnake.Member, time: str, reason: str):
        time = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
        await member.timeout(reason=reason, until=time)
        await interaction.response.send_message(f"{member.mention} был замучен в {time} по причине {reason}")


def setup(bot):
    bot.add_cog(Timeout(bot))