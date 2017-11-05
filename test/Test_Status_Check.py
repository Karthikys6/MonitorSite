import pytest
import os
import Status_Check

def test_response_200():
    assert Status_Check.get_status('http://httpstat.us/200') == 200

def test_response_201():
    assert Status_Check.get_status('http://httpstat.us/201') == 201

def test_response_305():
    assert Status_Check.get_status('http://httpstat.us/305') == 305

def test_response_403():
    assert Status_Check.get_status('http://httpstat.us/403') == 403

def test_response_404():
    assert Status_Check.get_status('http://httpstat.us/404') == 404

def test_response_500():
    assert Status_Check.get_status('http://httpstat.us/500') == 500

def test_response_524():
    assert Status_Check.get_status('http://httpstat.us/524') == 524

def test_url_retrieve():
    assert Status_Check.read_urls(os.getcwd() + '/urls_test.txt') == ['http://httpstat.us/200','http://httpstat.us/201','http://httpstat.us/305','http://httpstat.us/403','http://httpstat.us/404','http://httpstat.us/500','http://httpstat.us/524']