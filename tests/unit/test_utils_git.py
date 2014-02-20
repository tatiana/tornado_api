import unittest

from mock import patch

from lex.utils import git


class GitTestCase(unittest.TestCase):

    @patch("lex.utils.git.run", return_value="HEAD")
    def test_get_version_label_head(self, patch_run):
        response = git.get_version_label()
        self.assertEqual(response, "unstaged")
