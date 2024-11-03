# INSULTO ALEATÓRIO

from disnake.ext import commands
from requests import get 
from googletrans import Translator 

tr = Translator()

class InsultCommand(commands.Cog):
	def __init__(self, bot):
		self.bot = bot 

	@commands.command(aliases=["xingamento", "insulto"])
	async def insult(self, ctx):
		req = get(" https://insult.mattbas.org/api/insult")
		translate = tr.translate(req.text, dest="pt")
		await ctx.send(translate.text)

def setup(bot):
	bot.add_cog(InsultCommand(bot))