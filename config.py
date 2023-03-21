'''
____________________ Import Libs and Values ____________________
'''

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from datetime import datetime as dt
# import mysql.connector

'''
____________________ Create The Bot ____________________
'''

TOKEN_API = '6224316325:AAGB-cDYfJe-BIpR-l26u8xpe7n4-9KCYh0'
USERNAME = '@testtochka_stable_bot'

storage = MemoryStorage() ## FSMachine
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot, storage=storage)
admins = ['868207807', 868207807]

class FSM(StatesGroup):
    input_text = State()
    search_object = State()
    issue_object = State()

'''
____________________ DB_TXT ____________________
'''

# def save_data(user_id, username, text, answer):
#     log = f'\ndate: {dt.now()}\nuser_id: {user_id}\nusername: {username}\ntext: {text}\nanswer: \n{answer}\n'
    
#     file_path = 'DB_TXT.txt'
#     read = open(file_path, 'a')
#     read.write(f'{log}')
#     read.close()
    
#     file_path_copy = 'DB_TXT_copy.txt'
#     read_copy = open(file_path_copy, 'a')
#     read_copy.write(f'{log}')
#     read_copy.close()


#     print('\n____ DB_TXT ____\n'+log)
#     print('\nData saved successfully in',file_path+'\n________________\n')

# def show_data():
#     file_path = 'DB_TXT.txt'
#     read = open(file_path, 'r')
#     return_info = read.read()
#     return return_info

# def clear_data():
#     file_path = 'DB_TXT.txt'
#     read = open(file_path, 'w')
#     read.write(f' ')
#     read.close()
#     print('The data has been cleared!')

'''
____________________ MySQL ____________________
'''

# class MySQL_connection:
#     def __init__(self):

#         self.db = mysql.connector.connect(
#             host="containers-us-west-203.railway.app",
#             user='root',
#             password='CImnTk1Ii3WMXyIS036C',
#             database="railway",
#             port = 7123
#         )
#         self.cursor = self.db.cursor()

#         ## Creating table 'ChatGPT' if it doesn't exist
#         self.cursor.execute("CREATE TABLE IF NOT EXISTS ChatGPT \
#                     (id INT AUTO_INCREMENT PRIMARY KEY, \
#                     user_id VARCHAR(255), \
#                     username VARCHAR(255), \
#                     text VARCHAR(5100), \
#                     answer VARCHAR(5100), \
#                     date_added DATETIME DEFAULT CURRENT_TIMESTAMP \
#                     ON UPDATE CURRENT_TIMESTAMP)") 
        
#         ## Creating table 'ChatGPT_Copy' if it doesn't exist
#         self.cursor.execute("CREATE TABLE IF NOT EXISTS ChatGPT_Copy \
#                     (id INT AUTO_INCREMENT PRIMARY KEY, \
#                     user_id VARCHAR(255), \
#                     username VARCHAR(255), \
#                     text VARCHAR(5100), \
#                     answer VARCHAR(5100), \
#                     date_added DATETIME DEFAULT CURRENT_TIMESTAMP \
#                     ON UPDATE CURRENT_TIMESTAMP)") 

#     def add_info(self, user_id, username, text, answer):
#         self.user_id = user_id
#         self.username = username
#         self.text = text
#         self.answer = answer
#         sql = 'INSERT INTO ChatGPT\
#                 (user_id, username, text, answer)\
#                 VALUES (%s, %s, %s, %s)'
#         sql_copy = '''INSERT INTO ChatGPT_Copy 
#         SELECT * FROM ChatGPT 
#         WHERE NOT EXISTS 
#         (SELECT * FROM ChatGPT_Copy WHERE ChatGPT_Copy.id = ChatGPT.id)'''
#         val = (self.user_id, self.username, self.text, self.answer)
#         self.cursor.execute(sql, val)
#         self.db.commit()
#         print('MySQL: Data saved successfully!')
#         self.cursor.execute(sql_copy)
#         self.db.commit()
#         print('MySQL: A copy of the data has been saved successfully!')
        

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

You can also use <a href="https://t.me/testtochka_stable_bot">stable version of this bot</a></b>
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
