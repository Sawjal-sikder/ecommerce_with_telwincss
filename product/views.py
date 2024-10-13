from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CategoryForm


def categoryViews(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added successfully!")
            return redirect('category')
    else:
        form = CategoryForm()

    return render(request, 'category.html', {'form': form})
