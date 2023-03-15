from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="index"),
path("say_hello", views.say_hello, name= "say_hello"),
path("index.html/", views.index, name="index"),
path("about-us.html/", views.about_us, name="about-us"),
path("blog-post.html/", views.blog_post, name="blog-post"),
path("blog-v01.html/", views.blog_v01, name="blog-v01"),
path("blog-v02.html/", views.blog_v02, name="blog-v02"),
path("blog-v03.html/", views.blog_v03, name="blog-v03"),
path("category-grid-3-cols.html/", views.category_grid_3_cols, name="category_grid_3_cols"),
path("category-grid-left-sidebar.html/", views.category_grid_left_sidebar,name="category_grid_left_sidebar"),
path("category-grid-right-sidebar.html/", views.category_grid_right_sidebar,name="category_grid_right_sidebar"),
path("category-grid.html/", views.category_grid, name="category_grid"),
path("category-list-left-sidebar.html/", views.category_list_left_sidebar,name="category_list_left_sidebar"),
path("category-list-right-sidebar.html/", views.category_list_right_sidebar,name="category_list_right_sidebar"),
path("category-list.html/", views.category_list, name="category_list"),
path("checkout.html/", views.checkout, name="checkout"),
path("contact.html/", views.contact, name="contact"),
path("home-01.html/", views.home_01, name="home_01"),
path("home-02.html/", views.home_02, name="home_02"),
path("home-03.html/", views.home_03, name="home_03"),
path("home-03-green.html", views.home_03_green, name="home-03-green.html"),
path("home-04.html/", views.home_04, name="home_04"),
path("home-04-light.html/", views.home_04_light, name="home-04-light.html"),
path("home-05.html/", views.home_05, name="home_05"),
path("contact.html/", views.contact, name="contact"),
path("index-2.html/", views.index_2, name="index_2"),
path("landing.html/", views.landing, name="landing"),
path("login.html/", views.login, name="login"),
path("shopping-cart.html/", views.shopping_cart, name="shopping_cart"),
path("single-product-external.html/", views.single_product_external,name="single_product_external"),
path("single-product-grouped.html/", views.single_product_grouped,name="single_product_grouped"),
path("single-product-onsale.html/", views.single_product_onsale,name="single_product_onsale"),
path("single-product-simple/", views.single_product_simple,name="single_product_simple"),
path("single-product.html/", views.single_product, name="single_product"),
path("404.html/", views.error_404, name="error_404"),

]





