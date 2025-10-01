import unittest
from main import factorial, fibonacci, fizzbuzz

class TestAlgorithmFunctions(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_fibonacci_base_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_fizzbuzz_basic(self):
        result = fizzbuzz(5)
        expected = [1, 2, "Fizz", 4, "Buzz"]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()