from disnake.ext import commands
from googletrans import Translator

translator = Translator()

class TranslateCommand(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(name="traduzir", description="Traduz um texto")
	async def traduzir(self, ctx, texto:str):
		t = translator.translate(texto, dest="pt")
		await ctx.send(t.text)

def setup(bot):
	bot.add_cog(TranslateCommand(bot))