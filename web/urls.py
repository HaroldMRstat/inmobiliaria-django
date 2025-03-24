from django.urls import path
from .views import index, agentes, testimonios, lista_propiedades, login_view, formulario_contacto


urlpatterns = [
    path('', index, name='index'),  # Página principal
    path('agentes/', agentes, name='agentes'),
    path('propiedades/', lista_propiedades, name='lista_propiedades'),
    path('testimonios/', testimonios, name='testimonios'),
    path('login/', login_view, name='login'),
    path('formulario/', formulario_contacto, name='formulario_contacto'),
]