import genshin
from discord.ext import commands, tasks
from core.classes import cogExtension
from core.tool import tool
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo


class hoyolab(cogExtension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settingJson = tool.getSettingJson()
        self.botTestchannel = self.bot.get_channel(self.settingJson['botTestChannelID'])
        self.dailySignIn.start()

    async def _dailySignIn(self):
        nowTimeYMD = (
            datetime.now(tz=timezone.utc)
            .astimezone(ZoneInfo('Asia/Taipei'))
            .date()
            .strftime('%Y-%m-%d')
        )
        for i in range(len(self.settingJson['genshin'])):
            if self.settingJson['genshin'][i]['signInDate'] != nowTimeYMD:
                cookies = {
                    "ltuid": self.settingJson['genshin'][i]['ltuid'],
                    "ltoken": self.settingJson['genshin'][i]['ltoken'],
                }
                client = genshin.Client(cookies)
                client.default_game = genshin.Game.GENSHIN
                try:
                    reward = await client.claim_daily_reward()
                except genshin.AlreadyClaimed:
                    await self.botTestchannel.send(
                        f"{self.settingJson['genshin'][i]['name']} 每日簽到獎勵已領取!!"
                    )
                else:
                    await self.botTestchannel.send(
                        f"{self.settingJson['genshin'][i]['name']} 每日簽到獲得 {reward.amount} x {reward.name}"
                    )
                self.settingJson['genshin'][i]['signInDate'] = nowTimeYMD
            tool.setSettingJson(self.settingJson)

    @tasks.loop(hours=1)
    async def dailySignIn(self):
        await self._dailySignIn()

    @commands.command()
    async def genshinAdd(self, ctx, name, ltuid, ltoken):
        await ctx.message.delete()
        for i in self.settingJson['genshin']:
            if i['ltuid'] == ltuid:
                await ctx.send('此 ltuid:', ltuid, '已存在!!')
                return
        nowTime = datetime.now(tz=timezone.utc).astimezone(ZoneInfo('Asia/Taipei'))
        self.settingJson['genshin'].append(
            {
                "name": name,
                "ltuid": ltuid,
                "ltoken": ltoken,
                "signInDate": (nowTime + timedelta(days=-1)).strftime('%Y-%m-%d'),
            }
        )
        tool.setSettingJson(self.settingJson)
        await ctx.send('name:', name, 'ltuid:', ltuid, '新增成功!!')
        await self._dailySignIn()


def setup(bot):
    bot.add_cog(hoyolab(bot))
