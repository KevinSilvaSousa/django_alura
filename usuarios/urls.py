from django.urls import path
from usuarios.views import login, cadastro, buscar

app_name = 'usuarios'

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
        path('buscar', buscar, name='buscar'),

]