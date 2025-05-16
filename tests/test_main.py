import unittest
import io
from contextlib import redirect_stdout
import asyncio

# src.main をインポートするために、プロジェクトのルートがPYTHONPATHに含まれているか、
# テストランナーが適切に解釈してくれることを期待します。
from src.main import main as main_program, root_agent
from google.adk.agents import LlmAgent

class TestMain(unittest.IsolatedAsyncioTestCase):
    async def test_main_runs_agent_and_gets_response(self):
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            await main_program() # main_program is now async
        output = captured_output.getvalue().strip()

        self.assertIn("Initializing agent runner...", output)
        self.assertIn(f">>> Sending to agent '{root_agent.name}':", output)
        self.assertIn(f"<<< Agent '{root_agent.name}' Response:", output)

        # Check that there is some response text after "Agent ... Response:"
        # The actual content of the response will depend on the LLM and the agent's instruction
        response_marker = f"<<< Agent '{root_agent.name}' Response:"
        self.assertTrue(len(output.split(response_marker)[1].strip()) > 0, "Agent did not provide a response.")


    def test_root_agent_definition(self):
        self.assertIsInstance(root_agent, LlmAgent)
        self.assertEqual(root_agent.name, "root_orchestrator_agent")
        self.assertEqual(root_agent.description, "The main orchestrator agent responsible for understanding user goals and delegating tasks to appropriate sub-agents.")
        self.assertIn("Your primary role is to understand the user's overall goal", root_agent.instruction)
        self.assertEqual(root_agent.tools, [])



if __name__ == '__main__':
    unittest.main()