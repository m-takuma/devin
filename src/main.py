import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from google.adk.agents import LlmAgent
import os

# Define the root orchestrator agent
root_agent = LlmAgent(
    name="root_orchestrator_agent",
    model="gemini-2.0-flash", # As per the ADK LlmAgent example
    description="The main orchestrator agent responsible for understanding user goals and delegating tasks to appropriate sub-agents.",
    instruction="""You are the root orchestrator agent.
Your primary role is to understand the user's overall goal and delegate tasks to specialized sub-agents.
When you receive a request, analyze it and determine which sub-agent is best suited to handle it or if the task can be handled directly.
You will be provided with a list of available sub-agents and their capabilities.
Your goal is to coordinate these agents to fulfill the user's request efficiently.
If the request is simple and doesn't require a sub-agent, you can attempt to answer it directly.
""",
    tools=[] # Sub-agents (as AgentTool instances) will be added here later
)

APP_NAME = "devin_orchestrator_app"
USER_ID = "test_user_001"
SESSION_ID = "test_session_001"

async def main():
    print("Initializing agent runner...")

    session_service = InMemorySessionService()
    # Create a session for the interaction
    session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)

    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service
    )

    user_query = "Hello, what is your primary role?"
    print(f"\n>>> Sending to agent '{root_agent.name}': '{user_query}'")

    user_content = types.Content(role='user', parts=[types.Part(text=user_query)])

    final_response_text = "Agent interaction failed." # Default error message

    try:
        # Run the agent and process events
        async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=user_content):
            # print(f"Event: {event.type}, Author: {event.author}") # Uncomment for detailed event logging
            if event.is_final_response() and event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
                break # Stop after the first final response for this simple interaction
        if final_response_text == "Agent interaction failed.": # If loop finished without a final response
             final_response_text = "No final response received from agent."
    except Exception as e:
        print(f"An error occurred during agent interaction: {e}")
        final_response_text = "Sorry, I encountered an error while processing your request. Please try again later."

    print(f"\n<<< Agent '{root_agent.name}' Response: {final_response_text}")

    # You can inspect the session state if needed
    # current_session = session_service.get_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
    # print(f"\nSession state after interaction: {current_session.state}")

if __name__ == "__main__":
    asyncio.run(main())
