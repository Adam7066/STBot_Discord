from discord.ext import commands
from core.classes import cogExtension


class event(cogExtension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if '小十' in msg.content and msg.author != self.bot.user:
            await msg.channel.send('小十最可愛了!!')


def setup(bot):
    bot.add_cog(event(bot))
