from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_template, name='show_template'),
    path('add/', add_product, name='add_product'),
    path('product/<uuid:id>/', show_product, name='show_product'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete/<uuid:id>/', delete_product, name='delete_product'),
    path('edit/<uuid:id>/', edit_product, name='edit_product'),
    path('add_ajax/', add_product_ajax, name='add_product_ajax'),
    path('edit_ajax/<uuid:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('delete_ajax/<uuid:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('my-products-flutter/', flutter_list_user_products, name='list_user_products_flutter'),
]