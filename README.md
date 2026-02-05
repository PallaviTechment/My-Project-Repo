# Basic Calculator (Flask + Playwright tests)

This project is a minimal calculator web app built with Flask (Python). It contains:

- A backend module that performs arithmetic operations.
- A simple HTML UI served by Flask.
- Playwright test cases (in the `tests/playwright` folder) which exercise the UI.

Quick start
1. Create and activate a virtualenv (recommended):

   python3 -m venv .venv
   source .venv/bin/activate

2. Install Python dependencies:

   pip install -r requirements.txt

3. Install Playwright browsers (required once):

   python -m playwright install

4. Run the app:

   python app.py

   Then open http://127.0.0.1:5000 in your browser.

5. Run tests (ensure the app is NOT already running; tests start the app themselves):

   pytest -q

Project layout
- `app.py` — Flask application entrypoint and wiring
- `calculator/backend.py` — arithmetic logic
- `templates/index.html` — simple UI
- `static/style.css` — small stylesheet
- `tests/playwright/test_calculator.py` — Playwright tests that launch the app and test UI flows

Notes
- The Playwright tests use the `page` fixture from `pytest-playwright`. If you prefer, you can run Playwright scripts directly.
- If you can't run tests due to environment restrictions (no network or missing dependencies), you can still run `app.py` after installing dependencies locally.
