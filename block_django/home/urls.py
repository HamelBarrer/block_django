from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('iniciar_sesion/', views.login_view, name='login'),
    path('cerrar_sesion/', views.logout_view, name='logout'),
    path('registro/', views.register_view, name='register'),
]
