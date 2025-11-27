import logging
from agents.base import BaseAgent
from tools.gmail import GmailTool
from services.session import SessionService

logger = logging.getLogger(__name__)

class IntakeAgent(BaseAgent):
    def __init__(self, session_service: SessionService):
        self.gmail_tool = GmailTool()
        self.session_service = session_service

    def run(self):
        logger.info("Running Intake Agent")
        # 1. Fetch labeled threads from Gmail
        threads = self._fetch_labeled_threads()
        for thread in threads:
            logger.info(f"Processing thread {thread['id']}")
            # 2. Summarize the thread
            summary = self._summarize_thread(thread)
            # 3. Extract constraints
            constraints = self._extract_constraints(thread)
            # 4. Create or update Objective session
            self._create_or_update_objective(thread, summary, constraints)

    def _fetch_labeled_threads(self):
        logger.info("Fetching labeled threads...")
        return self.gmail_tool.get_labeled_threads("Autopilot InProgress")

    def _summarize_thread(self, thread):
        logger.info(f"Summarizing thread {thread['id']}...")
        # Placeholder for summarizing thread - will be replaced with LLM call
        return f"Summary of thread: {thread['snippet']}"

    def _extract_constraints(self, thread):
        logger.info(f"Extracting constraints from thread {thread['id']}...")
        # Placeholder for extracting constraints - will be replaced with LLM call
        return {"topic": "project discussion"}

    def _create_or_update_objective(self, thread, summary, constraints):
        logger.info(f"Creating or updating objective for thread {thread['id']}...")
        objective = {
            "id": f"obj_{thread['id']}",
            "thread_id": thread['id'],
            "summary": summary,
            "constraints": constraints,
            "status": "processed"
        }
        self.session_service.update_objective(objective)
        logger.info(f"Objective created: {objective}")

