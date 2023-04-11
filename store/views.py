from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Category, Product, Brand

# Create your views here.


def index(request):
    categories = Category.objects.all()

    products = Product.objects.all()

    context ={
        'categories': categories,
        'products': products
    }
    return render(request, 'home/index.html', context)



def shopPage(request):
    data = Product.objects.all().order_by('price')

    paginator = Paginator(data, 24) # Show 24 contacts per page.

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context ={
        'products': products
    }

    return render(request, 'shop/index.html', context)


def singleProduct(request, slug):
    product = Product.objects.get(slug=slug)
    products = Product.objects.filter(category=product.category).order_by('-id')[:5]

    context = {
        'product': product,
        'products':products
    }
    return render(request, 'shop/show.html', context)


def category(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }
    return render(request, 'category/index.html', context)


def singleCategory(request, slug):
    category = Category.objects.get(slug=slug)

    data = Product.objects.filter(category=category).order_by('price')

    paginator = Paginator(data, 24) # Show 24 contacts per page.

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'category': category,
        'products': products
    }

    return render(request, 'category/show.html', context)


def singleBrand(request, slug):
    brand = Brand.objects.get(slug=slug)

    data = Product.objects.filter(brand=brand).order_by('price')

    paginator = Paginator(data, 24) # Show 24 contacts per page.

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'category': category,
        'products': products
    }

    context ={
        'brand': brand,
        'products': products
    }

    return render(request, 'brand/index.html', context)