import unittest

from lex.main import main


class MainTestCase(unittest.TestCase):

    def test_main(self):
        response = main()
        expected = "Lex is running"
        self.assertEqual(response, expected)
