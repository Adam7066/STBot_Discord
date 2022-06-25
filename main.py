# -*- coding:UTF-8 -*-
import os
import discord
from discord.ext import commands
from core.tool import tool


bot = commands.Bot(command_prefix='//')


@bot.event
async def on_ready():
    print('>> Bot is online <<')


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'src.{extension}')
    await ctx.send(f'Load {extension} done.')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'src.{extension}')
    await ctx.send(f'Unload {extension} done.')


@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'src.{extension}')
    await ctx.send(f'Reload {extension} done.')


if __name__ == '__main__':
    settingJson = tool.getSettingJson()
    for file in os.listdir('./src'):
        if file.endswith('.py'):
            bot.load_extension(f'src.{file[:-3]}')
    bot.run(settingJson['token'])
