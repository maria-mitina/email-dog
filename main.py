
class EmailDog:
    def __init__(self):
        self.intake_agent = IntakeAgent()
        self.planner_agent = PlannerAgent()
        self.email_writer_agent = EmailWriterAgent()

    def run(self):
        # Run the agents in a sequence
        self.intake_agent.run()
        self.planner_agent.run()
        self.email_writer_agent.run()

from agents.intake import IntakeAgent
from agents.planner import PlannerAgent
from agents.writer import EmailWriterAgent


if __name__ == "__main__":
    email_dog = EmailDog()
    email_dog.run()
