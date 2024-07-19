


APlicacion Backend Python con Django 

para persistencia de base de datos se utilizo Mysql


directorio: ProyectoDjangoCodersNova
			\Back
Aplicacion		\myproject
modulo					\peliculas

en la aplicacion de peliculas creamos templates para diseñar un Fronted
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ayuda', views.ayuda, name='ayuda'),
    path('peliculas', views.peliculas, name='peliculas'),
    path('peliculas/agregar', views.agregar, name='agregar'),
    path('peliculas/editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    #get metodo para validar API
    path('peliculas-list', views.PeliculasList.as_view(), name='peliculas-list'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

ademas de esto fue creado un metodo API GET para consulta de Peliculas 


Dentro de la aplicacion Raiz, se continua manteniendo la parte de admisnitracion

urlpatterns = [
    path('', include('peliculas.urls')),
    path('admin/', admin.site.urls),
]
			