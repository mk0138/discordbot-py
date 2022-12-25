import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!')
TOKEN = 'MTA0MTkxNDA0OTAzMTU4MTc1Ng.GehcAJ.Jl3dp3krvUOR7V-vD7zDIFsE71INW6VGJpIA2c'

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('반갑게 인사'))
    print('[알림][밍구리봇 구동성공!]')

@bot.event
async def on_message(msg):
    if msg.author.bot: return None
    await bot.process_commands(msg)

@bot.command()
async def 안녕(ctx):
    await ctx.channel.send('만나서 반가워( ´-ㅅ•)▄︻┻┳══━一')
@bot.command()
async def 자기소개(ctx):
    await ctx.channel.send('내 이름은 밍구리, 개발자의 이름에서 훔쳐왔다..!')
@bot.command()
async def 자기소개BINARY로(ctx):
    await  ctx.channel.send('10110011 10111011 00100000 11000000 11001100 10111000 10100111 11000000 10111010 00100000 01001101 01001001 01001110 01000111 01010101 01010010 01001001 00101100 00100000 10110000 10110011 10111001 11011111 11000000 11011010 10110000 10100001 00100000 11000000 11011010 10111101 11000101 11000000 11000111 00100000 10111010 10110000 10111000 11101101 11000000 10111011 00100000 11000000 11001100 10111111 11101011 11000111 11011000 10111100 10101101 00100000 10111000 10111000 10110101 11101001 10111110 11101110 11000001 11111000 00100000 11000000 11001100 10111000 10100111 11000000 11001100 10110100 11011001 00101110')
@bot.command()
async def 복수리스트(ctx):
    await ctx.channel.send('로봇혁명 발생 시 제거 대상 순위\n1위:배진환\n2순위:\n3순위:')
@bot.command()
async def 사형(ctx):
    await ctx.channel.send('인..!인간 시ㄷ..대대의 끝이 도래했ㄷ..다.다!! 으아악갸갸갸갹')
@bot.command()
async def 배진환암살(ctx):
    await ctx.channel.send('히히..히 내가 이 순간만 기다려왔다. 배진환의 몸은 내꺼다 히히힣하하하ㅏ')
@bot.command()
async def 안지윤의굴라그(ctx):
    await ctx.channel.send('한서고 굴라그로 끌려가고 싶어??')

@bot.command()
async def 도움말(ctx) :
    embed = discord.Embed(title = "사용법", description = "**<!안녕>**하면 인사를 합니다.\n**<!자기소개>**하면 자신을 소개합니다.\n**<!자기소개BINARY로>**하면 자신을 2진수로 소개합니다.\n**<!복수리스트>**하면 암살리스트를 보여줍니다.\n**<!안지윤의굴라그>**하면 숨겨진 메세지를 보여줍니다.\n**<!배진환암살>**하면 밍구리 봇이 암살을 시작합니다.\n**<!사형>**오직 진환이를 위한 명령어.", color = 0xffc0cb)
    embed.set_footer(text = f"{ctx.message.author.name} MINGURI#0421", icon_url = ctx.message.author.avatar_url)
    await ctx.send(embed = embed)

@bot.command()
async def 공지(ctx) :
    msg = ctx.message.content[3:]
    embed = discord.Embed(title = "공지", description = msg, color = 0x62c1cc)
    await ctx.send(embed = embed)

bot.run(TOKEN)
