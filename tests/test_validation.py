import unittest
from campusflow.tickets import (
    validate_affected_users,
    validate_category,
    validate_urgency,
    validate_title,
)


class TestValidateAffectedUsers(unittest.TestCase):
    def test_valid_number_returns_integer(self):
        self.assertEqual(validate_affected_users("12"), 12)

    def test_zero_users_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_affected_users("0")

    def test_negative_users_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_affected_users("-3")

    def test_decimal_users_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_affected_users("2.5")

    def test_word_users_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_affected_users("many")


class TestValidateCategory(unittest.TestCase):
    def test_category_is_normalized(self):
        self.assertEqual(validate_category("  SOFTWARE "), "Software")

    def test_unknown_category_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_category("Laptop")


class TestValidateUrgency(unittest.TestCase):
    def test_urgency_is_normalized(self):
        self.assertEqual(validate_urgency(" HIGH "), "high")


class TestValidateTitle(unittest.TestCase):
    def test_blank_title_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_title("   ")

    def test_title_is_trimmed(self):
        self.assertEqual(validate_title("  Printer jammed  "), "Printer jammed")


if __name__ == "__main__":
    unittest.main()