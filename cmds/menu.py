ẽfrom discord.ext import commands

class Menu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def menu(self, ctx):

        text = """
╔══════════════════╗
        🔥 USERMAP MENU
╚══════════════════╝

🤖 AI SYSTEM
┠➤ ..ask [câu hỏi]

🎧 MUSIC SYSTEM
┠➤ ..nhac [tên bài]

🎬 VIDEO
┠➤ ..tiktok [link]

🖼 IMAGE
┠➤ ..img [từ khoá]
┠➤ ..girl

🌦 WEATHER
┠➤ ..weather [thành phố]

🎮 GAME
┠➤ ..lq [Acc lq ngẫu nhiên]

👤 USER
┠➤ ..info
┠➤ ..id
┠➤ ..avatar
┠➤ ..fb [id facebook]

⚡ SYSTEM
┠➤ ..ping
┠➤ ..uptime
"""

        await ctx.send(text)

async def setup(bot):
    await bot.add_cog(Menu(bot))
