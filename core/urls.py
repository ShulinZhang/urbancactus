from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.default_index, name='index'),
    url(r'^(?P<ln>[\w-]+)?/$', views.index, name='index'),
    url(r'^(?P<ln>[\w-]+)/contact?/$', views.contact, name='contact'),

    url(r'^(?P<ln>[\w-]+)/spi?/$', views.spi_index, name='spi'),
    url(r'^(?P<ln>[\w-]+)/spi/map?/$', views.spi_map, name='spi-map'),

    url(r'^(?P<ln>[\w-]+)/n/products?/$', views.n_products, name='n-products'),

    url(r'^(?P<ln>[\w-]+)/events?/$', views.events_index, name='events'),
    url(r'^(?P<ln>[\w-]+)/events/archive?/$', views.events_archive, name='events-archive'),
    url(r'^(?P<ln>[\w-]+)/events/(?P<slug>[\w-]+)?/$', views.events_single, name='events-single'),
]
