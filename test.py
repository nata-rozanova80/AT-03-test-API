import unittest
from unittest.mock import patch
from main import get_random_cat_image

class TestGetRandomCatImage(unittest.TestCase):

    @patch('requests.get')
    def test_successful_request(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'url': 'http://example.com/cat.jpg'}]
        url = get_random_cat_image()
        self.assertEqual(url, 'http://example.com/cat.jpg')

    @patch('requests.get')
    def test_unsuccessful_request(self, mock_get):
        mock_get.return_value.status_code = 404
        url = get_random_cat_image()
        self.assertIsNone(url)

if __name__ == '__main__':
    unittest.main()
