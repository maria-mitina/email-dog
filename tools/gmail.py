class GmailTool:
    def __init__(self):
        # In a real application, this would be initialized with credentials
        pass

    def get_labeled_threads(self, label):
        print(f"Getting threads with label: {label}")
        # Mock response
        return [
            {"id": "thread1", "snippet": "Hello, let's discuss the project."},
            {"id": "thread2", "snippet": "Following up on our conversation."}
        ]

    def create_draft(self, thread_id, body):
        print(f"Creating draft for thread {thread_id} with body: {body}")
        # Mock response
        return {"id": "draft1", "message": {"threadId": thread_id}}
