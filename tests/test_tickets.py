import unittest
from campusflow.tickets import calculate_priority

class TestCalculatePriority(unittest.TestCase):
    def test_high_urgency_twelve_users_is_critical(self):
        # Fill in the expected value
        self.assertEqual(calculate_priority("high", 12), "critical")
    def test_high_urgency_two_users_is_high(self):
        self.assertEqual(calculate_priority("high", 2), "high") 
    def test_low_urgency_four_users_is_medium(self):
            self.assertEqual(calculate_priority("low", 4), "medium") 
    def test_high_urgency_two_users_is_high(self):
                self.assertEqual(calculate_priority("low", 1), "low")
    def test_high_urgency_ten_users_is_critical(self):
            # Fill in the expected value
            self.assertEqual(calculate_priority("high", 10), "critical")
    def test_medium_urgency_one_user_is_medium(self):
            self.assertEqual(calculate_priority("medium", 1), "medium") 
    def test_low_urgency_three_users_is_medium(self):
                self.assertEqual(calculate_priority("low", 3), "medium") 
    def test_low_urgency_two_users_is_low(self):
                    self.assertEqual(calculate_priority("low", 2), "low")
    def test_low_urgency_one_user_is_low(self):
       self.assertEqual(calculate_priority("low", 1), "low")                            
        


if __name__ == "__main__":
    unittest.main()