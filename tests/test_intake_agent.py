import unittest
from unittest.mock import patch, MagicMock
from agents.intake import IntakeAgent
from services.session import SessionService

class TestIntakeAgent(unittest.TestCase):
    @patch('agents.intake.GmailTool')
    def test_intake_agent_run(self, MockGmailTool):
        """
        Tests the run method of the IntakeAgent with mocked data.
        """
        mock_gmail_tool = MockGmailTool.return_value
        mock_gmail_tool.get_labeled_threads.return_value = [
            {"id": "thread1", "snippet": "Hello, let's discuss the project."},
            {"id": "thread2", "snippet": "Following up on our conversation."}
        ]
        
        session_service = SessionService()
        intake_agent = IntakeAgent(session_service)
        intake_agent.run()
        
        # Assert that the session service has been updated
        self.assertEqual(len(session_service.get_all_objectives()), 2)
        self.assertIn("obj_thread1", session_service.sessions)
