# Devin - AI Software Developer Agent Project
# Devin - AIソフトウェア開発エージェントプロジェクト

This project aims to build a self-improving AI software developer agent.
このプロジェクトは、自己改善型のAIソフトウェア開発エージェントを構築することを目的としています。

## Prerequisites
## 前提条件

Before you begin, ensure you have the following installed:
作業を始める前に、以下のものがインストールされていることを確認してください：

*   **Python**: バージョン3.10以上を推奨します。
*   **uv**: 高速なPythonパッケージインストーラー兼リゾルバーです。まだインストールしていない場合は、pipでインストールできます：
    ```bash
    pip install uv
    ```
*   **Git**: For version control and managing submodules.
*   **Visual Studio Code (Recommended IDE)**:
    *   [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for VSCode.
*   **Git**: バージョン管理とサブモジュールの管理に使用します。
*   **Visual Studio Code (推奨IDE)**:
    *   VSCode用の[Python拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python)。

## Development Setup
## 開発環境のセットアップ

Follow these steps to set up your development environment:
以下の手順で開発環境をセットアップしてください：

1.  **Clone the Repository**:
    If you haven't already, clone the project repository:
1.  **リポジトリのクローン**:
    まだクローンしていない場合は、プロジェクトリポジトリをクローンします：
    ```bash
    git clone <repository-url> # Replace <repository-url> with the actual URL
    cd devin # Or your project's root directory name
    git clone <リポジトリURL> # <リポジトリURL> を実際のURLに置き換えてください
    cd devin # またはプロジェクトのルートディレクトリ名
    ```

2.  **Initialize Git Submodules**:
    This project uses Git submodules to include external documentation (e.g., `google-adk-docs`). After cloning, initialize and update the submodules:
2.  **Gitサブモジュールの初期化**:
    このプロジェクトでは、外部ドキュメント（例：`google-adk-docs`）を含めるためにGitサブモジュールを使用しています。クローン後、サブモジュールを初期化して更新します：
    ```bash
    git submodule update --init --recursive
    ```
    The `google-adk` documentation will be available in the `docs/` directory.
    `google-adk` のドキュメントは `docs/google-adk/` ディレクトリで利用可能になります。

3.  **Create and Activate Virtual Environment (using `uv`)**:
    It's highly recommended to use a virtual environment to manage project dependencies.
3.  **仮想環境の作成と有効化 (`uv` を使用)**:
    プロジェクトの依存関係を管理するために、仮想環境を使用することを強く推奨します。
    ```bash
    # Create the virtual environment (usually creates a .venv folder)
    # 仮想環境を作成します (通常 .venv フォルダが作成されます)
    uv venv

    # Activate the virtual environment
    # On macOS/Linux (bash/zsh):
    # 仮想環境を有効化します
    # macOS/Linux (bash/zsh) の場合:
    source .venv/bin/activate
    # On Windows (PowerShell):
    # Windows (PowerShell) の場合:
    # .\.venv\Scripts\Activate.ps1
    # On Windows (cmd.exe):
    # Windows (cmd.exe) の場合:
    # .\.venv\Scripts\activate.bat
    ```
    You should see `(.venv)` at the beginning of your terminal prompt.
    ターミナルのプロンプトの先頭に `(.venv)` と表示されるはずです。

4.  **Install Dependencies (using `uv`)**:
    With the virtual environment activated, install the required Python packages:
4.  **依存関係のインストール (`uv` を使用)**:
    仮想環境を有効化した状態で、必要なPythonパッケージをインストールします：
    ```bash
    uv pip install -r requirements.txt
    ```

## VSCode Configuration
## VSCodeの設定

*   **Python Interpreter**: VSCode should automatically detect and use the Python interpreter from your `.venv` virtual environment. If not, you can manually select it:
    1.  Open the Command Palette (Cmd+Shift+P or Ctrl+Shift+P).
    2.  Type "Python: Select Interpreter".
    3.  Choose the interpreter located at `.venv/bin/python` within your project directory.
*   **Debugging and Testing**: The project includes a `.vscode/launch.json` file with pre-configured settings for:
    *   Debugging the current Python file ("Python: Current File").
    *   Running unit tests ("Python: Run Unittests").
    You can access these from the "Run and Debug" view in VSCode.
*   **Pythonインタプリタ**: VSCodeは、`.venv` 仮想環境からPythonインタプリタを自動的に検出して使用するはずです。そうでない場合は、手動で選択できます：
    1.  コマンドパレットを開きます (Cmd+Shift+P または Ctrl+Shift+P)。
    2.  "Python: Select Interpreter" と入力します。
    3.  プロジェクトディレクトリ内の `.venv/bin/python` にあるインタプリタを選択します。
*   **デバッグとテスト**: プロジェクトには、以下のための事前設定が含まれた `.vscode/launch.json` ファイルがあります：
    *   現在のPythonファイルのデバッグ ("Python: Current File")。
    *   ユニットテストの実行 ("Python: Run Unittests")。
    これらはVSCodeの「実行とデバッグ」ビューからアクセスできます。

## Running Unit Tests
## ユニットテストの実行

To ensure the application is working correctly, run the unit tests:
アプリケーションが正しく動作することを確認するために、ユニットテストを実行します：

*   **Via Command Line (with `uv`)**:
*   **コマンドライン経由 (`uv` を使用)**:
    ```bash
    uv run python -m unittest discover tests
    ```
*   **Via VSCode**:
    Use the "Python: Run Unittests" launch configuration from the "Run and Debug" panel.
*   **VSCode経由**:
    「実行とデバッグ」パネルから "Python: Run Unittests" 起動設定を使用します。

## Running the Application
## アプリケーションの実行

To run the main application (currently, it initializes the root agent and prints its details):
メインアプリケーションを実行するには（現在はルートエージェントを初期化し、その詳細を表示します）：
```bash
# Ensure your virtual environment is activated
# 仮想環境が有効化されていることを確認してください
python src/main.py
# Or using uv:
# または uv を使用する場合:
uv run python src/main.py
```