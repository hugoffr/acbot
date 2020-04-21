import discord
from discord.ext import commands
from acbot.models.turnip_price import TurnipPrice
import datetime
import acbot.utils as utils

class Turnips(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def rtp(self, ctx: commands.Context, price: int):
        time_of_day = utils.time_of_day()

        today = datetime.date.today()
        user_id = ctx.author.id

        turnip_prices = TurnipPrice.objects(user_id=user_id, date=today, time_of_day=time_of_day)

        if not turnip_prices:
            tp = TurnipPrice(
                user_id=user_id, 
                date=today, 
                time_of_day=time_of_day, 
                price=price
            )
            tp.save()

            await ctx.send('Successfully registered {0} turnip price: {1} Bells'.format(time_of_day, price))
        else:
            old_price = turnip_prices[0].price
            TurnipPrice.objects(
                user_id=user_id, 
                date=today, 
                time_of_day=time_of_day).update_one(price=price, upsert=True)

            await ctx.send('Successfully updated {0} turnip price from {1} to {2} Bells'.format(time_of_day, old_price, price))

    @commands.command()
    async def chp(self, ctx: commands.Context):
        time_of_day = utils.time_of_day()
        today = datetime.date.today()

        turnip_prices = TurnipPrice.objects(date=today, time_of_day=time_of_day).order_by('-price')
        best_price = turnip_prices[0].price
        username = self.bot.get_user(ctx.author.id)

        await ctx.send("Today's best {0} price is {1} on {2}'s island".format(time_of_day, best_price, username))

def setup(bot: commands.Bot):
    bot.add_cog(Turnips(bot))
