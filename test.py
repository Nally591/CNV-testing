import unittest
from my_sum import sum

class TestSum(unittest.TestCase):

    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)



    def test_tuple_int(self):
        data = (1, 2, 2)
        result = sum(data)
        self.assertEqual(result, 7)  # This will fail at first

if __name__ == "__main__":
    unittest.main()