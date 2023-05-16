from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('MealType'), 
                                                                      KeyboardButton('CuisineType')).row(KeyboardButton('Drinks'), 
                                                                                                         KeyboardButton('Desserts'))

ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Breakfast')).add(
  KeyboardButton('Lunch')).add(KeyboardButton('Dinner'))

ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('anything else'))

ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('American'), 
                                                                      KeyboardButton('Asian'), 
                                                                      KeyboardButton('British')).row(KeyboardButton('Chinese'), 
                                                                                                     KeyboardButton('Japanese'), 
                                                                                                     KeyboardButton('Indian'))

ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Alcohol-Cocktail'), 
                                                                      KeyboardButton('Alcohol-Free'))
