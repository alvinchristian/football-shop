from django.shortcuts import render

# Create your views here.
def show_template(request):
    context = {
        'shop': 'Full Time Gear',
        'name': 'Alvin Christian Halim',
        'class': 'PBP F'
    }

    return render(request, "template.html", context)