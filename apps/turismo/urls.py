from django.urls import path
from .views import inicio_view, login_view, logout_view, registro_view, categorias_view, categoria_agregar_view, categoria_editar_view, categoria_eliminar_view, mis_sitios_view, sitio_agregar_view, sitio_editar_view, sitio_eliminar_view, reportes_view

urlpatterns = [
    path('',inicio_view, name='inicio'),

    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("registro/", registro_view, name="registro"),

    path("categorias/", categorias_view, name="categorias"),
    path("categoria_agregar/", categoria_agregar_view, name="categoria_agregar"),
    path("categoria_editar/<int:id_categoria>", categoria_editar_view, name="categoria_editar"),
    path("categoria_eliminar/<int:id_categoria>", categoria_eliminar_view, name="categoria_eliminar"),

    path("mis_sitios/", mis_sitios_view, name="mis_sitios"),
    path("sitio_agregar/", sitio_agregar_view, name="sitio_agregar"),
    path("sitio_editar/<int:id_sitio>", sitio_editar_view, name="sitio_editar"),
    path("sitio_eliminar/<int:id_sitio>", sitio_eliminar_view, name="sitio_eliminar"),

    path("reportes/", reportes_view, name="reportes"),
    
]