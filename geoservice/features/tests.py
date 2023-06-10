import random

from django.contrib.gis.geos import GEOSGeometry
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import geopandas as gpd
from geoservice.features.models import Feature
from django.contrib.auth.models import User


class TestFeaturesBase(APITestCase):
    def setUp(self):
        self.path = '/Users/takrimrahmanalbi/Projects/AiInfraSolutions/GeoJson_File_Stroage/municipalities_nl (5).geojson'
        gdf = gpd.read_file(self.path)
        gdf_values = gdf.values
        self.feature_lst = [
            Feature(
                name=i[0],
                features=GEOSGeometry(str(i[1]))
            ) for i in gdf_values
        ]

        self.feature_objs = Feature.objects.bulk_create(self.feature_lst)
        self.user_payload = {
            'username': 'testuser',
            'password': '12345'
        }
        self.user = User.objects.create_user(**self.user_payload)
        self.token_url = reverse('token_obtain_pair')
        response = self.client.post(self.token_url, data=self.user_payload)
        self.headers = {
            'Authorization': f'Bearer {response.json().get("access")}',
            "Content-Type": "application/json"
        }
        self.base_url = '/main/features/'
        self.valid_id = random.choice(list(range(0, 355)))
        self.invalid_id = random.choice(list(range(356, 1000)))
        super(TestFeaturesBase, self).setUp()

    def tearDown(self):
        super(TestFeaturesBase, self).tearDown()


class FeatureListAPIViewTestCase(TestFeaturesBase):

    def test_get_feature_list(self):
        url = reverse('feature-list')
        response = self.client.get(url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_feature_list_with_bbox_filter(self):
        url = reverse('feature-list')
        params = {'xmin': 0, 'ymin': 0, 'xmax': 10, 'ymax': 10}
        response = self.client.get(url, params, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_feature_list_with_invalid_bbox_filter(self):
        url = reverse('feature-list')
        params = {'xmin': 10, 'ymin': 10, 'xmax': 0, 'ymax': 0}  # Invalid bbox values
        response = self.client.get(url, params, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.json().get('results'), [])

    def test_get_feature_list_with_no_results(self):
        url = reverse('feature-list')
        params = {'xmin': 100, 'ymin': 100, 'xmax': 110, 'ymax': 110}  # Bbox outside feature bounds
        response = self.client.get(url, params, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.json()), 0)


class FeatureRetrieveUpdateDestroyAPIViewTestCase(TestFeaturesBase):

    def test_get_feature(self):
        valid_id = Feature.objects.first().id
        url = f'{self.base_url}{valid_id}/'
        response = self.client.get(url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_feature(self):
        valid_id = Feature.objects.first().id
        url = f'{self.base_url}{valid_id}/'
        data = {"name": "Partial Update"}
        response = self.client.patch(url, json=data, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_feature(self):
        valid_id = Feature.objects.first().id
        url = f'{self.base_url}{valid_id}/'
        response = self.client.delete(url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_nonexistent_feature(self):
        invalid_id = random.choice(list(range(356, 1000)))
        url = f'{self.base_url}{invalid_id}/'
        response = self.client.get(url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_nonexistent_feature(self):
        invalid_id = random.choice(list(range(356, 1000)))
        url = f'{self.base_url}{invalid_id}/'
        data = {'name': 'Partial Update'}
        response = self.client.patch(url, data, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_nonexistent_feature(self):
        invalid_id = random.choice(list(range(356, 1000)))
        url = f'{self.base_url}{invalid_id}/'
        response = self.client.delete(url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
