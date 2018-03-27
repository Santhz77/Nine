import requests
import geocoder

import logging
log = logging.getLogger( __name__ )



def get_my_location():
    '''Get the co ordinates from the current location
    :return: (josn) the location co-ordinates
    '''

    my_coordinates = geocoder.ip('me')
    return my_coordinates


def getweather_info(API_KEY):
    '''
    This gets the weather info for the city.
    :param API_KEY:
    :param city_code:
    :return: (josn) The weather info
    '''
    my_coordinates = get_my_location()
    API_URL = "http://api.openweathermap.org/data/2.5/weather?units=metric&lat=" + str(my_coordinates.lat) + "&lon=" + str(my_coordinates.lng) +"&appid=" + API_KEY
    response = requests.get(API_URL)
    return response.text



