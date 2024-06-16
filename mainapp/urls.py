from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('post/create', views.create_post, name= "post_create")
]