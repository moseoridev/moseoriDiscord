from discord.ext import commands, tasks
import os
import crawler

bot = commands.Bot("!")
TOKEN = os.getenv("DISCORD_TOKEN")


@bot.event
async def on_ready():
    send_so.start()
    print(f"Logged in as {bot.user.name}({bot.user.id})")


@tasks.loop(seconds=300)
async def send_so():
    ch_id = 781729030491209762
    url = 'https://www.coupang.com/vp/products/2378328151'
    if not crawler.isSoldOut(url):
        channel = bot.get_channel(ch_id)
        await channel.send('품절 풀림!')


@bot.command(pass_context=True)
async def hi(ctx):
    await ctx.send('Hi, ' + ctx.author.mention)

if __name__ == "__main__":
    bot.run(TOKEN)
