from discord.ext import commands
from core.classes import cogExtension


class normal(cogExtension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Latency: {round(self.bot.latency * 1000, 2)} ms')

    @commands.command()
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num + 1)


def setup(bot):
    bot.add_cog(normal(bot))
