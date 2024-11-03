# CONSELHO ALEATÓRIO 

from disnake.ext import commands
from googletrans import Translator 
from requests import get 


tr = Translator()

class ConselhoCommand(commands.Cog):
	def __init__(self, bot):
		self.bot = bot 

	@commands.command()
	async def conselho(self, ctx):
		req = get("https://api.adviceslip.com/advice")
		conselho = req.json()["slip"]["advice"]
		translate = tr.translate(conselho, dest="pt")
		await ctx.send(translate.text)

def setup(bot):
	bot.add_cog(ConselhoCommand(bot))