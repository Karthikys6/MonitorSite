import pytest
import os
from src import Status_Check

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

