import requests
import disnake as discord
from disnake.ext import commands

url = "http://ip-api.com/json/"

class SlashIpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="locip", description="Faz o rastreamento do endereço ip específicado")
    async def locip(self, ctx, ip):
        try:
            req = requests.get(url + ip)
            r = req.json()

            result = f"""Endereço ip: {r["query"]} 
Cidade: {r["city"]}
País: {r["country"]} ({r["countryCode"]})
Região: {r["regionName"]} ({r["region"]}) 
Latitude: {r["lat"]}
Longitude: {r["lon"]}   
Zip: {r["zip"]}
Org: {r["org"]}"""
            embed = discord.Embed(
                title=f"STATUS:  ✔ {req.status_code}",
                description=result,
                color=discord.Colour.blue()
            )


            await ctx.send(embed=embed)

        except Exception:
            print(Exception)
            status_code = "error"
            embed = discord.Embed(title=f"STATUS: ❌ {status_code}",
                    description="Não foi possível rastrear este ip, verifique se é um endereço ip válido.",
                    color=discord.Colour.red())

            await ctx.send(embed=embed, delete_after=5.0)

def setup(bot):
    bot.add_cog(SlashIpCommand(bot))
