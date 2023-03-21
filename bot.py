'''
____________________ Import Libs and Values ____________________
'''
from aiogram import executor

from config import *

from ChatGPT_FUNC import chatgpt_func

from aiogram.dispatcher.filters import Text

from aiogram.dispatcher import FSMContext

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from aiogram import md

'''
____________________ Create The Keyboard ____________________
'''

def ChatGPT_beforestart_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(text='Start the bot')
    )
    return kb

def ChatGPT_start_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(text='Write a message to ChatGPT')).row(
        KeyboardButton(text='Report a problem'), (KeyboardButton(text='Stop the bot'))
    )

    return kb

def ChatGPT_stop_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text='Cancel writing'))
    
    return kb

def ChatGPT_admin_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).row(
        KeyboardButton(text='Logs'),
        KeyboardButton(text='Clear Logs'),
        KeyboardButton(text='Cancel'))
    
    return kb

def ChatGPT_confirm_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text='Confirm Clearing')).add(KeyboardButton(text='Cancel Clearing'))

    return kb
'''
____________________ Create The Bot ____________________
'''
## config.py

'''
____________________ Customer Handlers ____________________
'''

@dp.message_handler(Text(equals=['Start the bot'], ignore_case=True))
async def start_the_bot_button(message: types.Message):
    await bot.send_message(message.chat.id, text='Hello again, glad to see you!', reply_markup=ChatGPT_start_keyboard())

@dp.message_handler(commands=['start'])
async def start_cd(message: types.Message): 
    await bot.send_photo(message.chat.id, photo=start_image_url, 
                         caption=eng_desc_text, parse_mode='html', 
                         reply_markup=ChatGPT_start_keyboard())    
    
@dp.message_handler(Text(equals=['Cancel writing','Cancel'], 
                                 ignore_case=True), state='*')
@dp.message_handler(commands=['cancel'], state='*')
async def cancel_cd(message: types.Message, state: FSMContext, 
                    reply_markup=ChatGPT_start_keyboard()):
    if state is None:
        return
    await state.finish()
    await bot.send_message(chat_id=message.chat.id, 
                           text='Ok, see you!', reply_markup=reply_markup)
    
@dp.message_handler(Text(equals=['Stop', 'Stop the bot'], 
                                 ignore_case=True), state='*')
@dp.message_handler(commands=['stop'], state='*')
async def stop_cd(message: types.Message, state: FSMContext, 
                    reply_markup=ChatGPT_beforestart_keyboard()):
    if state is None:
        return
    await state.finish()
    await bot.send_message(chat_id=message.chat.id, 
                           text='Ok, see you!', reply_markup=reply_markup)

@dp.message_handler(Text(equals=['Write a message to ChatGPT']))
async def write_to_cd(message: types.Message):
    await FSM.input_text.set()
    await bot.send_message(chat_id=message.chat.id, 
                           text='Ok, enter your message:',
                           reply_markup=ChatGPT_stop_keyboard())

@dp.message_handler(state=FSM.input_text)
async def input_text(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id = message.chat.id,
                           text= '<b>Generating a response... Wait pls!</b>',
                           parse_mode='html')
    async with state.proxy() as data:
        data['input_text'] = message.text
        input_txt = data['input_text']
        return_txt = str(chatgpt_func(input_txt))
    
    try:
        await bot.send_message(chat_id = message.chat.id, 
                           text=f'<b>From ChatGPT:</b>{md.quote_html(return_txt)}',
                           parse_mode='html', reply_markup=ChatGPT_stop_keyboard())
    except:
        print('Error in function "input_txt"')
        print(f'answer: {return_txt}')

    # save_data(user_id=message.from_user.id, username=message.from_user.username, text=input_txt, answer=return_txt)

    # try:
    #     Connection = MySQL_connection()
    #     Connection.add_info(
    #         user_id = message.from_user.id, 
    #         username = message.from_user.username,
    #         text = message.text,
    #         answer = return_txt
    #         )
    # except:
    #     print ('MySQL: ERROR')

@dp.message_handler(Text(equals = ['Report a problem','report'], ignore_case=True))
@dp.message_handler(commands='report')
async def report_cd(message: types.Message):
    global report_user_id, report_username
    report_user_id = message.from_user.id
    report_username = message.from_user.username
    await bot.send_message(chat_id = message.from_user.id, 
                           text = f'<b>Please, contact the developer:  @t0_ochka ❤️</b>',
                           parse_mode = 'html',
                           reply_markup = ChatGPT_start_keyboard())
    
'''
____________________ Admin Handlers ____________________
'''

# @dp.message_handler(commands=['root'])
# async def root_cd(message: types.Message):
#     if message.from_user.id in admins:
#         await bot.send_message(chat_id=message.from_user.id,
#                                text=f'Hello, my lord {message.from_user.username}',
#                                reply_markup=ChatGPT_admin_keyboard())

# @dp.message_handler(Text(equals='Logs', ignore_case=True))
# async def root_cd(message: types.Message):
#     if message.from_user.id in admins:
#         # print(f'{show_data}')
#         if show_data() != ' ':
#             # show_data = show_data()
#             await bot.send_message(chat_id=message.from_user.id,
#                              text=f'{show_data()}',
#                              reply_markup=ChatGPT_admin_keyboard())
#         else: 
#             await bot.send_message(chat_id=message.from_user.id,
#                              text='No data found',
#                              reply_markup=ChatGPT_admin_keyboard())

# @dp.message_handler(Text(equals='Clear Logs'))
# async def root_cd(message: types.Message):
#     if message.from_user.id in admins:
#         await bot.send_message(chat_id=message.from_user.id,
#                          text='Confirm the action', 
#                          reply_markup=ChatGPT_confirm_kb())

# @dp.message_handler(Text(equals='Confirm Clearing', ignore_case=True))
# async def root_cd(message: types.Message):
#     if message.from_user.id in admins:
#         clear_data()
#         await bot.send_message(chat_id=message.from_user.id,
#                          text='The data has been cleared!',
#                          reply_markup=ChatGPT_admin_keyboard())

# @dp.message_handler(Text(equals='Cancel Clearing', ignore_case=True))
# async def root_cd(message: types.Message):
#     if message.from_user.id in admins:
#         await bot.send_message(chat_id=message.from_user.id,
#                          text='The data has not been cleared!',
#                          reply_markup=ChatGPT_admin_keyboard())



'''
____________________ Start of the Bot ____________________
'''

async def on_startup(_):
    print(f'{USERNAME}: IM HERE, BABY!')

async def on_shutdown(_):
    print()
    print(f'{USERNAME}: IM GONNA SLEEP')

if __name__ == '__main__':
    executor.start_polling(dp, 
        skip_updates=True, 
        on_startup=on_startup,
        on_shutdown=on_shutdown)
