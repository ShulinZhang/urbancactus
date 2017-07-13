from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact?/$', views.contact, name='contact'),
    url(r'^spi?/$', views.spi, name='spi'),

    url(r'^map?/$', views.map, name='map'),
    #url(r'^map/(?P<slug>[\w-]+)?/$', views.one_map, name='map-single'),

    url(r'^products?/$', views.all_series, name='products-index'),
    url(r'^products/(?P<slug>[\w-]+)?/$', views.one_series, name='products-single'),
    url(r'^partners?/$', views.all_partners, name='partners-index'),
    url(r'^partners/(?P<slug>[\w-]+)?/$', views.one_partner, name='partners-single'),

    url(r'^events?/$', views.all_events, name='events-index'),
    url(r'^events/archive?/$', views.past_events, name='events-archive'),
    url(r'^events/(?P<slug>[\w-]+)?/$', views.one_event, name='events-single'),
]
