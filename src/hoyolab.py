import asyncio
import genshin
from discord.ext import commands
from core.classes import cogExtension
from core.tool import tool
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


class hoyolab(cogExtension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settingJson = tool.getSettingJson()
        self.botTestchannel = self.bot.get_channel(self.settingJson['botTestChannelID'])
        self.signInDate = self.settingJson['genshinSignInDate']

        async def dailySignIn():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                nowTime = datetime.now(tz=timezone.utc).astimezone(
                    ZoneInfo('Asia/Taipei')
                )
                if nowTime.date() != self.signInDate:
                    for i in self.settingJson['genshin']:
                        cookies = {
                            "ltuid": i['ltuid'],
                            "ltoken": i['ltoken'],
                        }
                        client = genshin.Client(cookies)
                        client.default_game = genshin.Game.GENSHIN
                        try:
                            reward = await client.claim_daily_reward()
                        except genshin.AlreadyClaimed:
                            await self.botTestchannel.send(f"{i['name']} 每日簽到獎勵已領取!!")
                        else:
                            await self.botTestchannel.send(
                                f"{i['name']} 每日簽到獲得 {reward.amount} x {reward.name}"
                            )
                    self.signInDate = nowTime.date()
                await asyncio.sleep(3600)

        self.bgTask = self.bot.loop.create_task(dailySignIn())

    @commands.command()
    async def genshinAdd(self, ctx, name, ltuid, ltoken):
        await ctx.message.delete()
        for i in self.settingJson['genshin']:
            if i['ltuid'] == ltuid:
                await ctx.send('此 ltuid: ' + ltuid + '已存在!!')
                return
        self.settingJson['genshin'].append(
            {"name": name, "ltuid": ltuid, "ltoken": ltoken}
        )
        tool.setSettingJson(self.settingJson)
        await ctx.send('ltuid: ' + ltuid + '新增成功!!')


def setup(bot):
    bot.add_cog(hoyolab(bot))
