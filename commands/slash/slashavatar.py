from disnake.ext import commands 
from disnake import User, Embed, Colour 

class SlashAvatarCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.slash_command(description="Mostra o avatar/foto do usuário mencionado")
    async def avatar(self, ctx, user:User = None):
        if user is None:
            user = ctx.author

        avatar = user.display_avatar
        embed = Embed(
            title=f"🖼 Avatar de {user.name}",
            color=Colour.blue()
        ).set_image(avatar)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(SlashAvatarCommand(bot))