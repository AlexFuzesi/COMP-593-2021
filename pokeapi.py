import requests

def get_pokemon_info(name):
    """"

    Gets a Dictionary of information from the pokiApi fro specified pokemon. 

    :parm name: pokemons name (or poke index)
    :returns:dict: Dictionary of pokemon information if syccesful;none if unsuccesfule  
    """

    print("Getting Pokemong information...", end='')

    name = name.lower().strip()

    URL = 'https://pokeapi.co/api/v2/pokemon/' + str(name)

    if response.status_code == 200:
        print('success')
        return respones.json()
    else:
        print('failed. Response code:', response.status_code)
        return 


def get_pokemon_list(limit=2000, offset=0):
     """"

    Gets a list of limit of the pokemnn from the pokiApi 
     
    :parm name: limit gives limit to how mnay pokemon to put into the list 
    :parm name: offset of where to start 
    :returns: results of the pokemon getting a list of all pokemon   
    """

     URL = 'https://pokeapi.co/api/v2/pokemon/' + str(name)
     #limit how many pokemon to put in the list 
     params = {'limit': limit, 'offset': offset}
     response = requests.get(URL, params=params)

    if response.status_code == 200:
        print('success')
        poke_dict = respones.json()
        return [p['name']for p in poke_dict['results']]
    else:
        print('failed. Response code:', response.status_code)


def get_pokemon_image_url(name):
     """"
    Gets a png image of a pokemon from the pokiApi fro specified pokemon. 

    :parm name: pokemons name (or poke index)
    :returns:poke_url: this gives us the path way to get the officAL-ART of the pokemon from poke api   
    """
    #how we get the pokemon image from the pokiApi
    poke_dict = get_pokemon_info(name)
    if poke_dict:
        poke_url = poke_dict['sprites']['other']['official-artwork']['front_default']
        return poke_url