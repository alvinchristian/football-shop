from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Products
from .forms import ProductsForm
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
# Create your views here.
@login_required(login_url='/login')
def show_template(request):
    filter_type = request.GET.get('filter','all')
    
    if filter_type == 'all':
        product_list = Products.objects.all()
    else:
        product_list = Products.objects.filter(user=request.user)
    context = {
        'shop': 'FullTime Gear',
        'name': request.user.username,
        'class': 'PBP F',
        'products': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    
    return render(request, "template.html", context)

def show_xml(request):
    products = Products.objects.all()
    xml_data = serializers.serialize("xml", products)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Products.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'brand': product.brand,
            'sold': product.sold,
            'stock': product.stock,
            'user': product.user.username if product.user else None,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, id):
    products = Products.objects.get(id=id)
    xml_data = serializers.serialize("xml", [products])
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, id):
    try:
        product = Products.objects.select_related('user').get(id=id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'brand': product.brand,
            'sold': product.sold,
            'stock': product.stock,
            'user': product.user.username if product.user else None,
        }
        return JsonResponse(data)
    except Products.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

@login_required(login_url='/login')
def add_product(request):
    form = ProductsForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_template')
    
    context = {'form': form}
    return render(request, 'add_product.html', context)

def delete_product(request, id):
    product = get_object_or_404(Products, id=id)
    product.delete()
    return redirect('main:show_template')

def edit_product(request, id):
    product = get_object_or_404(Products, id=id)
    form = ProductsForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_template')
    
    context = {'form': form}
    return render(request, 'edit_product.html', context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Products, id=id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

def register(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})

    elif request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success", "message": "Account created successfully."}, status=201)

        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)

def login_user(request):
    if request.method == "GET":
        return render(request, "login.html")

    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            response = JsonResponse({"status": "success", "message": "Login successful."}, status=200)
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response

        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=401)

    return JsonResponse({"error": "Method not allowed"}, status=405)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(f"{reverse('main:login')}?logout=1")
    response.delete_cookie('last_login')
    return response


@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = request.POST.get("name")
    brand = request.POST.get("brand")
    price = request.POST.get("price")
    stock = request.POST.get("stock")
    category = request.POST.get("category")
    description = request.POST.get("description")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user

    new_product = Products(
        name=name,
        brand=brand,
        price=price,
        stock=stock,
        category=category,
        description=description,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()
    return HttpResponse(b"CREATED", status=201)


@csrf_exempt
@require_POST
def edit_product_ajax(request, id):
    product = get_object_or_404(Products, id=id)

    product.name = strip_tags(request.POST.get("name", product.name))
    product.brand = strip_tags(request.POST.get("brand", product.brand))
    product.price = strip_tags(request.POST.get("price", product.price))
    product.stock = strip_tags(request.POST.get("stock", product.stock))
    product.category = strip_tags(request.POST.get("category", product.category))
    product.description = strip_tags(request.POST.get("description", product.description))
    product.thumbnail = strip_tags(request.POST.get("thumbnail", product.thumbnail))
    product.is_featured = request.POST.get("is_featured") == 'on' if "is_featured" in request.POST else product.is_featured

    product.save()
    return HttpResponse(b"UPDATED", status=200)

@csrf_exempt
def delete_product_ajax(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Products, id=id)
        product.delete()
        return HttpResponse(b"DELETED", status=200)
    return HttpResponse(b"METHOD NOT ALLOWED", status=405)

