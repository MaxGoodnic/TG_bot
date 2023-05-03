
##Описание работы

С сайта https://developer.edamam.com/edamam-recipe-api надо взять токен и вставить в файл apikey.cpp. Бот ищет рецепты по критерию. При вызове /start или /help вызываются кнопки, с помощью которых можно выбрать категорию, по которой ищется рецепт. При выборе некоторых из этих кнопок появляютя другие категории в данной(по типу выбор страны, завтрак, обед, ужин и т.д). Помимо этого можно искать рецепт по словам(воспринимает только английский).

Installation

git clone https://github.com/pariramb/Tg_bot.git

pip3 install aiogram

pip3 install requests

Running from 'dev' branch

git checkout dev

python3 bot_telegram.py
