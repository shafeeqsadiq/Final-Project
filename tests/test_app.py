import unittest
from flask import json
from app import app

class TestListingsEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_all_listings(self):
        response = self.app.get('/listings')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        # Add more assertions based on your data structure and expectations

    def test_get_listing_by_id(self):
        response = self.app.get('/listings/5456')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data.decode('utf-8'))
        # Add more assertions based on your data structure and expectations

    def test_search_listings(self):
        response = self.app.post('/listings/search', json={"search_terms": ["2 bedroom", "condo"]})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        # Add more assertions based on your data structure and expectations

    def test_create_listing(self):
        new_listing = {
            "name": "New Listing",
            "host_id": 123,
            "neighbourhood": 12345,
            "latitude": "12.3456",
            "longitude": "-67.8901",
            "room_type": "Entire home/apt",
            "price": 150
        }
        response = self.app.post('/listings', json=new_listing)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data.decode('utf-8'))
        # Add more assertions based on your data structure and expectations

    def test_update_listing(self):
        updated_data = {
            "price": 200
        }
        response = self.app.patch('/listings/5456', json=updated_data)
        self.assertEqual(response.status_code, 404)
        # Add more assertions based on your data structure and expectations

    
    def test_delete_listing(self):
        response = self.app.delete('/listings/5456')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data.decode('utf-8'))
        # Add more assertions based on your data structure and expectations


if __name__ == '__main__':
    unittest.main()
