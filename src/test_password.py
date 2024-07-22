import unittest
from password import PasswordGenerator


class PasswordTests(unittest.TestCase):
    def test_length(self):
        gen_pass = PasswordGenerator()
        test_pass = gen_pass.generate_password(8, 0, 0)
        test_case = "abcd1234"
        self.assertEqual(len(test_case), len(test_pass))

    def test_numbers(self):
        gen_pass = PasswordGenerator()
        test_pass = gen_pass.generate_password(8, 1, 0)
        self.assertRegex(test_pass, r'[a-zA-Z0-9]{8}')

    def test_symbols(self):
        gen_pass = PasswordGenerator()
        test_pass = gen_pass.generate_password(8, 0, 1)
        self.assertRegex(test_pass, r'\D{8}')


if __name__ == '__main__':
    unittest.main()
