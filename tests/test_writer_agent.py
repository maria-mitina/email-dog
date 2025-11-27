# test_writer_agent.py
import unittest
from unittest.mock import patch
from agents.writer import EmailWriterAgent

class TestEmailWriterAgent(unittest.TestCase):
    @patch('agents.writer.EmailWriterAgent._get_objectives')
    def test_email_writer_agent_run(self, mock_get_objectives):
        """
        Tests the run method of the EmailWriterAgent with mocked data.
        """
        mock_get_objectives.return_value = [
            {"id": "objective1", "thread_id": "thread1", "status": "planned", "summary": "Summary of thread1", "constraints": {"topic": "project discussion"}, "next_step": "draft_email"}
        ]
        
        writer_agent = EmailWriterAgent()
        writer_agent.run()
        
        mock_get_objectives.assert_called_once()

if __name__ == "__main__":
    unittest.main()
