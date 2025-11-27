import logging
from agents.intake import IntakeAgent
from agents.planner import PlannerAgent
from agents.writer import EmailWriterAgent
from services.session import SessionService

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class EmailDog:
    def __init__(self):
        session_service = SessionService()
        self.intake_agent = IntakeAgent(session_service)
        self.planner_agent = PlannerAgent(session_service)
        self.email_writer_agent = EmailWriterAgent(session_service)

    def run(self):
        # Run the agents in a sequence
        logging.info("Starting E-Mail Dog...")
        self.intake_agent.run()
        self.planner_agent.run()
        self.email_writer_agent.run()
        logging.info("E-Mail Dog run complete.")

if __name__ == "__main__":
    email_dog = EmailDog()
    email_dog.run()
