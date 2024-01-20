import os
import unittest

from .email_validation import Email as EmailValidator


class EmailValidatorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        with open("pb.json", "w") as file:
            self.file = file

    def tearDown(self) -> None:
        os.remove("pb.json")

    def test_pass(self):
        self.assertTrue(True)

    def test_email_includes_first_and_last_names__is_valid(self):
        result = EmailValidator.validate("gandalfthegrey@milldeearth.com")

        # assert result == expected_result, "first-and-last-emails doesn't work!"
        self.assertTrue(
            result,
            msg="first-and-last-emails doesn't work!",
        )


if __name__ == "__main__":
    unittest.main()
