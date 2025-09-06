from django.urls import path
from main.views import show_template

app_name = 'main'

urlpatterns = [
    path('', show_template, name='show_template'),
]