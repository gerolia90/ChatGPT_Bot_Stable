'''
____________________ Import Libs and Values ____________________
'''

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import mysql.connector


'''
____________________ Create The Bot ____________________
'''

TOKEN_API = '6224316325:AAGpMIi1y0yziypomDdlNo0UjBsOpNt4Kjo'
LINK = 'http://t.me/testtochka_stable_bot'

storage = MemoryStorage() ## FSMachine
bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=storage)

class FSM(StatesGroup):
    input_text = State()
    search_type = State()
    search_object = State()


'''
____________________ Connect MySQL ____________________
'''

## Coming soon

'''
____________________ Create Text Values ____________________
'''

start_sticker_id='CAACAgIAAxkBAAEIGAFkDJf_QqvgbD00t_pDJ3ErJqqoGQAC8xEAAou8GEuje6z2O_w3Uy8E'

start_image_path='C:\\Users\\User\\Pictures\\0\\CVUT\\Files\\Projects\\ChatGPT\\photo_2023-03-15_16-09-30.jpg'

start_image_url='https://openaicom.imgix.net/8d14e8f0-e267-4b8b-a9f2-a79120808f5a/chatgpt.jpg?fm=auto&auto=compress,format&fit=min&rect=0,0,2048,2048&w=3840&h=3840'

help_text = '''
<b>ChatGPT Telegram Bot</b> 

<b>/start</b> - <em>start of this bot</em>
<b>/help</b> - <em>all commands of this bot</em>
<b>/desc</b> - <em>description of ChatGPT bot</em>
'''

eng_desc_text = '''
<b><a href="https://chat.openai.com/">Chat GPT</a> is a powerful Telegram bot designed to provide you with instant access to an intelligent conversational agent trained on vast amounts of text data. 
</b>
With <a href="https://chat.openai.com/">Chat GPT</a>, you can ask any question or engage 
in any topic you want and get a quick, accurate response in seconds. 

Whether you need help with your homework, 
want to discuss current events, or simply want to have a fun chat, <a href="https://chat.openai.com/">Chat GPT</a> is the perfect companion. 

The Chat GPT was created by <a href="https://openai.com/">OpenAI</a>.

An official page — <a href="https://chat.openai.com/">Chat GPT</a>

<b>If you have any problems, write to the developer: @t0_ochka ❤️
'''

ru_desc_text = '''
<em>ChatGPT - мощный Telegram-бот, предназначенный для быстрого получения ответов на ваши вопросы. 
Это интеллектуальный разговорный агент, обученный на огромном количестве текстовых данных. 

С ChatGPT вы можете задавать любые вопросы или обсуждать 
любые темы и получать быстрый и точный ответ в считанные секунды (в случае перегрузки серверов - минуты). 

Независимо от того, нужна вам помощь с домашним заданием, хотите обсудить 
текущие события или просто хотите весело пообщаться, ChatGPT - идеальный спутник.
</em>
'''
