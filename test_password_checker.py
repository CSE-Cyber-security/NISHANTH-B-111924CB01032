import unittest

from password_checker import check_password


class PasswordCheckerTests(unittest.TestCase):
    def test_returns_expected_fields(self):
        result = check_password("Example!Passphrase2026")
        self.assertEqual(set(result), {"score", "strength", "feedback"})

    def test_score_is_within_range(self):
        result = check_password("A!b2")
        self.assertGreaterEqual(result["score"], 0)
        self.assertLessEqual(result["score"], 100)

    def test_common_password_is_penalized(self):
        result = check_password("password")
        self.assertLessEqual(result["score"], 10)
        self.assertIn("Very Weak", result["strength"])

    def test_non_string_input_raises_error(self):
        with self.assertRaises(TypeError):
            check_password(None)


if __name__ == "__main__":
    unittest.main()
