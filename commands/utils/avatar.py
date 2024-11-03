import disnake as discord
from disnake.ext import commands 

class AvatarCommand(commands.Cog):
	def __init__(self, bot):
		self.bot = bot 

	@commands.command(aliases=["av", "icon", "userav"])
	async def avatar(self, ctx, user:discord.User = None):
		if user is None:	user = ctx.author
		avatar = user.display_avatar

		embed = discord.Embed(title=f"🖼 Avatar de {user.name}", color=discord.Colour.red())
		embed.set_image(avatar.url)

		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(AvatarCommand(bot))