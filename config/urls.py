from django.urls import path

from main import views


urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('new', views.contact_create, name='contact_create')
]
