import disnake as discord
from disnake.ext import commands

class BanCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command(aliases=["banned"])
    async def ban(self, ctx, user:discord.Member = None, reason = None):
        try:
            if user is None:
                await ctx.send("Para banir um usuário use: *ban @menção*", delete_after=5.0)
                return

            if reason is None:
                reason = "Motivo não específicado."

            await user.ban(reason=reason)
        except discord.Forbidden:
            await ctx.send("Você não tem permissão para banir este usuário!", delete_after=5.0)

def setup(bot):
    bot.add_cog(BanCommand(bot))