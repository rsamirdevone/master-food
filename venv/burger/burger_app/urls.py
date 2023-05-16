from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('/about', about, name='about'),
    path('/blog', blog, name='blog'),
    path('/booking', booking, name='booking'),
    path('/contact', contact, name='contact'),
    path('/feature', feature, name='feature'),
    path('/menu', menu, name='menu'),
    path('/single', single, name='single'),
    path('/team', team, name='team')
]
