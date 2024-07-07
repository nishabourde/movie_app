# api/test_views.py

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class UserRegistrationTestCase(APITestCase):
    def test_user_registration(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'password': 'testpass'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access_token', response.data)

class MovieListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_movie_list(self):
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('data', response.data)

class CollectionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_collection(self):
        url = reverse('collection-list-create')
        data = {
            'title': 'My Collection',
            'description': 'Description of my collection',
            'movies': [
                {
                    'title': 'Movie 1',
                    'description': 'Description 1',
                    'genres': 'Action',
                    'uuid': 'uuid1'
                }
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)

    def test_list_collection(self):
        url = reverse('collection-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)

    def test_update_collection(self):
        # Create a collection first
        collection_url = reverse('collection-list-create')
        data = {
            'title': 'My Collection',
            'description': 'Description of my collection',
            'movies': [
                {
                    'title': 'Movie 1',
                    'description': 'Description 1',
                    'genres': 'Action',
                    'uuid': 'uuid1'
                }
            ]
        }
        response = self.client.post(collection_url, data, format='json')
        collection_id = response.data['id']
        
        # Update the collection
        update_url = reverse('collection-detail', args=[collection_id])
        update_data = {
            'title': 'Updated Collection',
            'description': 'Updated description',
            'movies': [
                {
                    'title': 'Updated Movie 1',
                    'description': 'Updated Description 1',
                    'genres': 'Action',
                    'uuid': 'uuid1'
                }
            ]
        }
        response = self.client.put(update_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_collection(self):
        # Create a collection first
        collection_url = reverse('collection-list-create')
        data = {
            'title': 'My Collection',
            'description': 'Description of my collection',
            'movies': [
                {
                    'title': 'Movie 1',
                    'description': 'Description 1',
                    'genres': 'Action',
                    'uuid': 'uuid1'
                }
            ]
        }
        response = self.client.post(collection_url, data, format='json')
        collection_id = response.data['id']
        
        # Delete the collection
        delete_url = reverse('collection-detail', args=[collection_id])
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
