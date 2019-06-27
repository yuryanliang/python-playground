import unittest


class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)


        for i in range(0,4):
            with self.subTest(failed_number=i ):
                self.assertEqual(i%2, 0)