from apikey import API_TOKEN

# from pprint import PrettyPrinter

# pp=PrettyPrinter()
url = 'https://api.edamam.com/api/recipes/v2'
params = {'type': 'public', 'app_id': 'd1fe2d37', 'app_key': API_TOKEN, 'mealType': ''}
all_links = []
