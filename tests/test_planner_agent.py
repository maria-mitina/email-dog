import unittest
from agents.planner import PlannerAgent
from services.session import SessionService

class TestPlannerAgent(unittest.TestCase):
    def test_planner_agent_run(self):
        """
        Tests the run method of the PlannerAgent with mocked data.
        """
        session_service = SessionService()
        session_service.update_objective({"id": "objective1", "thread_id": "thread1", "status": "processed", "summary": "Summary of thread1", "constraints": {"topic": "project discussion"}})
        
        planner_agent = PlannerAgent(session_service)
        planner_agent.run()
        
        # Assert that the objective has been updated
        updated_objective = session_service.get_objective("objective1")
        self.assertEqual(updated_objective['status'], 'planned')
        self.assertEqual(updated_objective['next_step'], 'draft_email')

if __name__ == "__main__":
    unittest.main()
