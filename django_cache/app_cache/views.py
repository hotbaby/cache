# -*- coding:utf-8 -*-

import logging
from django.shortcuts import render
from django.core.cache import cache
from django.http import HttpResponse
from django.views.decorators.http import require_GET

EXPIRE_TIME = 30

_logger = logging.getLogger('app_cache')

@require_GET
def session(request):
    session = cache.get('session')
    if not session:
        session = cache.set('session', 'hotbaby', timeout=EXPIRE_TIME) 
        _logger.debug('cache not hit')
    else:
        _logger.debug('cache hit')
    return HttpResponse(content=session)