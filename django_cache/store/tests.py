from django.test import TestCase

from .services import get_values_and_reset_ttl, get_values, set_keys_and_values, patch_keys_and_values

from django.core.cache import cache
cache.clear()

class StoreViewTest(TestCase):

    payload = {
        'key1': 'v1',
        'key2': 'v2',
        'key3': 'v3',
        'key4': 'v4',
        'key5': 'v5',
        'key6': 'v6',
        'key7': 'v7'}

    def setUp(self):
        set_keys_and_values(self.payload)

    def test_get_values(self):
        query_params = ['key1', 'key2', 'key3', 'key4', 'key5', 'key6','key7']
        output = ({
            'key1': 'v1',
            'key2': 'v2',
            'key3': 'v3',
            'key4': 'v4',
            'key5': 'v5',
            'key6': 'v6',
            'key7': 'v7'}, 200, {})
        result = get_values(query_params)
        self.assertEqual(result, output)

    def test_get_2_key_values(self):
        query_params = ['key1', 'key2']
        output = ({'key1': 'v1',
                   'key2': 'v2'}, 200, {})
        result = get_values(query_params)
        self.assertEqual(result, output)
    
    def test_set_keys_and_values_with_previous_value(self):
        payload = {
            'key7': 'v7',
            'key8': 'v8'
        }
        output = (200, {'key7': 'Key is already cached'})
        result = set_keys_and_values(payload)
        self.assertEqual(result, output)

    def test_patch_keys_and_values_with_new_value(self):
        payload = {
            'key10': 'v10'
        }
        output = (200, {'key10': 'Key is not patched'})
        result = patch_keys_and_values(payload)
        self.assertEqual(result, output)

    def test_get_1_key_values(self):
        query_params = ['key9']
        output = ({'key9': 'v9'}, 200, {})
        set_keys_and_values({'key9': 'v9'})
        result = get_values(query_params)
        self.assertEqual(result, output)

    def test_patch_keys_and_values_with_previous_value(self):
        payload = {
            'key9': 'v9-1'
        }
        output = (200, {})
        result = patch_keys_and_values(payload)
        self.assertEqual(result, output)