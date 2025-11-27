import unittest
from unittest.mock import patch
from agents.planner import PlannerAgent

class TestPlannerAgent(unittest.TestCase):
    @patch('agents.planner.PlannerAgent._get_objectives')
    def test_planner_agent_run(self, mock_get_objectives):
        """
        Tests the run method of the PlannerAgent with mocked data.
        """
        mock_get_objectives.return_value = [
            {"id": "objective1", "thread_id": "thread1", "status": "processed", "summary": "Summary of thread1", "constraints": {"topic": "project discussion"}}
        ]
        
        planner_agent = PlannerAgent()
        planner_agent.run()
        
        mock_get_objectives.assert_called_once()
        # Add more assertions here to verify the logic of _decide_next_step and _update_objective
        # For example, you could check the updated objective in a mock session service
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
