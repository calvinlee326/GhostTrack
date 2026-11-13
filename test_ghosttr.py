import contextlib
import io
import unittest
from unittest import mock

import GhostTR

SITE = {"name": "Example", "uri_check": "https://example.com/{account}", "e_code": 200, "e_string": "profile"}


class SiteHasAccountTest(unittest.TestCase):
    def test_matching_code_and_string_is_found(self):
        self.assertTrue(GhostTR.site_has_account(SITE, 200, "<h1>profile</h1>"))

    def test_wrong_status_code_is_not_found(self):
        self.assertFalse(GhostTR.site_has_account(SITE, 404, "<h1>profile</h1>"))

    def test_missing_e_string_is_not_found(self):
        self.assertFalse(GhostTR.site_has_account(SITE, 200, "<h1>nothing here</h1>"))


class UsernameInputTest(unittest.TestCase):
    def test_url_breaking_username_makes_no_request(self):
        for username in ["evil.com/#", "evil.com\\", "a?b", "a#b", "a@b", "a:b", "a b", "a%2fb", "a[b]"]:
            with self.subTest(username=username):
                with mock.patch.object(GhostTR.requests, "get") as get, contextlib.redirect_stdout(io.StringIO()):
                    GhostTR.TrackLu.__wrapped__(username)
                get.assert_not_called()

    def test_normal_username_is_searched(self):
        with mock.patch.object(GhostTR.requests, "get") as get, contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(io.StringIO()):
            GhostTR.TrackLu.__wrapped__("john.doe_1-x")
        get.assert_called()


class PrintableTest(unittest.TestCase):
    def test_terminal_escape_sequences_are_stripped(self):
        self.assertEqual(GhostTR.printable("https://x.io/\x1b[2Jbob"), "https://x.io/[2Jbob")


if __name__ == "__main__":
    unittest.main()
