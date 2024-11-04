from disnake.ext import commands
from googletrans import Translator

class SlashTradutor(commands.Cog):
	def __init__(self, bot):	self.bot = bot 
	
	@commands.slash_command(description="Traduz um texto para o pt-br")
	async def traduzir(self, ctx, text:str):
		tr = Translator()
		traducao = tr.translate(text, dest="pt")
		await ctx.send(traducao.text)

def setup(bot):
	bot.add_cog(SlashTradutor(bot))