# ==========================================
# Medical Awareness App Entry Point (Flask)
# ==========================================

from flask import Flask, request, render_template
import os
from crews import medical_awareness_crew

app = Flask(__name__)


# ==========================================
# Core Function
# ==========================================
def run_medical_awareness(topic):
    if not topic:
        return "Topic is required"

    try:
        result = medical_awareness_crew.kickoff(
            inputs={"topic": topic}
        )

        return str(result)

    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {str(e)}"


# ==========================================
# Routes
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    # Get topic from HTML form
    topic = request.form.get("topic")

    if not topic:
        return render_template(
            "index.html",
            result="Topic is required"
        )

    result = run_medical_awareness(topic)

    return render_template(
        "index.html",
        result=result
    )


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