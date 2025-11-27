# E-Mail Dog: Technical Decisions

This document outlines the chosen technology stack and key architectural decisions for the E-Mail Dog project.

## 1. Language and Core Framework

- **Language**: **Python 3.10+**
    - **Reasoning**: Python is the lingua franca of AI/ML and has the most mature ecosystem for building with LLMs. Its readability and extensive libraries for web development and API integration make it a robust choice.

- **Agent Framework**: **LangChain**
    - **Reasoning**: LangChain provides a comprehensive and flexible framework for developing agent-based applications. It offers pre-built components for multi-agent systems, tool usage, memory, and chains, which directly map to the project's requirements. This accelerates development and ensures we can easily implement concepts from the Kaggle course. An alternative could be the OpenAI Assistants API, but LangChain offers more vendor-neutrality and control.

## 2. Gmail Integration

- **API**: **Google Cloud SDK (google-api-python-client)**
    - **Reasoning**: This is the official and most stable library for interacting with Google APIs, including Gmail. It handles authentication (OAuth 2.0) and provides the necessary methods to read threads, manage labels, and send emails.

- **Authentication**: **OAuth 2.0 (User Consent Flow)**
    - **Reasoning**: This is the standard, secure way to gain delegated access to a user's Gmail account without handling their credentials directly. We will request the minimal necessary scopes (`gmail.modify`).

## 3. State and Session Management

- **Session Store**: **In-Memory Dictionary (for initial development)**
    - **Reasoning**: For the prototype and to satisfy the course requirements, a simple in-memory Python dictionary mapping `objective_id` to a state object is sufficient. It's fast, easy to implement, and avoids external dependencies.

- **Persistence (Production Consideration)**: **PostgreSQL or a NoSQL database (e.g., MongoDB)**
    - **Reasoning**: For a real-world application, state must be persisted. A relational database like PostgreSQL is a solid choice for structured data like objectives and states. A NoSQL database could also work well if the state objects are complex and evolve frequently. This will not be implemented for the initial course submission.

## 4. Agent and LLM Configuration

- **LLM Provider**: **OpenAI (GPT-4 or later)**
    - **Reasoning**: GPT-4 provides state-of-the-art reasoning and language generation capabilities, which are critical for the Planner and Email Writer agents to function effectively. The API is reliable and well-documented.

- **Tool Definition**: **LangChain Custom Tools & Pydantic**
    - **Reasoning**: We will define custom tools (e.g., `GmailTool`, `SchedulerTool`) as Python functions and use Pydantic to define their input schemas. LangChain's agent executors can natively handle these structured tools.

## 5. Testing and Evaluation

- **Testing Framework**: **pytest**
    - **Reasoning**: `pytest` is the standard for testing in the Python ecosystem. Its fixture model is excellent for managing dependencies like mocked API clients and setting up agent states for tests.

- **Evaluation Strategy**: **Scripted Scenarios**
    - **Reasoning**: We will create a set of synthetic email threads and objectives as test cases. An evaluation script will run the agent system against these scenarios and assert that the generated responses or state changes meet expectations. This provides a repeatable way to measure agent performance and satisfy the "Agent evaluation" course requirement.

## 6. Project Structure

The project will follow a standard Python application layout:

```
/email-dog
|-- main.py             # Main application entry point
|-- agents/             # Agent definitions (Intake, Planner, etc.)
|-- tools/              # Custom tool implementations (Gmail, etc.)
|-- services/           # State management and scheduling services
|-- tests/              # Pytest tests
|-- docs/               # Markdown documentation
|-- requirements.txt    # Python dependencies
|-- README.md
```
