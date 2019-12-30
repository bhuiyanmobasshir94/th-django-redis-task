from django.core.cache import cache
from django.conf import settings
from redis.exceptions import ConnectionError
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def get_values_and_reset_ttl(keys):
    payload, status_code, error = {}, 200, {}
    try:
        payload = cache.get_many(keys)
        error = dict.fromkeys({*keys} - {*payload}, "Key is not cached")
        for k in payload.keys():
            cache.touch(k, CACHE_TTL)
        if not payload:
            status_code = 204
    except ConnectionError:
        error = 'Service Unavailable'
        status_code = 503
    except Exception as e:
        error = 'Internal Server Error'
        status_code = 500
    return dict(payload), status_code, error

def get_values(keys):
    payload, status_code, error = {}, 200, {}
    try:
        payload = cache.get_many(keys)
        error = dict.fromkeys({*keys} - {*payload}, "Key is not cached")
        if not payload:
            status_code = 204
    except ConnectionError:
        error = 'Service Unavailable'
        status_code = 503
    except Exception as e:
        error = 'Internal Server Error'
        status_code = 500
    return dict(payload), status_code, error

def set_keys_and_values(payload):
    status_code, error = 200, {}
    try:
        existed_keys = cache.get_many(payload.keys())
        if existed_keys:
            error = dict.fromkeys({*existed_keys}, "Key is already cached")
            for k in existed_keys.keys():
                payload.pop(k)
            cache.set_many(payload, timeout=CACHE_TTL)
        else: 
            cache.set_many(payload, timeout= CACHE_TTL)
    except ConnectionError:
        error = 'Service Unavailable'
        status_code = 503
    except Exception:
        error = 'Internal Server Error'
        status_code = 500
    return status_code, error

def patch_keys_and_values(payload):
    status_code, error = 200, {}
    try:
        existed_keys = cache.get_many(payload.keys())
        if existed_keys:
            cache.delete_many(existed_keys.keys())
            new_payload = {}
            for k in existed_keys.keys():
                new_payload[k] = payload[k]
            cache.set_many(new_payload, timeout=CACHE_TTL)
        patched_keys = cache.get_many(payload.keys())
        error = dict.fromkeys({*payload} - {*patched_keys}, "Key is not patched")
    except ConnectionError:
        error = 'Service Unavailable'
        status_code = 503
    except Exception as ex:
        error = 'Internal Server Error'
        status_code = 500
    return status_code, error
