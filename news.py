import requests
import datetime

API_KEY = '1b96de7dc8c7442db91526a3078a60e4'

h, t = 'h', 't'

wish = input('Please Enter (h) for Headlines and (t) to Search by Topic: ')

if wish == h: 
    BASE_URL = 'https://newsapi.org/v2/top-headlines'
    request_url = f'{BASE_URL}?country=us&apiKey={API_KEY}'
    response = requests.get(request_url)
    if response.status_code == 404:
        print("there was a problem")
    else:
        data = response.json()
        for i in range(20):
            title = data['articles'][i]['title']
            print(title)
            print()
elif wish == t:
    topic = input('Enter the Interested Topic: ')
    BASE_URL = 'https://newsapi.org/v2/everything'
    request_url = f'{BASE_URL}?q={topic}&from={datetime.date.today()}&sortBy=popularity&apiKey={API_KEY}'
    response = requests.get(request_url)
    if response.status_code == 404:
        print("there was a problem")
    else:
        data = response.json()
        # print(data)
        for i in range(10):
            title = data['articles'][i]['title']
            print()
            print(title)


