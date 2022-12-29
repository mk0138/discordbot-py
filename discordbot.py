from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")
        
       


    if message.content.startswith(f'{PREFIX}안녕'):
        await message.channel.send('안녕!( ´-ㅅ•)▄︻┻┳══━一')

    if message.content.startswith(f'{PREFIX}갈게'):
        await message.channel.send('잘가! 기다리고 있을게')
        
    if message.content.startswith(f'{PREFIX}바보'):
        await message.channel.send('바보 으느르그...')        

    if message.content.startswith(f'{PREFIX}자기소개'):
        await message.channel.send('개발자의 이름에서 따온 밍구리 로봇')

    if message.content.startswith(f'{PREFIX}뭐해'):
        await message.channel.send('너 생각 ERROR: 110111110011001101110001111110111001110111')
        
    if message.content.startswith(f'{PREFIX}굴라그'):
        await message.channel.send('한서고 굴라그..? 아니면 나니의 굴라그..?')
        
    if message.content.startswith(f'{PREFIX}생일'):
        await message.channel.send('생일 축하해~ 좋은 하루 보냈으면 좋겠다 ㅎㅎ')
        
    if message.content.startswith(f'{PREFIX}약속잡기'):
        await message.channel.send('오늘은 할 일이 있어서..내일은 쉬어야해서..그 다음은 위의 일정을 반복해야해서...')
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
