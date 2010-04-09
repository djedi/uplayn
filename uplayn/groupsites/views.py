import urllib
from xml.dom import minidom

from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404

from uplayn.common import models as cmodels

def home(request):
    group = get_object_or_404(cmodels.GroupProfile, subdomain=request.subdomain)
    weather = google_weather(group)
    return direct_to_template(request, 'groupsites/home.html',
        {'group': group, 'weather': weather})

def location(request):
    group = get_object_or_404(cmodels.GroupProfile, subdomain=request.subdomain)
    return direct_to_template(request, 'groupsites/location.html',
        {'group': group})

def google_weather(group_profile):
    GOOGLE_WEATHER_URL = 'http://www.google.com/ig/api?weather=%s&hl=en'
    GOOGLE_IMG_ROOT = 'http://img0.gmodules.com'

    if group_profile.zip_code:
        url = GOOGLE_WEATHER_URL % group_profile.zip_code
    elif group_profile.city and group_profile.state:
        city_state = "%s,%s" % (group_profile.city, group_profile.state)
        url = GOOGLE_WEATHER_URL % urllib.quote(city_state)
    else:
        return None

    weather = {}
    dom = minidom.parse(urllib.urlopen(url))
    weather['city'] = get_data(dom, "city")
    weather['postal_code'] = get_data(dom, "postal_code")
    weather['forcast_date'] = get_data(dom, "forecast_date")
    weather['current_date_time'] = get_data(dom, "current_date_time")
    weather['condition'] = get_data(dom, "condition")
    weather['temp_f'] = get_data(dom, "temp_f")
    weather['humidity'] = get_data(dom, "humidity")
    weather['icon'] = GOOGLE_IMG_ROOT + get_data(dom, "icon")
    weather['wind_condition'] = get_data(dom, "wind_condition")
    forecasts = []
    for node in dom.getElementsByTagName("forecast_conditions"):
        forecast = {
            'day_of_week': get_data(node, "day_of_week"),
            'low': get_data(node, "low"),
            'high': get_data(node, "high"),
            'icon': GOOGLE_IMG_ROOT + get_data(node, "icon"),
            'condition': get_data(node, "condition"),
        }
        forecasts.append(forecast)
    weather['forecasts'] = forecasts
    return weather

def get_data(dom, tag):
    return dom.getElementsByTagName(tag)[0].getAttribute("data")
