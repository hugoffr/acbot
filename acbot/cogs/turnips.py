import discord
from discord.ext import commands
from acbot.models.turnip_price import TurnipPrice
import datetime

class Turnips(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def rtp(self, ctx: commands.Context, price: int):
        now = datetime.datetime.now()
        time_of_day = ''

        if now.hour < 12:
            time_of_day = 'AM'
        else:
            time_of_day = 'PM'

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


def setup(bot: commands.Bot):
    bot.add_cog(Turnips(bot))
