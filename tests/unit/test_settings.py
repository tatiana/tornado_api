import unittest

from lex import settings


class SettingsTestCase(unittest.TestCase):

    def test_local_values(self):
        self.assertEqual(settings.DEBUG, True)
        self.assertEqual(settings.PORT, 8888)
        self.assertEqual(settings.HTML_PATH, 'docs/build/html')
        self.assertEqual(settings.STATIC_PATH, "docs/build/html/_static")
