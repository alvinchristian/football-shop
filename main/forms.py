from django.forms import ModelForm
from main.models import Products

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ["name", "description", "price", "category", "thumbnail", "is_featured", "brand","stock"]


