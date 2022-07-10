import unittest


# Running Test:
# unittest.main() RUN button, click button near to def and class
# python test_exercise.py
# Another way to run tests with the unittest module is by using it with the Python executable.
# This time, it isn't necessary to specify the filename because tests can be discovered automatically:
# python -m unittest


class TestAssertions(unittest.TestCase):

    def test_equals(self):
        self.assertEqual("one string", "one string")


def str_to_bool(value):
    # value = value.lower()
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False

# advanced_method
# In this case, the function being tested only works with strings, so using any other type as input would cause
# an unhandled exception to be raised.
# Update the function so that it raises an AttributeError if a non-string value is used. This can be detected
# by catching an AttributeError when calling value.lower() because only strings have a lower() method:
def str_to_bool_adv(value):
    try:
        value = value.lower()
    except AttributeError:
        raise AttributeError(f"{value} must be of type string")
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False

class TestStrToBool(unittest.TestCase):

    def test_y_is_true(self):
        result = str_to_bool('y')
        self.assertTrue(result)

    def test_Yes_is_true(self):
        result = str_to_bool('Yes')
        self.assertTrue(result)

    def test_yes_is_true(self):
        result = str_to_bool('yes')
        self.assertTrue(result)

    def test_invalid_input(self):
        with self.assertRaises(AttributeError):
            str_to_bool_adv(1)

if __name__ == '__main__':
    unittest.main()