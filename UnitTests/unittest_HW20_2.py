import unittest

def formatted_name(first_name, last_name, middle_name=''):
    if len(middle_name) > 0:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


class TestFormattedName(unittest.TestCase):

    def test_first_last_name(self):
        result = formatted_name('john', 'doe')
        self.assertEqual(result, 'John Doe')

    def test_first_middle_last_name(self):
        result = formatted_name('john', 'doe', 'michael')
        self.assertEqual(result, 'John Michael Doe')

    def test_empty_middle_name(self):
        result = formatted_name('john', 'doe', '')
        self.assertEqual(result, 'John Doe')

    def test_whitespace_middle_name(self):
        result = formatted_name('john', 'doe', ' ')
        self.assertEqual(result, 'John Doe')

    def test_capitalization(self):
        result = formatted_name('ALICE', 'SMITH', 'ELIZA')
        self.assertEqual(result, 'Alice Eliza Smith')

    def test_names_with_spaces(self):
        result = formatted_name(' anna  ', '  ivanova ')
        self.assertEqual(result, 'Anna Ivanova')

    def test_all_whitespace(self):
        with self.assertRaises(ValueError):
            formatted_name('   ', '   ')
