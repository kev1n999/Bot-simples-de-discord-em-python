# PIADA ALEATÓRIA

from disnake.ext import commands 
from requests import get 
from bs4 import BeautifulSoup as sp 
from googletrans import Translator 

tr = Translator()

class PiadaCommand(commands.Cog):
	def __init__(self, bot):
		self.bot = bot 

	@commands.command(aliases=["randompiada", "piadaaleatoria", "piadadepai"])
	async def piada(self, ctx):
		req = get("https://icanhazdadjoke.com/")
		bf = sp(req.text, "html.parser")
		find = bf.find("p", attrs={"class": "subtitle"})
		translate = tr.translate(find.text, dest="pt")

		await ctx.send(translate.text)

def setup(bot):
	bot.add_cog(PiadaCommand(bot))