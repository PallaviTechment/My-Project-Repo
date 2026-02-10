from flask import Flask, render_template, request, jsonify
from calculator import backend
import os

# Optional runtime coverage: when COVERAGE=1 is set in the environment,
# we start coverage collection for the Flask process and emit a JSON report
# at shutdown (coverage-playwright.json).
_cov = None
if os.getenv("COVERAGE") == "1":
    try:
        import coverage
        _cov = coverage.Coverage(data_file=".coverage_playwright", source=["calculator", "app.py"])
        _cov.start()
    except Exception:
        _cov = None


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/calculate", methods=["POST"])
    def calculate():
        data = request.get_json() or {}
        try:
            a = float(data.get("a", 0))
            b = float(data.get("b", 0))
            op = data.get("op", "+")
            result = backend.calculate(op, a, b)
            # If result is an integer value, return as int for nicer display
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            return jsonify({"ok": True, "result": result})
        except ZeroDivisionError:
            return jsonify({"ok": False, "error": "division by zero"}), 400
        except Exception as exc:
            return jsonify({"ok": False, "error": str(exc)}), 400

    return app


def _shutdown_coverage():
    """Stop coverage and generate a JSON report with extra metadata.

    The report will be written to `coverage-playwright.json` in the project root.
    """
    try:
        if _cov is None:
            return
        _cov.stop()
        _cov.save()
        # Try to produce a raw coverage JSON first
        try:
            _cov.json_report(outfile="coverage-raw.json")
        except Exception:
            pass
        # Generate an enhanced JSON with source and function info using the helper
        try:
            from tools.coverage_json import generate_detailed_json

            generate_detailed_json(data_file=".coverage_playwright", out_file="coverage-playwright.json")
        except Exception:
            # Fallback: copy raw report if available
            try:
                import shutil

                shutil.copyfile("coverage-raw.json", "coverage-playwright.json")
            except Exception:
                pass
    except Exception:
        pass


if __name__ == "__main__":
    app = create_app()
    try:
        app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)
    finally:
        _shutdown_coverage()

