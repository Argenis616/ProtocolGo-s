import pokepy
import urllib
from requests import get
import random

def obtain_ip_address():
    """
    We can get the public id
    """
    ip = 0
    try:    
        ip = get('https://api.ipify.org').text
    except Exception as err:
        print (err)
    finally:
        return ip


def obtain_img_pokemon(pokemon,ruta=""):
    """
    We can get pokemon's image
    Args:
        pokemon:  We pass the pokemon as a parameter.
        ruta : We pass the route as a parameter.
    """
    poke = pokepy.V2Client().get_pokemon(pokemon)
    url = poke.sprites.front_default
    urllib.request.urlretrieve(url,ruta + str(pokemon) + ".png")
    return url,ruta

def show_name(pokemon):
    """
    This function shows the pokemon
    Args:
        pokemon:  We pass the pokemon as a parameter.
    """
    poke = pokepy.V2Client().get_pokemon(pokemon)
    name = poke.name
    return name

def show_id(pokemon):
    """
    We show the pokemon's identification
    Args:
        pokemon:  We pass the pokemon as a parameter.
    """
    poke = pokepy.V2Client().get_pokemon(pokemon)
    id_poke = poke.id
    return id_poke