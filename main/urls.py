from django.urls import path
from main.views import show_template, show_xml, show_json, show_xml_by_id, show_json_by_id, add_product, show_product

app_name = 'main'

urlpatterns = [
    path('', show_template, name='show_template'),
    path('add/', add_product, name='add_product'),
    path('product/<int:id>/', show_product, name='show_product'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]