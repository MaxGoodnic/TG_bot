from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
kb_begin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_meal_type = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_add = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_country_type = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_coctail_type = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_begin.add(KeyboardButton('MealType'), KeyboardButton('CuisineType')).row(KeyboardButton('Drinks'), KeyboardButton('Desserts'))

kb_meal_type.add(KeyboardButton('Breakfast')).add(KeyboardButton('Lunch')).add(KeyboardButton('Dinner'))

kb_add.add(KeyboardButton('anything else'))

kb_country_type.add(KeyboardButton('American'), KeyboardButton('Asian'), 
               KeyboardButton('British')).row(KeyboardButton('Chinese'), KeyboardButton('Japanese'), KeyboardButton('Indian'))

kb_coctail_type.add(KeyboardButton('Alcohol-Cocktail'), KeyboardButton('Alcohol-Free'))
