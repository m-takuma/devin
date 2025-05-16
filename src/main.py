from google.adk.agents import LlmAgent

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

def main():
    print("Root orchestrator agent defined successfully!")
    print(f"Agent Name: {root_agent.name}")
    print(f"Agent Description: {root_agent.description}")
    print(f"Agent Model: {root_agent.model}")
    # In future steps, this main function will likely be used to run the agent
    # or initiate a session with it.

if __name__ == "__main__":
    main()
