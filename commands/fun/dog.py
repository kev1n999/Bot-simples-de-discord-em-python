# GERA FOTOS ALEATÓRIAS DE CACHORROS

from disnake.ext import commands 
from requests import get 

class DogCommand(commands.Cog):
	def __init__(self, bot):
		self.bot = bot 

	@commands.command(aliases=["cachorro", "cão"])
	async def dog(self, ctx):
		req = get("https://dog.ceo/api/breeds/image/random")
		url = req.json()["message"]

		await ctx.send(url)

def setup(bot):    
	bot.add_cog(DogCommand(bot))