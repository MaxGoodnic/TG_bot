from aiogram import types, Dispatcher

import web
from create_bot import bot
from Keyboards import kb_begin, kb_meal_type, kb_add, kb_country_type, kb_coctail_type
from web import url
from requests import get
from apikey import API_TOKEN
import random


async def commands_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Choose one of categories. Also you can write the name of dish you want to cook.',
                           reply_markup=kb_begin)


async def find_recipe(message: types.Message):
    params = {'type': 'public', 'app_id': 'd1fe2d37', 'app_key': API_TOKEN}
    params['q'] = message.text
    response = get(url, params=params).json()
    web.all_links = [response["hits"][i]["recipe"]["url"] for i in range(response["to"])]
    if len(web.all_links) == 0:
        await  bot.send_message(message.from_user.id, 'Sorry, I dont find anything.')
        # обработка ошибок с сайтов
    else:
        i = random.randrange(len(web.all_links))
        await bot.send_message(message.from_user.id, web.all_links[i], reply_markup=kb_add)
        web.all_links.pop(i)


async def meal_types(message: types.Message):
    await bot.send_message(message.from_user.id, 'Choose one of categories', reply_markup=kb_meal_type)


async def meal_type(message: types.Message):
    params = {'type': 'public', 'app_id': 'd1fe2d37', 'app_key': API_TOKEN}
    params['meal_type'] = message.text.lower().capitalize()
    response = get(url, params=params).json()
    web.all_links = [response["hits"][i]["recipe"]["url"] for i in range(response["to"])]
    if len(web.all_links) == 0:
        await  bot.send_message(message.from_user.id, 'Sorry, I dont find anything.')
        # обработка ошибок с сайтов
    else:
        i = random.randrange(len(web.all_links))
        await bot.send_message(message.from_user.id, web.all_links[i] + '\nIs it good enough?',
                               reply_markup=kb_add)
        web.all_links.pop(i)


async def anything_else(message: types.Message):
    if len(web.all_links) == 0:
        await bot.send_message(message.from_user.id, "That's all I can to offer to you")
    i = int(random.randrange(len(web.all_links)))
    await bot.send_message(message.from_user.id, web.all_links[i], reply_markup=kb_add)
    web.all_links.pop(i)


async def cuisine_type(message: types.Message):
    await bot.send_message(message.from_user.id, "Choose country", reply_markup=kb_country_type)


async def countries(message: types.Message):
    params = {'type': 'public', 'app_id': 'd1fe2d37', 'app_key': API_TOKEN}
    params['cuisine_type'] = message.text.lower().capitalize()
    response = get(url, params=params).json()
    web.all_links = [response["hits"][i]["recipe"]["url"] for i in range(response["to"])]
    if len(web.all_links) == 0:
        await  bot.send_message(message.from_user.id, 'Sorry, I dont find anything.')
        # обработка ошибок с сайтов
    else:
        i = random.randrange(len(web.all_links))
        await bot.send_message(message.from_user.id, web.all_links[i], reply_markup=kb_add)
        web.all_links.pop(i)


async def drinks(message: types.Message):
    await bot.send_message(message.from_user.id, "Choose one of categories", reply_markup=kb_coctail_type)


async def elsee(message: types.Message):
    if len(web.all_links) == 0:
        await bot.send_message(message.from_user.id, "That's all I can to offer to you")
    i = int(random.randrange(len(web.all_links)))
    await bot.send_message(message.from_user.id, web.all_links[i], reply_markup=kb_add)
    web.all_links.pop(i)


async def drink_type(message: types.Message):
    params = {'type': 'public', 'app_id': 'd1fe2d37', 'app_key': API_TOKEN}
    params['dish_type'] = 'Drinks'
    params['health'] = message.text.lower()
    response = get(url, params=params).json()
    print(response)
    web.all_links = [response["hits"][i]["recipe"]["url"] for i in range(response["to"])]
    if len(web.all_links) == 0:

        if (message.text.lower() == 'alcohol-cocktail'):
            await  bot.send_message(message.from_user.id, 'Я за здоровую нацию.')
        else:
            await  bot.send_message(message.from_user.id, 'Sorry, I dont find anything.')
        # обработка ошибок с сайтов
    else:
        i = random.randrange(len(web.all_links))
        await bot.send_message(message.from_user.id, web.all_links[i], reply_markup=kb_add)
        web.all_links.pop(i)


async def desserts(message: types.Message):
    params = {'type': 'public', 'app_id': 'd1fe2d37', 'app_key': API_TOKEN}
    params['dish_type'] = 'Desserts'
    response = get(url, params=params).json()
    web.all_links = [response["hits"][i]["recipe"]["url"] for i in range(response["to"])]
    if len(web.all_links) == 0:
        await  bot.send_message(message.from_user.id, 'Sorry, I dont find anything.')
        # обработка ошибок с сайтов
    else:
        i = random.randrange(len(web.all_links))
        await bot.send_message(message.from_user.id, web.all_links[i], reply_markup=kb_add)
        web.all_links.pop(i)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['Start', 'Help'])
    dp.register_message_handler(cuisine_type, lambda message: message.text.lower() in ['cuisine type'])
    dp.register_message_handler(meal_types, lambda message: message.text.lower() in ['meal type'])
    dp.register_message_handler(drinks, lambda message: message.text.lower() in ['drinks'])
    dp.register_message_handler(desserts, lambda message: message.text.lower() in ['dessert'])
    dp.register_message_handler(countries,
                                lambda message: message.text.lower() in ['american', 'asian', 'british', 'chinese',
                                                                         'japanese', 'indian'])
    dp.register_message_handler(drink_type, lambda message: message.text.lower() in ['alcohol-cocktail', 'alcohol-free'])
    dp.register_message_handler(meal_type, lambda message: message.text.lower() in ['breakfast', 'lunch', 'dinner'])
    dp.register_message_handler(elsee, lambda message: message.text.lower() in ['anything else'])
    dp.register_message_handler(find_recipe)
