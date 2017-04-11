# -*- coding: utf-8 -*-

import requests
import nose
from nose import with_setup

from django.test import TestCase


domain = 'http://localhost:8000'

def setup_module():
    pass

def teardown_module():
    pass

def setup():
    pass

def teardown():
    pass

def test_session():
    url = '{domain}/cache/session/'.format(domain=domain)
    resp = requests.get(url)
    assert(resp.status_code==200)