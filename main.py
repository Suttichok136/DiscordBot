import discord
from discord.ext import commands

import os

#import all of the cogs
from photopicker import image_cog

bot = commands.Bot(command_prefix='/')

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(image_cog(bot))

#start the bot with our token
bot.run("ODg2OTk0MjU5NTc0NjczNDI5.YT9rxw.xqJ0eafYQ_OkwK5LhSvRkitkwIg")