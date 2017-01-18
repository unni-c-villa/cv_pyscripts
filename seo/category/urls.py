from django.conf.urls import url
from category import views

urlpatterns = [
    url(r'^category/getIntUrl/$', views.categorys_list),
    url(r'^category/getIntUrl/(?P<pk>[0-9]+)$', views.categorys_detail),
    url(r'^category/postIntUrl$', views.categorys_create),
    url(r'^category/putIntUrl/(?P<pk>[0-9]+)$', views.categorys_update),
    url(r'^category/putDomesticUrl/(?P<pk>[0-9]+)$', views.categorys_update_dom),
    url(r'^category/deleteUrl/(?P<pk>[0-9]+)$', views.categorys_soft_delete),
]