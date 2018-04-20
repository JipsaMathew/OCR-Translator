from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.get_form_data, name='name')
]
