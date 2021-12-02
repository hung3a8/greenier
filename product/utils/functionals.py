import geopy
from django.conf import settings
from geopy import distance

geolocator = geopy.geocoders.Nominatim(user_agent='greenier')


def calculate_price(price, rating, geocode1, geocode2):
    if rating >= 4:
        price = price * 0.88
    elif rating >= 3:
        price = price * 0.93

    # The function will reduce the price maximum by 50% if the distance between the two points is less than
    # settings.MAX_DISTANCE, otherwise it will significantly increase the price as bonus distance charge.
    d = distance.distance(geocode1, geocode2).km
    price = price - price / 2 * (1 - d / settings.MAX_DISTANCE)
    return price
