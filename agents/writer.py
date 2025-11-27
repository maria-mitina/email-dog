import logging
from agents.base import BaseAgent
from services.session import SessionService
from tools.gmail import GmailTool

logger = logging.getLogger(__name__)

class EmailWriterAgent(BaseAgent):
    def __init__(self, session_service: SessionService):
        self.session_service = session_service
        self.gmail_tool = GmailTool()

    def run(self):
        logger.info("Running Email Writer Agent")
        # 1. Get objectives from the session service
        objectives = self._get_objectives()
        for objective in objectives:
            if objective.get('next_step') == 'draft_email':
                logger.info(f"Writing email for objective {objective['id']}")
                # 2. Generate the email draft
                draft = self._generate_draft(objective)
                # 3. Create the draft in Gmail
                self._create_draft_in_gmail(objective, draft)
                # 4. Update the objective status
                self._update_objective_status(objective)

    def _get_objectives(self):
        logger.info("Getting objectives for email writer...")
        return self.session_service.get_all_objectives()

    def _generate_draft(self, objective):
        logger.info(f"Generating draft for objective {objective['id']}...")
        # Placeholder for generating draft - will be replaced with LLM call
        return f"This is a draft for {objective['summary']}."

    def _create_draft_in_gmail(self, objective, draft):
        logger.info(f"Creating draft in Gmail for objective {objective['id']}...")
        self.gmail_tool.create_draft(objective['thread_id'], draft)
        pass

    def _update_objective_status(self, objective):
        logger.info(f"Updating objective status for {objective['id']}...")
        objective['status'] = 'drafted'
        self.session_service.update_objective(objective)
        logger.info(f"Objective status updated: {objective}")

