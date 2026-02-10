# Basic Calculator (Flask + Playwright tests)

This project is a minimal calculator web app built with Flask (Python). It contains:

- A backend module that performs arithmetic operations.
- A simple HTML UI served by Flask.
- Playwright JS test cases (in the `tests/playwright-js` folder) which exercise the UI.

Quick start
1. Create and activate a virtualenv (recommended):

   python3 -m venv .venv
   source .venv/bin/activate

2. Install Python dependencies (only Flask is required):

   pip install -r requirements.txt

3. Start the Flask app (keep it running while you run tests):

   python app.py

   Then open http://127.0.0.1:5000 in your browser.

4. Run Playwright JS tests (in a separate terminal):

   cd tests/playwright-js
   npm install
   npx playwright install
   npx playwright test

Coverage
--------
To collect coverage of the Python server while Playwright exercises the UI, start the Flask app with the environment variable `COVERAGE=1`. This will cause the server to collect coverage and emit a detailed JSON report when the process exits.

Example (macOS/zsh):

```bash
# from project root
source .venv/bin/activate
COVERAGE=1 python app.py

# in another terminal run Playwright tests
cd tests/playwright-js
npx playwright test

# after the server process exits, coverage-playwright.json will be created in the project root
```

Convenience helper
-------------------
If you want Playwright to start the server with coverage for you, use the helper `tests/playwright-js/start_server_coverage.js` from your Playwright tests to spawn the server with coverage enabled.

Project layout
- `app.py` — Flask application entrypoint and wiring
- `calculator/backend.py` — arithmetic logic
- `calculator/advanced.py` — additional operations (power/mod/sqrt/etc.)
- `templates/index.html` — simple UI
- `static/style.css` — small stylesheet
- `tests/playwright-js/` — Playwright JS tests and config

Notes
- Tests run against a running Flask server (configured at http://127.0.0.1:5000 by `tests/playwright-js/playwright.config.js`).
- `tests/playwright-js` contains `package.json` and `playwright.config.js`. Use those to install Playwright and run tests.
- I removed Python pytest-related files/dependencies to keep the repo focused on the Flask app + Playwright JS tests.

