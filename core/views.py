from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import json

from .models import Product, ProductSeries, Event, MarkerType, Partner

def get_map_data(ln, map_slug=None):
    result = list()
    marker_types = None

    if map_slug is not None:
        map_object = Map.objects.get(slug=map_slug)

        if map_object.count > 0 and map_object.marker_type_set.count > 0:
            marker_types = map_object.marker_type_set

    if marker_types is None:
        marker_types = MarkerType.objects.all()

    for marker_type in marker_types:
        markers = list()

        for marker in marker_type.marker_set.all():
            markers.append({
                'name': marker.name,
                'description': marker.description,
                'latitude': marker.latitude,
                'longitude': marker.longitude,
                'link': marker.link,
            })

        name = ""

        if ln == 'en':
            name = marker_type.english_name
        else:
            name = marker_type.chinese_name

        result.append({
            'name': name,
            'icon': marker_type.icon,
            'colour': marker_type.colour,
            'markers': markers,
        })

    return result

# Special Pages
def index(request):
    ln = request.LANGUAGE_CODE
    today = date.today()
    js_data = {
        'map_types': get_map_data(ln),
        'disableMapScroll': True,
        'disableLocationDetection': True,
    }

    return render(request, ln+'/home.html', {
        'product_series': ProductSeries.objects.all()[:3],
        'events': Event.objects.filter(publish_date__lte=today)[:3],
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
        'js_data': json.dumps(js_data, cls=DjangoJSONEncoder),
    })

def about(request):
    ln = request.LANGUAGE_CODE
    today = date.today()

    return render(request, ln+'/about.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
    })

def contact(request):
    ln = request.LANGUAGE_CODE
    today = date.today()

    return render(request, ln+'/contact.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
    })

def spi(request):
    ln = request.LANGUAGE_CODE
    today = date.today()

    return render(request, ln+'/spi.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
        'partners': Partner.objects.filter(alliance_member=True),
    })

def sra(request):
    ln = request.LANGUAGE_CODE
    today = date.today()

    return render(request, ln+'/sra.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
        'partners': Partner.objects.filter(alliance_member=True),
    })

def map(request):
    ln = request.LANGUAGE_CODE
    today = date.today()
    js_data = { 'map_types': get_map_data(ln) }

    return render(request, ln+'/map.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
        'js_data': json.dumps(js_data, cls=DjangoJSONEncoder),
    })

def one_map(request, slug):
    ln = request.LANGUAGE_CODE
    today = date.today()
    js_data = { 'map_types': get_map_data(ln, slug) }

    return render(request, ln+'/map.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
        'js_data': json.dumps(js_data, cls=DjangoJSONEncoder),
    })

# Product Pages
def all_series(request):
    ln = request.LANGUAGE_CODE
    today = date.today()

    return render(request, ln+'/products/all-product-series.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
        'product_series': ProductSeries.objects.all(),
    })

def one_series(request, slug):
    ln = request.LANGUAGE_CODE
    today = date.today()

    return render(request, ln+'/products/one-product-series.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
        'series': ProductSeries.objects.get(slug=slug),
    })

def all_partners(request):
    ln = request.LANGUAGE_CODE
    today = date.today()

    return render(request, ln+'/products/all-partners.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
        'partners': Partner.objects.all(),
    })

def one_partner(request, slug):
    ln = request.LANGUAGE_CODE
    today = date.today()

    return render(request, ln+'/products/one-partner.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
        'partner': Partner.objects.get(slug=slug),
    })

# Events Pages
def all_events(request):
    ln = request.LANGUAGE_CODE
    today = date.today()

    future_events = Event.objects.filter(publish_date__lte=today, event_date__gte=today)

    return render(request, ln+'/events/all-events.html', {
        'product_series': ProductSeries.objects.all()[:3],
        'upcoming_events': future_events[:3],
        'future_events': future_events,
        'past_events': Event.objects.filter(publish_date__lte=today, event_date__lt=today)[:3],

        'events': Event.objects.all()
    })

def one_event(request, slug):
    ln = request.LANGUAGE_CODE
    today = date.today()

    return render(request, ln+'/events/one-event.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
        'event': Event.objects.get(slug=slug),
    })

def past_events(request):
    ln = request.LANGUAGE_CODE
    today = date.today()

    return render(request, ln+'/events/past-events.html', {
        'upcoming_events': Event.objects.filter(publish_date__lte=today, event_date__gte=today)[:3],
        'past_events': Event.objects.filter(publish_date__lte=today, event_date__lt=today),
    })
