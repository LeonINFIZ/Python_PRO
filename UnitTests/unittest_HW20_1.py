import unittest

class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]



class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.fib = Fibonacci()

    def test_base_cases(self):
        self.assertEqual(self.fib(0), 0)
        self.assertEqual(self.fib(1), 1)

    def test_recursive_cases(self):
        self.assertEqual(self.fib(2), 1)
        self.assertEqual(self.fib(3), 2)
        self.assertEqual(self.fib(4), 3)
        self.assertEqual(self.fib(5), 5)
        self.assertEqual(self.fib(10), 55)
        self.assertEqual(self.fib(15), 610)

    def test_cache_growth(self):
        self.fib(10)
        self.assertGreaterEqual(len(self.fib.cache), 11)
        self.assertEqual(self.fib.cache[10], 55)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.fib(-1)
        with self.assertRaises(ValueError):
            self.fib("string")
        with self.assertRaises(ValueError):
            self.fib(3.5)
        with self.assertRaises(ValueError):
            self.fib(None)

    def test_large_input(self):
        self.assertEqual(self.fib(30), 832040)
