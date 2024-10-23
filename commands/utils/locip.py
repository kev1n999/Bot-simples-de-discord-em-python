import requests
import disnake as discord
from disnake.ext import commands

url = "http://ip-api.com/json/"

class LocipCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["geoip"])
    async def locip(self, ctx, ip = None):
        if ip is None:
            await ctx.send("Você precisa inserir um endereço ip para utilizar este comando!", delete_after=5.8)
            return

        try:
            req = requests.get(url+ip)
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

            del_button = discord.ui.Button(
                label="Esquecer",
                style=discord.ButtonStyle.red,
                custom_id="ignore"
            )

            await ctx.send(embed=embed, components=[del_button])

        except Exception:
            print(Exception)
            status_code = "error"
            embed = discord.Embed(title=f"STATUS: ❌ {status_code}", description="Não foi possível rastrear este ip, verifique se é um endereço ip válido.", color=discord.Colour.red())
            await ctx.send(embed=embed, delete_after=5.0)


def setup(bot):
    bot.add_cog(LocipCommand(bot))