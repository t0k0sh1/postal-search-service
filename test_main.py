import unittest
import main

import json

class Test(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()

    def test_get(self):
        res = self.app.get('/?q={}'.format('142'))

        # assert HTTP status code.
        self.assertEqual(res.status_code, 200)

        # assert response data
        data = json.loads(res.data)
        self.assertEqual('1420041', data[0]['zipcode'])
        self.assertEqual('東京都', data[0]['pref_name'])
        self.assertEqual('トウキョウト', data[0]['pref_name_kana'])
        self.assertEqual('品川区', data[0]['city_name'])
        self.assertEqual('シナガワク', data[0]['city_name_kana'])
        self.assertEqual('戸越', data[0]['town_name'])
        self.assertEqual('トゴシ', data[0]['town_name_kana'])

if __name__ == '__main__':
    unittest.main()