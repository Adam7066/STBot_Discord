from discord.ext import commands
from core.classes import cogExtension
from core.tool import tool


class genshin(cogExtension):
    @commands.command()
    async def genshinAdd(self, ctx, name, ltuid, ltoken):
        await ctx.message.delete()
        settingJson = tool.getSettingJson()
        for i in settingJson['genshin']:
            if i['ltuid'] == ltuid:
                await ctx.send('此 ltuid: ' + ltuid + '已存在!!')
                return
        settingJson['genshin'].append({"name": name, "ltuid": ltuid, "ltoken": ltoken})
        tool.setSettingJson(settingJson)
        await ctx.send('ltuid: ' + ltuid + '新增成功!!')


def setup(bot):
    bot.add_cog(genshin(bot))
