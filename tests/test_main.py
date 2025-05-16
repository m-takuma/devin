import unittest
import io
from contextlib import redirect_stdout

# src.main をインポートするために、プロジェクトのルートがPYTHONPATHに含まれているか、
# テストランナーが適切に解釈してくれることを期待します。
from src.main import main as main_program, root_agent
from google.adk.agents import LlmAgent

class TestMain(unittest.TestCase):

    def test_main_prints_agent_info(self):
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            main_program()
        output = captured_output.getvalue().strip().split('\n')
        self.assertIn("Root orchestrator agent defined successfully!", output[0])
        self.assertIn(f"Agent Name: {root_agent.name}", output[1])
        self.assertIn(f"Agent Description: {root_agent.description}", output[2])
        self.assertIn(f"Agent Model: {root_agent.model}", output[3])

    def test_root_agent_definition(self):
        self.assertIsInstance(root_agent, LlmAgent)
        self.assertEqual(root_agent.name, "root_orchestrator_agent")
        self.assertEqual(root_agent.model, "gemini-2.0-flash")
        self.assertEqual(root_agent.description, "The main orchestrator agent responsible for understanding user goals and delegating tasks to appropriate sub-agents.")
        self.assertIn("Your primary role is to understand the user's overall goal", root_agent.instruction)
        self.assertEqual(root_agent.tools, [])



if __name__ == '__main__':
    unittest.main()