import json

import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


@pytest.mark.django_db
class TestApiClient(APITestCase):

    def __int__(self):
        self.client = APIClient()

    def test_create_product(self):
        url = reverse('product:create')
        data = {'title': 'test', 'description': 'test', 'price': 12.2}
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
