import logging
from agents.base import BaseAgent
from services.session import SessionService

logger = logging.getLogger(__name__)

class PlannerAgent(BaseAgent):
    def __init__(self, session_service: SessionService):
        self.session_service = session_service

    def run(self):
        logger.info("Running Planner Agent")
        # 1. Get objectives from the session service
        objectives = self._get_objectives()
        for objective in objectives:
            logger.info(f"Planning for objective {objective['id']}")
            # 2. Decide the next step
            next_step = self._decide_next_step(objective)
            # 3. Update the objective with the next step
            self._update_objective(objective, next_step)

    def _get_objectives(self):
        logger.info("Getting objectives...")
        return self.session_service.get_all_objectives()

    def _decide_next_step(self, objective):
        logger.info(f"Deciding next step for objective {objective['id']}...")
        # Placeholder for deciding next step - will be replaced with LLM call
        if objective['status'] == 'processed':
            return "draft_email"
        else:
            return "no_action"

    def _update_objective(self, objective, next_step):
        logger.info(f"Updating objective {objective['id']} with next step {next_step}...")
        objective['next_step'] = next_step
        objective['status'] = 'planned'
        self.session_service.update_objective(objective)
        logger.info(f"Objective updated: {objective}")

