from django.contrib import admin

from .models import MapMarker, Product, Partner, Event, ProductSeries, MapType

admin.site.register(Product)
admin.site.register(Partner)
admin.site.register(Event)
admin.site.register(MapMarker)

admin.site.register(ProductSeries)
admin.site.register(MapType)
