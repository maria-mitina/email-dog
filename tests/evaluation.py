import unittest
from main import EmailDog
from services.session import SessionService

class TestEmailDogEvaluation(unittest.TestCase):
    def test_end_to_end_flow(self):
        """
        Tests the end-to-end flow of the E-Mail Dog application.
        """
        email_dog = EmailDog()
        email_dog.run()
        
        # You can add more detailed assertions here based on the expected final state
        # For now, we'll just check that the application runs without errors.
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
