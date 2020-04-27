# Это пример простого бота на python с использованием библиотеки saya
# сделал Lazy Fox (Ссылка на Вк — @fox_lazy )
# Актуально на 2020 год


# импорт пакетов

import time
import random
from saya import Vk #pip3.7 install saya
import json

# используем более удобную отправку сообщения 

def send(text):
    vk.messages.send(message = text, peer_id = peer_id, random_id = peer_id)

# вход в аккаунт, у меня через группу, если вы хотите через аккаунт то уберите group_id

vk = Vk(token="ваш токен", group_id="айди группы")

print("✨Загрузка...")

# Основной цикл

for event in vk.longpoll.listen(True):
  try:
    # для удобства я присвоил back значение эвента, но это не обязательно 
    back = event
    # возвращаем значение текста 
    text = (str(back["object"]["message"]["text"]))
    # возвращаем id диалога 
    peer_id = (str(back["object"]["message"]["peer_id"]))
    # возвращаем айди получателя 
    from_id = (str(back["object"]["message"]["from_id"]))
    # возвращаем номер чата
    chat_id = str(int(peer_id ) - 2000000000)
    
    # получение имени пользователя
    name = vk.users.get(user_ids=from_id)['response'][0]['first_name']
    
    # получение фамилии пользователя
    surname = vk.users.get(user_ids=from_id)['response'][0]["last_name"]
    
    if text in ["Привет","Приветик","Hello"]: # если текст сообщения совпадает с доступными 
      send("Привет, привет :³") # отпрвляется сообщение 
    
  except Exception, e: # если ошибка
    print(e) # вывод ошибки в консоль 
    send(e) # отправка сообщения об ошибке
    time.sleep(5) # отключение кода на 5 секунд

