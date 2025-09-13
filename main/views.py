from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .models import Products
from .forms import ProductsForm
# Create your views here.
def show_template(request):
    product_list = Products.objects.all()
    context = {
        'shop': 'Full Time Gear',
        'name': 'Alvin Christian Halim',
        'class': 'PBP F',
        'products': product_list
    }

    
    return render(request, "template.html", context)

def show_xml(request):
    products = Products.objects.all()
    xml_data = serializers.serialize("xml", products)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products = Products.objects.all()
    json_data = serializers.serialize("json", products)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, id):
    products = Products.objects.get(id=id)
    xml_data = serializers.serialize("xml", [products])
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, id):
    products = Products.objects.get(id=id)
    json_data = serializers.serialize("json", [products])
    return HttpResponse(json_data, content_type="application/json")

def add_product(request):
    form = ProductsForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_template')
    
    context = {'form': form}
    return render(request, 'add_product.html', context)

def show_product(request, id):
    product = get_object_or_404(Products, id=id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

