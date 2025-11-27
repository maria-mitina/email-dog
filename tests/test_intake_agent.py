import unittest
from unittest.mock import patch
from agents.intake import IntakeAgent

class TestIntakeAgent(unittest.TestCase):
    @patch('agents.intake.IntakeAgent._fetch_labeled_threads')
    def test_intake_agent_run(self, mock_fetch_threads):
        """
        Tests the run method of the IntakeAgent with mocked data.
        """
        mock_fetch_threads.return_value = [
            {"id": "thread1", "snippet": "Hello, let's discuss the project."},
            {"id": "thread2", "snippet": "Following up on our conversation."}
        ]
        
        intake_agent = IntakeAgent()
        # This will run with the mocked _fetch_labeled_threads method
        intake_agent.run()
        
        # Here you would assert that the objectives were created correctly.
        # For now, we'll just assert that the mocked method was called.
        mock_fetch_threads.assert_called_once()

if __name__ == "__main__":
    unittest.main()
