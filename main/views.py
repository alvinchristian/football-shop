from django.shortcuts import render

# Create your views here.
def show_template(request):
    context = {
        'name': 'Alvin Christian Halim',
        'class': 'PBP F'
    }

    return render(request, "template.html", context)