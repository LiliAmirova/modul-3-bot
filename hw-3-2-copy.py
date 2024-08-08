

#Реализовать запрос на отправку копии сообщения пользователю, который отправил его боту.

import requests
import json
#BASE_URL=' https://api.telegram.org/bot '


TOKEN='5813875350:AAESBclkuB6mOSzcPtQBcHpUZvwHcVj3hH0'
API_URL = ' https://api.telegram.org/bot ' + TOKEN + '/'

ADMINS=[1017765414]
#def get_updates():
#    r=requests.get(f'{BASE_URL}{TOKEN}/getUpdates')
#    message=r.json()['result'][-1]['message']['text']
#    user_id=r.json()['result'][-1]['message']['chat']['id']

#    requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text={message}')
 #   print('Вывод сообщения:',message)
#print('Started')
#get_updates()


def send_message_copy(chat_id, text):
# Получаем информацию о пользователе и чате
    data = {'chat_id': chat_id,'text': text}

    response = requests.post (API_URL + 'sendMessage', data=data)
    return json.loads(response.content)['ok']

send_message_copy(1017765414, 'text-1')
print(chat_id)















