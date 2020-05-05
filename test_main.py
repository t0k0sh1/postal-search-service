import unittest
import main

import json

class Test(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()

    def req(self, command):
        #data = Test.data.copy()
        #data['text'] = data['text'] + command
        return self.app.get('/?q={}', )

    def test_get(self):
        res = self.app.get('/?q={}'.format('232'))

        # assert HTTP status code.
        self.assertEqual(res.status_code, 200)

        # assert response data
        data = json.loads(res.data)
        self.assertEqual(data, list())


if __name__ == '__main__':
    unittest.main()