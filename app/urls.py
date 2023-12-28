
from django.urls import path, re_path

from .views import (
    login_view, 
    logout_view,
    register_view,
    index,
    create_post_view
    )

urlpatterns = [
    # admin
    path('login/', login_view, name='login'),

    #authentication
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('', index, name='index'),
    path('about', login_view, name='about'),
    path('create-post', create_post_view, name='create-post'),
    path('contact', login_view, name='contact'),
    path('blog', login_view, name='blog'),
    
]
