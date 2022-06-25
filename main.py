# -*- coding:UTF-8 -*-
import discord
from discord.ext import commands
from core.tool import tool


bot = commands.Bot(command_prefix='//')


@bot.event
async def on_ready():
    print('>> Bot is online <<')


if __name__ == '__main__':
    settingJson = tool.getSettingJson()
    bot.run(settingJson['token'])
