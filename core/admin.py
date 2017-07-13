from django.contrib import admin

from .models import Marker, Product, Partner, Event, ProductSeries, MarkerType, Map

admin.site.register(Event)

admin.site.register(ProductSeries)
admin.site.register(Product)
admin.site.register(Partner)

admin.site.register(Marker)
admin.site.register(MarkerType)
#admin.site.register(Map)
