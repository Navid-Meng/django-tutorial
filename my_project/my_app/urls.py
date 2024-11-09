from django.urls import path
from . import views

urlpatterns = [
    path(route='home/', view=views.home, name='home'),
    path(route='products/', view=views.items, name='products')
]

'''
    localhost:8000/myapp/home
    localhost:8000/myapp/products

'''