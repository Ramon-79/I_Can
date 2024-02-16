from django.shortcuts import render

from blog import models


def index(request):
    category_list = models.CategoryModel.objects.all()

    context = {
        'category_list': category_list,
    }

    return render(request,
                  'blog/base.html',
                  context)


def category_page(request, pk, slug):
    category = models.CategoryModel.objects.get(pk=pk)

    context = {
        'category': category,
    }

    return render(request,
                  'blog/category_page.html',
                  context)

# Create your views here.
