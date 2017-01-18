from django.conf.urls import url
from scripts import views

urlpatterns = [
    url(r'^scripts/category_international_mapping', views.category_mapping),
    url(r'^scripts/product_international_mapping', views.product_mapping),
]