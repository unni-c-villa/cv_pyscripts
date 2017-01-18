from django.conf.urls import url
from product import views

urlpatterns = [
    url(r'^product/getIntUrl/$', views.products_list),
    url(r'^product/getIntUrl/(?P<pk>[0-9]+)$', views.products_detail),
    url(r'^product/postIntUrl$', views.products_create),
    url(r'^product/putIntUrl/(?P<pk>[0-9]+)$', views.products_update),
    url(r'^product/putDomesticUrl/(?P<pk>[0-9]+)$', views.products_update_dom),
    url(r'^product/deleteUrl/(?P<pk>[0-9]+)$', views.products_soft_delete),
]