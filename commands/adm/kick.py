import disnake as discord
from disnake.ext import commands

class KickCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def kick(self, ctx, user:discord.Member = None):
        if user is None:
            await ctx.send("Para expulsar um membro use: *kick @menção*", delete_after=5.0)
            return

        try:
            await user.kick()
        except discord.Forbidden:
            await ctx.send("Você não tem permissão para usar este comando!")

def setup(bot):
    bot.add_cog(KickCommand(bot))