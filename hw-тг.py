

#Зарегистрировать своего бота и реализовать эхо бота в Телеграм.

import asyncio
import aiogram
import requests

BASE_URL='https://api.telegram.org/bot'
TOKEN='5813875350:AAESBclkuB6mOSzcPtQBcHpUZvwHcVj3hH0'

def get_updates():
    r=requests.get(f'{BASE_URL}{TOKEN}/getUpdates')
    message=r.json()['result'][-1]['message']['text']
    user_id=r.json()['result'][-1]['message']['chat']['id']

    requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text={message}')
    print('Started')
get_updates()

#if __name__ == "__main__":
#   main()












