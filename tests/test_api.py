# -*- coding: utf-8 -*-
import gmapapi


def test_geocode():
    assert gmapapi.geocode('東京タワー')['status'] == 'OK' 

def test_reverse_geocode():
    assert gmapapi.reverse_geocode('35.669622,139.7432093')['status'] == 'OK'