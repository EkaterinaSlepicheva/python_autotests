import requests

token = '68c7adb0e662eb755c2a5ae8aeff664d'

add_pokemone_response = requests.post('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json', 
                                                                                             'trainer_token': token},
                                                                                             json = {"name": "Вупсень", 
                                                                                                   "photo": "https://dolnikov.ru/pokemons/albums/541.png"}) 

print (add_pokemone_response.text)

change_pokemon_response = requests.put('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json', 
                                                                                             'trainer_token': token},
                                                                                             json = {"pokemon_id": "12250",
                                                                                                     "name": "Пузырик",
                                                                                                     "photo": "https://dolnikov.ru/pokemons/albums/582.png"})

print (change_pokemon_response.text)

catch_pokemon_response = requests.post('https://pokemonbattle.me:9104//trainers/add_pokeball', headers = {'Content-Type': 'application/json', 
                                                                                             'trainer_token': token},
                                                                                             json = { "pokemon_id": "12250"})

print (catch_pokemon_response.text)