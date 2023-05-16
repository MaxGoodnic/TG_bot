from apikey import API_TOKEN
from config.config import API_ID

url = 'https://api.edamam.com/api/recipes/v2'
params = {'type': 'public', 'app_id': API_ID, 'app_key': API_TOKEN, 'meal_type': ''}
all_links = []
