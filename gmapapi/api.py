# -*- coding: utf-8 -*-
import os
import json
import requests
import urllib.parse
from time import sleep
from .exceptions import *

KEY = os.environ.get("GMAP_API_KEY", None)
GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
LANGUAGE = 'ja'

def _request(url):
    try:
        response = requests.get(url)
        body = response.json()
        api_status = body["status"]
        if api_status == "OK":
            return body
        else:
            if "error_message" in body:
                raise ApiError(api_status, body["error_message"])
            raise ApiError(api_status)
  
    except requests.exceptions.Timeout:
        raise Timeout()

    except Exception as e:
        raise TransportError(e)


def geocode(address):
    params = {
        'language': LANGUAGE,
        'address': address,
        'key': KEY
    }
    url = GOOGLE_MAPS_API_URL +  '?' + urllib.parse.urlencode(params)
    ret = _request(url)
    return ret

def reverse_geocode(latlng):
    params = {
        'language': LANGUAGE,
        'latlng': latlng,
        'key': KEY
    }
    url = GOOGLE_MAPS_API_URL +  '?' + urllib.parse.urlencode(params, safe=',')
    ret = _request(url)
    return ret
