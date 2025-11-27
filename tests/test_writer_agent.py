# test_writer_agent.py
import unittest
from unittest.mock import patch
from agents.writer import EmailWriterAgent
from services.session import SessionService

class TestEmailWriterAgent(unittest.TestCase):
    @patch('agents.writer.GmailTool')
    def test_email_writer_agent_run(self, MockGmailTool):
        """
        Tests the run method of the EmailWriterAgent with mocked data.
        """
        mock_gmail_tool = MockGmailTool.return_value
        
        session_service = SessionService()
        session_service.update_objective({"id": "objective1", "thread_id": "thread1", "status": "planned", "summary": "Summary of thread1", "constraints": {"topic": "project discussion"}, "next_step": "draft_email"})
        
        writer_agent = EmailWriterAgent(session_service)
        writer_agent.run()
        
        # Assert that the draft was created and the objective updated
        mock_gmail_tool.create_draft.assert_called_once_with("thread1", "This is a draft for Summary of thread1.")
        updated_objective = session_service.get_objective("objective1")
        self.assertEqual(updated_objective['status'], 'drafted')
