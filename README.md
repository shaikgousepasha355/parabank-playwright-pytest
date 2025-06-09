# ParaBank Playwright Pytest Automation

## Overview
End-to-end UI and API automation for [ParaBank] using Playwright (Python) and Pytest.

## Project Structure
- `pages/`: Page Object Model classes for UI
- `tests/`: UI test cases
- `tests/`: API test cases
- `utils/`: Helpers for data and API
- `conftest.py`: Pytest fixtures
- `config/`: YAML config files

## Setup
1. Install dependencies:
    ```
    pip install -r requirements.txt
    playwright install
    ```
2. Configure URLs:
    ```
    Edit config/config.yaml with your base URLs if necessary.
    ```
3. Run all tests:
    ```
    pytest --html=reports/report.html
    ```

## Notes
- The framework generates a unique user for each run.
- UI test saves session/cookies for API test to reuse.
- Adjust selectors if ParaBank UI changes.
- Python 3.10 version or higher should be available.