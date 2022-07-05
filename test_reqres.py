import unittest
from unittest.mock import patch
from reqres.data import getdata


class Test_GetData(unittest.TestCase):


    def test_getdata(self):

        fake_json = [{"Soumil":'Ok'}]

        with patch('reqres.data.requests') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = fake_json

        response = getdata()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), fake_json)



if __name__ == "__main__":
    unittest.main()

