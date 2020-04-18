from discord.ext import commands

class ACBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
