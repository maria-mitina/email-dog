# test_email_dog.py
import unittest
from main import EmailDog

class TestEmailDog(unittest.TestCase):
    def test_email_dog_initialization(self):
        """
        Tests that the EmailDog class initializes correctly.
        """
        email_dog = EmailDog()
        self.assertIsNotNone(email_dog.intake_agent)
        self.assertIsNotNone(email_dog.planner_agent)
        self.assertIsNotNone(email_dog.email_writer_agent)

if __name__ == "__main__":
    unittest.main()
