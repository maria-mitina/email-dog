# E-Mail Dog: Requirements

This document outlines the functional, non-functional, and course-specific requirements for the E-Mail Dog project, derived from `history.txt`.

## 1. Core Product Goal

To create a goal-oriented agent system that automates email conversations to achieve user-defined objectives, turning a user's inbox from a task list into a set of managed outcomes.

## 2. Functional Requirements

### FR1: Objective-Driven Automation
- Users must be able to define a clear, natural language objective for a given email thread (e.g., "Book annual car service for 20/11/25 or 24/11/25").
- The system must use this objective as the primary driver for all its actions.

### FR2: Gmail Integration
- The system must securely connect to a user's Gmail account via OAuth.
- It must identify email threads designated for automation using a specific Gmail label (`Autopilot InProgress`).
- It must be able to read labeled threads, create drafts, and send emails on the user's behalf.

### FR3: Multi-Agent Workflow
The system will be composed of at least three distinct agents:
- **Intake Agent**: Analyzes new threads and user objectives, summarizes the context, and extracts key constraints (dates, topics, etc.).
- **Planner Agent**: Decides the next best action to move the objective forward (e.g., send initial outreach, send follow-up, wait, clarify). This agent must operate in a loop until the objective is complete.
- **Email Writer Agent**: Drafts the email content based on the Planner's decision, matching the tone and style of the conversation.

### FR4: Long-Running Operations & State Management
- The system must manage objectives that unfold over days or weeks.
- It must maintain the state of each objective (e.g., `WAITING_FOR_REPLY`, `DRAFTING`, `DONE`).
- It must support pausing and resuming automation on a per-objective basis.
- It must be able to schedule and trigger follow-up actions after a period of inactivity.

### FR5: User Control & Transparency
- All agent-driven actions should be reviewable by the user (e.g., via drafts in Gmail).
- A simple web interface is required to view all objectives, their current status, and the threads they are linked to.
- Users must be able to stop the automation at any time (e.g., by removing the Gmail label).

## 3. Kaggle Course Requirements Checklist

The final implementation must demonstrate at least **three (3)** of the following concepts:

- [ ] **Multi-agent system**: Satisfied by the Intake, Planner, and Email Writer agent design.
    - [ ] Agent powered by an LLM
    - [ ] Sequential agents
    - [ ] Loop agents
- [ ] **Tools**:
    - [ ] Custom tools (e.g., `get_thread_summary`, `schedule_followup`)
    - [ ] OpenAPI / built-in tools (e.g., `gmail.sendEmail`, `clock.now`)
- [ ] **Long-running operations**: Satisfied by the core design of managing objectives over time, including scheduled follow-ups.
- [ ] **Sessions & Memory**:
    - [ ] Sessions & state management (tracking the status of each objective).
    - [ ] Long term memory (optional, for remembering user preferences or past providers).
- [ ] **Context engineering**:
    - [ ] Context compaction (summarizing long email threads to fit context windows).
- [ ] **Observability**:
    - [ ] Logging, Tracing, Metrics for monitoring agent behavior and performance.
- [ ] **Agent evaluation**: A simple framework to test agent responses against predefined scenarios.
