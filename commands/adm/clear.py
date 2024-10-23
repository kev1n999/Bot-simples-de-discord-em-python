import disnake as discord
from disnake.ext import commands 


class ClearCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def clear(self, ctx, limit:int = None):
        channel = ctx.channel
        if limit is None:
            limit = 100
            
        try:
            await channel.purge(limit=limit)
        except discord.Forbidden:
            await ctx.send("Você não tem permissão para usar este comando!")

def setup(bot):
    bot.add_cog(ClearCommand(bot)) 
