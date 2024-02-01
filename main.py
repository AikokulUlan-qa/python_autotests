#a = 5
#b = 7
#sum = a + b  
#print(f'Результат сложения: {sum}')

#if sum == 12:
#   print ('Ok')
#else:
#   print ('Bad')

"""
Test api
Код для запросов c выводом (принтом) ответа по документации Покемонов:

- Создание покемона (**POST /pokemons** (*не забудь про нужный хэдер*))

В ответе (терминале) должен прийти объект json

- Смена имени покемона (**PUT /pokemons** (*не забудь про нужный хэдер*))

В ответе (терминале) должен прийти объект json

- Поймать покемона в покебол (**POST /trainers/add_pokeball** (*не забудь про нужный хэдер*))

В ответе (терминале) должен прийти объект json

"""
import requests 

#создание тренера
URL = 'https://api.pokemonbattle.me:9104'
Header = {'Content-Type': 'application/json'}

#HEADER = {'Content-Type': 'application/json', 'trainer_token': '48c7c3d9319ea7a6514e70ea7f8ab4b7'}
#body = {
 #   "trainer_token": "48c7c3d9319ea7a6514e70ea7f8ab4b7",
  #  "email": "aikaulanbekova@mail.ru",
   # "password":"1377PFh"
 #}
#response = requests.post(url=f'{URL}/trainers/reg', json=body, headers=Header, timeout=5)
#print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')


#запрос всех тренеров
response = requests.get(url=f'{URL}/trainers', params= {'level': 1}, timeout=3)
print(f'Статус код: {response.status_code}.')
json_data = response.json()

if len('json_data') == 61:
   print ('Ok')
else:
   print ('Bad')


# создание покемона
BODY = {
     "name": "Вивальди",
     "photo": "https://dolnikov.ru/pokemons/albums/037.png"
 }
#response = requests.post(f'{URL}/pokemons', json=BODY, headers=HEADER, timeout=5)
#print(f'Статус код: {response.status_code}. Сообщение: {print(response.text)}')


#изменение имени покемона
#Bodyadd = {
#    "pokemon_id": "29331",
#    "name": "VoVa",
#    "photo": "https://dolnikov.ru/pokemons/albums/037.png"
# }
#response = requests.put(f'{URL}/pokemons', json=Bodyadd, headers=HEADER, timeout=5)
#print(f'Статус код: {response.status_code}. Сообщение: {print(response.text)}')


#поймать покемона в покебол
#BODYADD = {
#    "pokemon_id": "29331"
# }
#response = requests.post(f'{URL}/trainers/add_pokeball', json=BODYADD, headers=HEADER, timeout=5)
#print(f'Статус код: {response.status_code}. Сообщение: {print(response.text)}')