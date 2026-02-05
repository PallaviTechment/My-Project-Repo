from flask import Flask, render_template, request, jsonify
from calculator import backend


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


if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)
