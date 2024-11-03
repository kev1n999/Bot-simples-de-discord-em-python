# FATOS E IMAGENS ALEATÓRIAS SOBRE GATOS 

import requests 
from disnake.ext import commands 
from googletrans import Translator 

tr = Translator()

class CatCommand(commands.Cog):
	def __init__(self, bot):
		self.bot = bot 

	@commands.command(aliases=["facat", "fatogato"])
	async def catf(self, ctx):
		req = requests.get("https://catfact.ninja/fact").json()
		fact = req["fact"]
		translate = tr.translate(fact, dest="pt")

		await ctx.send(translate.text)

	@commands.command(aliases=["gato", "gatinho"])
	async def cat(self, ctx):
		req = requests.get("https://api.thecatapi.com/v1/images/search").json()
		await ctx.send(req[0]["url"])

def setup(bot):
	bot.add_cog(CatCommand(bot))