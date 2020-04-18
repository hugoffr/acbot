import discord
from discord.ext import commands

class Turnips(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx: commands.Context):
        await ctx.send('This is a test command.')    


def setup(bot: commands.Bot):
    bot.add_cog(Turnips(bot))
