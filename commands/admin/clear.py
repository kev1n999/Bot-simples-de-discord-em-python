from disnake.ext import commands 
from asyncio import sleep 

class ClearCommand(commands.Cog):
    def __init__(self, bot): self.bot = bot 
    
    @commands.command(aliases=["cls", "clean"])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, limit: int = None):
        if limit is None:
            limit = 100
        elif limit > 100:
            await ctx.send("Eu posso apagar até 100 mensagens.")
            return 
        
        await ctx.channel.purge(limit=limit)
        await sleep(1.5)
        await ctx.send(f"Foram apagadas {limit} mensagens em <#{ctx.channel.id}>", delete_after=5.0)

def setup(bot):
    bot.add_cog(ClearCommand(bot))