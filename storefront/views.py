from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.db.models import Q
# ORM for testing purpose


def say_hello(request):
    # Practising ORM
    # queryset = Product.objects.filter(unit_price__range=(20,30))
    # queryset = Product.objects.filter(collection__id__range=(1,2,3))
    #  queryset = Product.objects.filter(title__startswith='coffee')
    # queryset = Product.objects.filter(title__icontains='coffee')
    # queryset = Product.objects.filter(description__isnull=True)
    # queryset = Product.objects.filter(last_update__year=2021)
    # queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))
   queryset = Product.objects.all()[10:]
   return render(request, "say_hello.html", {"name": "Faizan", 'products': list(queryset)})


def index(request):
    return render(request, "index.html")


def about_us(request):
    return render(request, "about-us.html")


def blog_post(request):
    return render(request, "blog-post.html")


def blog_v01(request):
    return render(request, "blog-v01.html")


def blog_v02(request):
    return render(request, "blog-v02.html")


def blog_v03(request):
    return render(request, "blog-v03.html")


def category_grid_3_cols(request):
    return render(request, "category-grid-3-cols.html")


def category_grid_left_sidebar(request):
    return render(request, "category-grid-left-sidebar.html")


def category_grid_right_sidebar(request):
    return render(request, "category-grid-right-sidebar.html")


def category_grid(request):
    return render(request, "category-grid.html")


def category_list_left_sidebar(request):
    return render(request, "category-list-left-sidebar.html")


def category_list_right_sidebar(request):
    return render(request, "category-list-right-sidebar.html")


def category_list(request):
    return render(request, "category-list.html")


def checkout(request):
    return render(request, "checkout.html")


def contact(request):
    return render(request, "contact.html")


def home_01(request):
    return render(request, "home-01.html")


def home_02(request):
    return render(request, "home-02.html")


def home_03(request):
    return render(request, "home-03.html")


def home_03_green(request):
    return render(request, "home-03-green.html")


def home_04(request):
    return render(request, "home-04.html")


def home_04_light(request):
    return render(request, "home-04-light.html")


def home_05(request):
    return render(request, "home-05.html")


def index_2(request):
    return render(request, "index-2.html")


def landing(request):
    return render(request, "landing.html")


def login(request):
    return render(request, "login.html")


def shopping_cart(request):
    return render(request, "shopping-cart.html")


def single_product_external(request):
    return render(request, "single-product-external.html")


def single_product_grouped(request):
    return render(request, "single-product-grouped.html")


def single_product_onsale(request):
    return render(request, "single-product-onsale.html")


def single_product_simple(request):
    return render(request, "single-product-simple.html")


def single_product(request):
    return render(request, "single-product.html")


def error_404(request):
    return render(request, "404.html")
