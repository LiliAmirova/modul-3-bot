

#Реализовать запрос на отправку копии сообщения пользователю, который отправил его боту.
import time
import requests
BASE_URL='https://api.telegram.org/bot'
TOKEN='5813875350:AAESBclkuB6mOSzcPtQBcHpUZvwHcVj3hH0'
ADMINS=[1017765414]

def get_updates():
    #resd=requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
    #message=resd['result'][-1]['message']['text']
    #user_id=message['result'][-1]['message']['chat']['id']
    requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text={message}')
    print('Вывод сообщения:',message)
    #print('update_id', update_id)

def get_updates_video1():
    response=requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
    message=response['result'][-1]
    user_id=message['message']['from']['id']
    file_id = message['message']['video']['file_id']
    requests.get(f'{BASE_URL}{TOKEN}/sendVideo?chat_id={user_id}&video={file_id}')
    print('Вывод сообщения:',message)

def get_updates_video():
    r=requests.get(f'{BASE_URL}{TOKEN}/getUpdates')
    message=r.json()['result'][-1]['message']
    user_id=r.json()['message']['from']['id']
    file_id = message['message']['video']['file_id']
    requests.get(f'{BASE_URL}{TOKEN}/sendVideo?chat_id={user_id}&video={file_id}')
    print('Вывод сообщения:',message)
#try:
#    photo_id = message['message']['video'][-1]['file_id']
 #   bot.send_message(message.chat.id,'получил фото')
#except:
 #       bot.send_message(message.chat.id,'получил что угодно, но определенно не фото')
#if(message.Photo != null):
   # { //do something!}

def find_key(dic):
 keys=[]
 if isinstance(dic,dict): 
  for key,value in dic.items():
     if isinstance(value,dict):
        keys.append(key)
        keys.append(find_key(value))
     elif isinstance(value,list):
         keys.append(key)
         keys.append(find_key(value[0]))
     else:
        keys.append(key)
  return print(keys)
 
def find_key_my(dic):
    keys=[]
    if isinstance(dic,dict): 
        for key,value in dic.items():
            print('Смотрим ключ:',key,value )
            if key == 'video':
                print('Есть Видео:', get_updates_video())

            elif key == 'text':
                print('есть тескт:')

            else:
                print("нет ничего1")

            if isinstance(value, dict):
                keys.append(key)
                keys.append(find_key_my(value))

            elif isinstance(value, list):
                keys.append(key)
                keys.append(find_key_my(value[0]))

            else:
                keys.append(key)
    return print(keys)

def pulling():
    update_id=0
    while True:
        time.sleep(0.5)
        r=requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        update_id_new=r['result'][-1]['update_id']
        if update_id!=update_id_new:
            message=r['result'][-1]
            #message = resd['result'][-1]['message']['text']
            #user_id=message['result'][-1]['message']['chat']['id']
            user_id=message['message']['from']['id']
            user_name=message['message']['from']['first_name']
            requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text=hello,{user_name}, возвращаю ваше сообщение')
            update_id=update_id_new
            print('update_id',update_id)
            print('Вывод последнего сообщения', message['message'])
            print('Проверка message-нового', message)
            find_key_my(message)
            #find_key(message)


            requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text={message}')



print("Старт")
pulling()


#print(message['message']['video']['file_id'])

#try:
#    if video=='video':
#        file_id =message['message']['video']['file_id']
#        requests.get(f'{BASE_URL}{TOKEN}/sendVideo?chat_id={user_id}&video={file_id}')
 #       print('получил video')
#        print(message['message']['video'])
#    elif text=='text':
 #       file_id = message['message']['text']['file_id']
#        requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text={message}')

#except:
    #print ('message', message)
    #print('ContentType', Type)
  #  print('получил что угодно, но определенно не фото')
















