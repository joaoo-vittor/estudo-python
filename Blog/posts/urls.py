from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('categoria/<str:categoria>',
         views.PostCategorias.as_view(), name='post_categoria'),
    path('busca/', views.PostBusca.as_view(), name='post_busca'),
    path('detalhes/<int:pk>', views.PostDetalhes.as_view(), name='post_detalhes'),
]
