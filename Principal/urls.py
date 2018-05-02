from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^productos', views.ProductList.as_view(), name='Persona-list'),
]


