from django.http import JsonResponse
from django.views import View
from django.core.cache import cache
import json

from .services import get_values_and_reset_ttl, get_values, set_keys_and_values, patch_keys_and_values

# Create your views here.

class StoreView(View):
    def get(self, request, *args, **kwargs):

        query_params = request.GET.get('keys')
        if query_params and type(query_params) == str:
            keys = query_params.split(',')
            payload, status_code, error = get_values_and_reset_ttl(keys)
        else:
            keys = cache.keys('*')
            payload, status_code, error = get_values(keys)
        return JsonResponse(payload)

    def post(self, request, *args, **kwargs):
        payload = request.body
        payload = json.loads(payload.decode('utf-8'))
        status_code, error = set_keys_and_values(payload)
        response = {
            'status_code': status_code,
        }
        if error:
            response['error'] = error
        return JsonResponse(response)

    def patch(self, request, *args, **kwargs):
        payload = request.body
        payload = json.loads(payload.decode('utf-8'))
        status_code, error = patch_keys_and_values(payload)
        response = {
            'status_code': status_code,
        }
        if error:
            response['error'] = error
        return JsonResponse(response)
