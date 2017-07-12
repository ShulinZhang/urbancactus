from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact?/$', views.contact, name='contact'),

    url(r'^spi?/$', views.spi_index, name='spi'),
    url(r'^spi/map?/$', views.spi_map, name='spi-map'),

    url(r'^n/products?/$', views.n_products, name='n-products'),

    url(r'^events?/$', views.events_index, name='events'),
    url(r'^events/archive?/$', views.events_archive, name='events-archive'),
    url(r'^events/(?P<slug>[\w-]+)?/$', views.events_single, name='events-single'),
]
