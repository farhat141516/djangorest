from rest_framework import status
from rest_framework.test import APITestCase


class StudentApiTests(APITestCase):
    list_url = '/api/students/'

    def test_homepage_redirects_to_swagger_docs(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response['Location'], '/api/docs/')

    def test_student_api_has_one_canonical_route(self):
        self.assertEqual(
            self.client.get('/api/').status_code,
            status.HTTP_404_NOT_FOUND,
        )
        self.assertEqual(
            self.client.get('/students/students/').status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_list_and_create_students(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [])

        response = self.client.post(
            self.list_url,
            {'name': 'Farhat', 'age': 20},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['cours'], 'Python')
        self.assertTrue(response.json()['is_active'])

        response = self.client.get(self.list_url)
        self.assertEqual(len(response.json()), 1)

    def test_retrieve_put_patch_and_delete_student(self):
        create_response = self.client.post(
            self.list_url,
            {'name': 'Farhat', 'age': 20},
            format='json',
        )
        student_url = f"{self.list_url}{create_response.json()['id']}/"

        response = self.client.get(student_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.put(
            student_url,
            {
                'name': 'Shahida',
                'age': 22,
                'cours': 'Django',
                'is_active': True,
            },
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'Shahida')

        response = self.client.patch(
            student_url,
            {'age': 23},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['age'], 23)

        response = self.client.delete(student_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(
            self.client.get(student_url).status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_invalid_student_data_returns_validation_error(self):
        response = self.client.post(
            self.list_url,
            {'name': '', 'age': 'not-an-integer'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
