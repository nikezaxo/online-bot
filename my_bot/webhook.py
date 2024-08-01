import os
import requests

TOKEN = os.getenv('7364696581:AAHk1qcga2LUeVBh8wZ58v84JL0q9j9po4A')
WEBHOOK_URL = 'https://your-codespace-url/github/your-repo-name/webhook'
url = f'https://api.telegram.org/bot{TOKEN}/setWebhook'
response = requests.post(url, data={'url': WEBHOOK_URL})

print(response.json())
