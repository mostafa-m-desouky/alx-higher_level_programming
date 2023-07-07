#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer function."""
    def test_max(self):
        """Test for max."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([1, 1, 1, 2]), 2)
        self.assertEqual(max_integer([1, 1, 2, 1]), 2)
        self.assertEqual(max_integer([1, 2, 1, 1]), 2)
        self.assertEqual(max_integer([2, 1, 1, 1]), 2)
        self.assertEqual(max_integer([1, 2, 3, 3]), 3)
        self.assertEqual(max_integer([1, 2, 3, 2]), 3)
        self.assertEqual(max_integer([1, 2, 2, 3]), 3)
        self.assertEqual(max_integer([1, 2, 2, 2]), 2)
        self.assertEqual(max_integer([2, 2, 2, 1]), 2)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
        self.assertEqual(max_integer([10, 9, 8, 7, 6, 5,
                                        4, 3, 2, 1]), 10)
        self.assertEqual(max_integer([1, 3, 5, 7, 9, 10,
                                        8, 6, 4, 2]), 10)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6,
                                        7, 8, 9, 10]), 10)
        self.assertEqual(max_integer([10, 9, 8, 7, 6, 5,
                                        4, 3, 2, 1]), 10)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6,
                                        7, 8, 9, 10]), 10)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6,
                                        7, 8, 9, 10]), 10)

    def test_empty(self):
        """Test for empty list."""
        self.assertEqual(max_integer([]), None)
    def test_type(self):
        """Test for type."""
        self.assertRaises(TypeError, max_integer, [1, 2, "Betty", 4])
        self.assertRaises(TypeError, max_integer, [1, 2, [1, 2], 4])
        self.assertRaises(TypeError, max_integer, [1, 2, (1, 2), 4])
        self.assertRaises(TypeError, max_integer, [1, 2, {1, 2}, 4])
        self.assertRaises(TypeError, max_integer, [1, 2, True, 4])
        self.assertRaises(TypeError, max_integer, [1, 2, 3, float('nan')])
        self.assertRaises(TypeError, max_integer, [1, 2, float('inf'), 4])
        self.assertRaises(TypeError, max_integer, [1, 2, float('inf'), 4])
        self.assertRaises(TypeError, max_integer, [1, 2, float('inf'), 4])
        self.assertRaises(TypeError, max_integer, [1, 2, float('inf'), 4])
        self.assertRaises(TypeError, max_integer, [1, 2, float('inf'), 4])
        self.assertRaises(TypeError, max_integer, [1, 2, float('inf'), 4])
        self.assertRaises(TypeError, max_integer, [1, 2, float('inf'), 4])
        self.assertRaises(TypeError, max_integer, [1, 2, float('inf'), 4])
        self.assertRaises(TypeError, max_integer, [1, 2, float('inf'), 4])
        self.assertRaises(TypeError, max_integer, [1, 2, float('inf'), 4])
