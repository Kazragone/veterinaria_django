from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dollar', views.dollar, name='dollar'),
    path('peliculas/<str:pelicula_nombre>/comentarios/<int:comentario_numero>', views.comentarios, name='comentarios'),
    path('animales/', views.animales, name='animales'),
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/<str:nro_documento>/', views.cliente, name='cliente'),
    path('animales/<str:animal_id>/', views.animal, name='animal'),
    path('crear_animal/', views.crear_animal, name='crear_animal'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('clientes/<str:cliente_id>/editar_cliente/', views.editar_cliente, name='editar_cliente'),
    path('animales/<str:animal_id>/editar_animal/', views.editar_animal, name='editar_animal'),
    path('clientes/eliminar_cliente/<str:nro_documento>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('animales/eliminar_animal/<str:animal_id>/', views.eliminar_animal, name='eliminar_animal'),
    path('consultas/', views.registro_de_consultas, name='consultas'),
    path('crear_consulta/', views.crear_consulta, name='crear_consulta'),
    path('consultas/eliminar_consulta/<str:consulta_id>/', views.eliminar_consulta, name='eliminar_consulta'),
    path('consultas/<str:consulta_id>/editar_consulta/', views.editar_consulta, name='editar_consulta'),
]
