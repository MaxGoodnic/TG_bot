from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('MealType')
b2 = KeyboardButton('CuisineType')
b3 = KeyboardButton('Drinks')
b4 = KeyboardButton('Desserts')

a1 = KeyboardButton('Breakfast')
a2 = KeyboardButton('Lunch')
a3 = KeyboardButton('Dinner')

c1 = KeyboardButton('American')
c2 = KeyboardButton('Asian')
c3 = KeyboardButton('British')
c4 = KeyboardButton('Chinese')
c5 = KeyboardButton('Japanese')
c6 = KeyboardButton('Indian')

d1 = KeyboardButton('Alcohol-Cocktail')
d2 = KeyboardButton('Alcohol-Free')

other = KeyboardButton('anything else')

kb_client1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client1.add(b1, b2).row(b3, b4)
kb_client2.add(a1).add(a2).add(a3)
kb_client3.add(other)
kb_client4.add(c1, c2, c3).row(c4, c5, c6)
kb_client5.add(d1, d2)
