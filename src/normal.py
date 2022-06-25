from discord.ext import commands
from core.classes import cogExtension


class normal(cogExtension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Latency: {round(self.bot.latency * 1000, 2)} ms')


def setup(bot):
    bot.add_cog(normal(bot))
