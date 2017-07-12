from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import json

from .models import Product, ProductSeries, Event, MapType

def get_map_data():
    result = list()

    for map_type in MapType.objects.all():
        markers = list()

        for marker in map_type.mapmarker_set.all():
            markers.append({
                'name': marker.name,
                'description': marker.description,
                'latitude': marker.latitude,
                'longitude': marker.longitude,
                'link': marker.link,
            })

        result.append({
            'name': map_type.name,
            'icon': map_type.icon,
            'colour': map_type.colour,
            'markers': markers,
        })

    return result

# Special Pages
def default_index(request):
    return index(request, 'cn')

def index(request, ln):
    today = date.today()
    js_data = {
        'map_types': get_map_data(),
        'disableMapScroll': True,
        'disableLocationDetection': True,
    }

    return render(request, ln+'/index.html', {
        'product_series': ProductSeries.objects.all()[:3],
        'events': Event.objects.filter(publish_date__lte=today)[:3],
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
        'js_data': json.dumps(js_data, cls=DjangoJSONEncoder),
    })

def contact(request, ln):
    today = date.today()

    return render(request, ln+'/contact.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
    })

# SPI Pages
def spi_index(request, ln):
    today = date.today()

    return render(request, ln+'/spi/index.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
    })

def spi_map(request, ln):
    today = date.today()
    js_data = { 'map_types': get_map_data() }

    return render(request, ln+'/spi/map.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
        'js_data': json.dumps(js_data, cls=DjangoJSONEncoder),
    })

# N# Pages
def n_products(request, ln):
    today = date.today()

    return render(request, ln+'/n/products.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
        'product_series': ProductSeries.objects.all(),
    })

# Events Pages
def events_index(request, ln):
    today = date.today()

    future_events = Event.objects.filter(publish_date__lte=today, event_date__gte=today)

    return render(request, ln+'/events/index.html', {
        'product_series': ProductSeries.objects.all()[:3],
        'upcoming_events': future_events[:3],
        'future_events': future_events,
        'past_events': Event.objects.filter(publish_date__lte=today, event_date__lt=today)[:3],

        'events': Event.objects.all()
    })

def events_single(request, ln, slug):
    today = date.today()

    return render(request, ln+'/events/single.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
        'event': Event.objects.get(slug=slug),
    })

def events_archive(request, ln):
    today = date.today()

    return render(request, ln+'/events/archive.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
        'past_events': Event.objects.filter(publish_date__lte=today, event_date__lt=today),
    })
