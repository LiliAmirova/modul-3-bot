
#Реализовать запрос на отправку копии сообщения пользователю, который отправил его боту.
import asyncio
import time
import requests
BASE_URL='https://api.telegram.org/bot'
TOKEN='5813875350:AAESBclkuB6mOSzcPtQBcHpUZvwHcVj3hH0'
ADMINS=[1017765414]



def get_updates_text():
    update_id=0
    while True:
        time.sleep(0.5)
        r=requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        update_id_new=r['result'][-1]['update_id']
        if update_id!=update_id_new:
            message=r['result'][-1]['message']['text']
            user_id=r['result'][-1]['message']['chat']['id']
            print('user_id=',user_id)
            requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text={message}')
            print('Вывод сообщения:',message)
            update_id=update_id_new
        return

def get_updates_video():
    update_id=0
    while True:
        time.sleep(0.5)
        r=requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        update_id_new=r['result'][-1]['update_id']
        if update_id!=update_id_new:
            message=r['result'][-1]
            file_id = message['message']['video']['file_id']
            user_id=message['message']['from']['id']
            requests.get(f'{BASE_URL}{TOKEN}/sendVideo?chat_id={user_id}&video={file_id}')
            update_id=update_id_new
        return
    
def get_updates_voice():
    update_id=0
    while True:
        time.sleep(0.5)
        r=requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        update_id_new=r['result'][-1]['update_id']
        if update_id!=update_id_new:
            message=r['result'][-1]
            file_id = message['message']['voice']['file_id']
            user_id=message['message']['from']['id']
            requests.get(f'{BASE_URL}{TOKEN}/sendVoice?chat_id={user_id}&voice={file_id}')
            update_id=update_id_new
        return   

def get_updates_photo():
    update_id=0
    while True:
        time.sleep(0.5)
        r=requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        update_id_new=r['result'][-1]['update_id']
        if update_id!=update_id_new:
            message=r['result'][-1]
            file_id = message['message']['photo'][-1]['file_id']
            user_id=message['message']['from']['id']
            requests.get(f'{BASE_URL}{TOKEN}/sendPhoto?chat_id={user_id}&photo={file_id}')
            update_id=update_id_new
        return 
    
def get_updates_sticker():
    update_id=0
    while True:
        time.sleep(0.5)
        r=requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        update_id_new=r['result'][-1]['update_id']
        if update_id!=update_id_new:
            message=r['result'][-1]
            file_id = message['message']['sticker']['file_id']
            user_id=message['message']['from']['id']
            requests.get(f'{BASE_URL}{TOKEN}/sendsticker?chat_id={user_id}&sticker={file_id}')
            update_id=update_id_new
        return  

def get_updates_document(): #текстовый документ
    update_id=0
    while True:
        time.sleep(0.5)
        r=requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        update_id_new=r['result'][-1]['update_id']
        if update_id!=update_id_new:
            message=r['result'][-1]
            file_id = message['message']['document']['file_id']
            user_id=message['message']['from']['id']
            requests.get(f'{BASE_URL}{TOKEN}/sendDocument?chat_id={user_id}&document={file_id}')
            update_id=update_id_new
        return

def get_updates_thumb(): # документ в формате PDF
    update_id=0
    while True:
        time.sleep(0.5)
        r=requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        update_id_new=r['result'][-1]['update_id']
        if update_id!=update_id_new:
            message=r['result'][-1]
            file_id = message['message']['thumb']['file_id']
            user_id=message['message']['from']['id']
            requests.get(f'{BASE_URL}{TOKEN}/sendThumb?chat_id={user_id}&thumb={file_id}')
            update_id=update_id_new
        return  
    
def get_updates_error():
    update_id=0
    while True:
        time.sleep(0.5)
        r=requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        update_id_new=r['result'][-1]['update_id']
        if update_id!=update_id_new:
            message=r['result'][-1]
            user_id=message['message']['from']['id']
            user_name=message['message']['from']['first_name']
            requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text= Оо,{user_name}, Формат сообщения боту не известен. Не могу вам его вернуть')
            update_id=update_id_new
        return
    
#def otpravka()





def find_key_my(dic): #поиск ключей, чтобы выявить тип сообщения

    keys=[]
    if isinstance(dic,dict): 
        for key,value in dic.items():
            print('Смотрим ключ:',key)
            if key == 'video':
                print('Есть Видео:', get_updates_video())    
            elif key == 'text':
                print('есть Tескт:', get_updates_text())

            elif key == 'voice': 
                print('есть Голос:', get_updates_voice())   
            elif key == 'photo':
                print('есть Фото:', get_updates_photo())
            elif key == 'sticker':  
                print('есть Стикер:', get_updates_sticker())
            elif key == 'document':    
                print('есть Документ:', get_updates_document())   
            elif key == 'thumb': 
                print('есть Документ pdf:', get_updates_thumb())                           
            else:
                print('---нет ничего---')

            if isinstance(value, dict):
                keys.append(key)
                keys.append(find_key_my(value))

            elif isinstance(value, list):
                keys.append(key)
                keys.append(find_key_my(value[0]))

            else:
                keys.append(key)
   
    print(keys)
    return
          
def pulling(): # приветствие и ловит новые сообщения
    update_id=0
    while True:
        time.sleep(0.5)
        r=requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        update_id_new=r['result'][-1]['update_id']
        if update_id!=update_id_new:
            message=r['result'][-1]
            user_id=message['message']['from']['id']
            user_name=message['message']['from']['first_name']
            requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text=hello, {user_name}, возвращаю ваше сообщение')
            update_id=update_id_new
            print('update_id',update_id)
            print('Вывод последнего сообщения', message['message'])
            print('Проверка message-нового', message)
            find_key_my(message)

   
print("Старт")
r=requests.get(f'{BASE_URL}{TOKEN}/getUpdates')
message=r.json()['result'][-1]
pulling()

