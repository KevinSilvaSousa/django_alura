from django.urls import path
from galeria.views import index, imagem, buscar

app_name = 'galeria'

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem.html'),
    path("buscar", buscar, name="buscar")
]