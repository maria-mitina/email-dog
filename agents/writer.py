from agents.base import BaseAgent
from services.session import get_session_service
from tools.gmail import GmailTool

class EmailWriterAgent(BaseAgent):
    def __init__(self):
        self.session_service = get_session_service()
        self.gmail_tool = GmailTool()

    def run(self):
        print("Running Email Writer Agent")
        # 1. Get objectives from the session service
        objectives = self._get_objectives()
        for objective in objectives:
            if objective.get('next_step') == 'draft_email':
                # 2. Generate the email draft
                draft = self._generate_draft(objective)
                # 3. Create the draft in Gmail
                self._create_draft_in_gmail(objective, draft)

    def _get_objectives(self):
        print("Getting objectives for email writer...")
        # Placeholder for getting objectives from session service
        mock_objectives = [
            {"id": "objective1", "thread_id": "thread1", "status": "planned", "summary": "Summary of thread1", "constraints": {"topic": "project discussion"}, "next_step": "draft_email"}
        ]
        return mock_objectives

    def _generate_draft(self, objective):
        print(f"Generating draft for objective {objective['id']}...")
        # Placeholder for generating draft - will be replaced with LLM call
        return f"This is a draft for {objective['summary']}."

    def _create_draft_in_gmail(self, objective, draft):
        print(f"Creating draft in Gmail for objective {objective['id']}...")
        self.gmail_tool.create_draft(objective['thread_id'], draft)
        pass
