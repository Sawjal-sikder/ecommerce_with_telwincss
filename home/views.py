from django.shortcuts import render


# Create your views here.
def homePages(request):
    return render(request, 'base.html')
