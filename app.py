# ==========================================
# Medical Awareness App Entry Point (Flask)
# ==========================================

from flask import Flask, request, jsonify
from crews import medical_awareness_crew

app = Flask(__name__)


# ==========================================
# Core Function (Crew Runner)
# ==========================================
def run_medical_awareness(topic: str):
    """
    Run the Medical Awareness Crew for a given topic.
    """

    if not topic:
        return {"error": "Topic is required"}

    print("\n====================================")
    print(f"Starting Medical Analysis for: {topic}")
    print("====================================\n")

    try:
        # Run CrewAI workflow
        result = medical_awareness_crew.kickoff(
            inputs={"topic": topic}
        )

        print("\n====================================")
        print("FINAL MEDICAL REPORT GENERATED")
        print("====================================\n")

        return {"success": True, "topic": topic, "result": str(result)}

    except Exception as e:
        print("Error occurred:", str(e))
        return {"success": False, "error": str(e)}


# ==========================================
# Flask Routes
# ==========================================

@app.route("/")
def home():
    return jsonify({
        "message": "🩺 Medical Awareness AI System Running",
        "status": "active"
    })


@app.route("/analyze", methods=["POST"])
def analyze():
    """
    API endpoint to analyze medical topic
    Expected JSON:
    {
        "topic": "diabetes"
    }
    """

    data = request.get_json()

    if not data or "topic" not in data:
        return jsonify({"error": "Topic is required"}), 400

    topic = data["topic"]

    result = run_medical_awareness(topic)

    return jsonify(result)


# ==========================================
# Run Server
# ==========================================
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)