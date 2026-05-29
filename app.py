# ==========================================
# Medical Awareness App Entry Point (Flask)
# ==========================================

from flask import Flask, request, render_template
import os
from crews import medical_awareness_crew
import time

app = Flask(__name__)


# ==========================================
# Core Function
# ==========================================
def run_medical_awareness(topic):
    if not topic:
        return "Topic is required"

    retries = 3

    for attempt in range(retries):
        try:
            result = medical_awareness_crew.kickoff(
                inputs={"topic": topic}
            )

            return str(result)

        except Exception as e:
            error_message = str(e)
            print(f"Attempt {attempt + 1} failed: {error_message}")

            # Retry if Gemini overloaded
            if "503" in error_message or "high demand" in error_message.lower():
                if attempt < retries - 1:
                    time.sleep(8)
                    continue

            return f"Error: {error_message}"

    return "Service temporarily unavailable. Please try again in a few minutes."
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