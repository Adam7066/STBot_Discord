from discord.ext import commands
from core.classes import cogExtension


class event(cogExtension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if '小十' in msg.content and msg.author != self.bot.user:
            await msg.channel.send('小十最可愛了!!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send('請輸入正確的參數')
        elif isinstance(error, commands.errors.CommandNotFound):
            await ctx.send('OAO 沒有這個指令啦!!')
        else:
            await ctx.send(error)


def setup(bot):
    bot.add_cog(event(bot))
