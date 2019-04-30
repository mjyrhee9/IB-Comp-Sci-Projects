import unittest #module to run unit tests
import my_method

class TestAdd(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(my_method.add_me(1,2)3 'Output should be 3')
        self.assertEqual(my_method.add)

__name__ == '__main__':
    unittest.main()
