# ==========================================
# Medical Awareness App Entry Point (Flask)
# ==========================================

from flask import Flask, request, jsonify, render_template
import os
from crews import medical_awareness_crew

app = Flask(__name__)


# ==========================================
# Core Function
# ==========================================
def run_medical_awareness(topic):
    if not topic:
        return {"error": "Topic is required"}

    try:
        result = medical_awareness_crew.kickoff(
            inputs={"topic": topic}
        )

        return {
            "success": True,
            "topic": topic,
            "result": str(result)
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            "success": False,
            "error": str(e)
        }


# ==========================================
# Routes
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "error": "No JSON data received"
        }), 400

    topic = data.get("topic")

    if not topic:
        return jsonify({
            "success": False,
            "error": "Topic is required"
        }), 400

    result = run_medical_awareness(topic)

    return jsonify(result)


# ==========================================
# Run Server
# ==========================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )