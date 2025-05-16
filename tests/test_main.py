import unittest
import io
from contextlib import redirect_stdout

# src.main をインポートするために、プロジェクトのルートがPYTHONPATHに含まれているか、
# テストランナーが適切に解釈してくれることを期待します。
from src.main import main as main_program

class TestMain(unittest.TestCase):

    def test_main_prints_helloworld(self):
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            main_program()
        self.assertEqual(captured_output.getvalue().strip(), "HelloWorld")

if __name__ == '__main__':
    unittest.main()