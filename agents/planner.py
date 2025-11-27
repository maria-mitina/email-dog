from agents.base import BaseAgent
from services.session import get_session_service

class PlannerAgent(BaseAgent):
    def __init__(self):
        self.session_service = get_session_service()

    def run(self):
        print("Running Planner Agent")
        # 1. Get objectives from the session service
        objectives = self._get_objectives()
        for objective in objectives:
            # 2. Decide the next step
            next_step = self._decide_next_step(objective)
            # 3. Update the objective with the next step
            self._update_objective(objective, next_step)

    def _get_objectives(self):
        print("Getting objectives...")
        # Placeholder for getting objectives from session service
        mock_objectives = [
            {"id": "objective1", "thread_id": "thread1", "status": "processed", "summary": "Summary of thread1", "constraints": {"topic": "project discussion"}},
            {"id": "objective2", "thread_id": "thread2", "status": "processed", "summary": "Summary of thread2", "constraints": {"topic": "follow up"}}
        ]
        return mock_objectives

    def _decide_next_step(self, objective):
        print(f"Deciding next step for objective {objective['id']}...")
        # Placeholder for deciding next step - will be replaced with LLM call
        if objective['status'] == 'processed':
            return "draft_email"
        else:
            return "no_action"

    def _update_objective(self, objective, next_step):
        print(f"Updating objective {objective['id']} with next step {next_step}...")
        # Placeholder for updating objective in session service
        objective['next_step'] = next_step
        objective['status'] = 'planned'
        print(f"Objective updated: {objective}")
        pass
