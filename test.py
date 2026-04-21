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

#The test results show whether the function works correctly. When the output says “Ran 2 tests – OK”, it means both tests passed and the function returned the expected results for the given inputs. If a test fails, it means there is a problem with the function or the expected value is incorrect. Overall, the tests confirm that the code behaves as expected.