# python -m unittest TO USE AUTO TEST DISCOVERY

# The class and method names are following a test convention. The convention is that they need to be prefixed
# with test. Although it isn't required, test classes use camel-casing, and test methods are lower-case, and
# words are separate with an underscore. For example, the following is how a test for customer accounts that
# verify creation and deletion could look:

import unittest

class TestAccounts(unittest.TestCase):

    def test_creation(self):
        self.assertTrue(account.create())

    def test_deletion(self):
        self.assertTrue(account.delete())


# Assertions and assert methods
# It's essential to use assert methods instead of Python's built-in assert() function to have rich reporting when
# failures happen. The test_assertion.py uses self.assertEqual(), one of the many special methods from the
# unittest.TestCase class to ensure that two values are equal:
# self.assertEqual("one string", "one string")
# In this case, both strings are equal, so the test passes. Testing equality is one of the many different
# assertions that the unittest.TestCase class offers. Although there are more than 30 assert methods, the
# following are most commonly used aside from self.assertEqual():
# self.assertTrue(value): Ensure that value is true.
# self.assertFalse(value): Ensure that value is false.
# self.assertNotEqual(a, b): Check that a and b aren't equal.