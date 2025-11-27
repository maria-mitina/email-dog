class SessionService:
    def __init__(self):
        self.sessions = {}

    def get_objective(self, objective_id):
        return self.sessions.get(objective_id)

    def update_objective(self, objective):
        self.sessions[objective['id']] = objective

    def get_all_objectives(self):
        return list(self.sessions.values())

def get_session_service():
    return SessionService()
