from django.shortcuts import render
from product.models import Category


# Create your views here.
def homePages(request):
    categories = Category.objects.all().order_by('name')
    context = {
        'categories': categories,
    }
    return render(request, 'home.html', context)
