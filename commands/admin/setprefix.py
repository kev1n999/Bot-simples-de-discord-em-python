import disnake as discord
from database import database 
from disnake.ext import commands


db = database.Database()
db.prefixes()

class SetPrefix(commands.Cog):
	def __init__(self, bot):
		self.bot = bot 
		self.bot.command_prefix = db.get_prefix
	
	@commands.command(aliases=["defprefix"])
	@commands.has_permissions(administrator=True)
	async def setprefix(self, ctx, prefix: str = None):
		guild_id = ctx.guild.id 
		if prefix is None:	
			await ctx.send("Defina um prefixo primeiro;")
			return
		elif len(prefix) > 3:
			await ctx.send("Prefixo muito longo!")
			return 

		db.cursor.execute(f"UPDATE prefixos SET prefix = ? WHERE guild_id = ?", (prefix, guild_id))
		db.cursor.execute(f"INSERT INTO prefixos Values(?, ?)", (prefix, guild_id))
		db.c.commit()

		embed = discord.Embed(description=f"Prefixo definido para este servidor: `{prefix}`", color=discord.Colour.red())
		await ctx.send(embed=embed)
	
	
def setup(bot):
	bot.add_cog(SetPrefix(bot))