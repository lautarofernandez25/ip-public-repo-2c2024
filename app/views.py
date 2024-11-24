# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.
# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.
def home(request):
    images = []
    favourite_list = []

    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })

def search(request):
    search_msg = request.POST.get('query', '')

    # si el texto ingresado no es vacío, trae las imágenes y favoritos desde services.py,
    # y luego renderiza el template (similar a home).
    if (search_msg != ''):
        pass
    else:
        return redirect('home')


# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    pass

from django.shortcuts import render 
import requests 

def home(request): 

    API_URL = "http://localhost:3000"

    try:
        response = requests.get(API_URL)
        response.raise_for_status()

        images = response.json()

    except Exception as e: 
        print(f"Error al obtener imagenes: {e}")
        images = [] 
    
    favorites = []

    context ={
        "images": images,
        "favorites": favorites
    }

    return render(request, "home.html", context) 

from django.shortcuts import render 
from app.config import config 

def fetchImagesFromAPI(): 

    response = requests.get(config.DEFAULT_REST_API_URL)
    return response.json()


def home(request): 

    images = fetchImagesFromAPI()
    print(images)

    context = {
        "images": images 
    }
    return render(request, "home.html", context) 

from django.shortcuts import render
import requests

def fetchImagesFromAPI():
    
    response = requests.get("http://localhost:3000") 
    return response.json() 


def mapToCard(api_data): 

    return {
        "id": api_data.get("id"),
        "image": api_data.get("image", ""),
        "name": api_data.get("name", "No Name Available"),
        "status": api_data.get("status", "unknown"), 
        "description": api_data.get("description", "No description available")
    }

def home(request): 

    images_data = fetchImagesFromAPI()

    images = [mapToCard(image) for image in images_data]

    context = {
        "images": images 
    } 

    return render(request, "home.html", context)