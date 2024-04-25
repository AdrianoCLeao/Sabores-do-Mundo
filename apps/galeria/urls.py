from django.urls import path
from apps.galeria.views import index, imagem, buscar, nova_receita
from apps.galeria import views

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('filtrar-cards/<str:categoria>/', views.filtrar_cards, name='filtrar_cards'),
    path('nova-receita', nova_receita, name='nova_receita')
]