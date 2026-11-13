import unittest

import GhostTR

SITE = {"name": "Example", "uri_check": "https://example.com/{account}", "e_code": 200, "e_string": "profile"}


class SiteHasAccountTest(unittest.TestCase):
    def test_matching_code_and_string_is_found(self):
        self.assertTrue(GhostTR.site_has_account(SITE, 200, "<h1>profile</h1>"))

    def test_wrong_status_code_is_not_found(self):
        self.assertFalse(GhostTR.site_has_account(SITE, 404, "<h1>profile</h1>"))

    def test_missing_e_string_is_not_found(self):
        self.assertFalse(GhostTR.site_has_account(SITE, 200, "<h1>nothing here</h1>"))


if __name__ == "__main__":
    unittest.main()
