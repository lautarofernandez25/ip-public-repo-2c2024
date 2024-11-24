# capa de servicio/lógica de negocio

from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user

def getAllImages(input=None):
    # obtiene un listado de datos "crudos" desde la API, usando a transport.py.
    json_collection = []

    # recorre cada dato crudo de la colección anterior, lo convierte en una Card y lo agrega a images.
    images = []

    return images

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request del template en una Card.
    fav.user = '' # le asignamos el usuario correspondiente.

    return repositories.saveFavourite(fav) # lo guardamos en la base.

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            card = '' # transformamos cada favorito en una Card, y lo almacenamos en card.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.

import requests

def getAllImages(input=None): 

    api_url = "http://localhost:3000"
    api_data = requests.get(api_url).json()

    if input: 
        api_data = [item for item in api_data if input.lower in item["name"].lower()]

    cards = []
    for image in api_data: 
        card = {
            "id": image.get("id"), 
            "url": image.get("url"), 
            "name": image.get("name"), 
            "status": image.get("status"), 
            "last_location": image.get("last_location"), 
            "first_seen": image.get("first_seen"), 
            "image": image.get("image")
        } 
        cards.append(card) 
    
    return cards 

from app.layers.transport.transport import fetchImagesFromAPI 

def getAllImages(input=None): 

    api_data = fetchImagesFromAPI()

    if input: 
        api_data = [item for item in api_data if input.lower() in item["name"].lower()]

        images = []
        for item in api_data: 

            image_data = {
                "name": item.get("name", "No Name"), 
                "image": item.get("image", "default.jpg"), 
                "status": item.get("status", "unknown"), 
                "description": item.get("description", "No description available")
            }
            images.append(image_data)

        return images 
    
    import requests
    from app.config import config

    def fetchImagesFromAPI(): 

        response = requests.get(config.DEFAULT_REST_API_URL)
        return response.json() 
    
import requests

