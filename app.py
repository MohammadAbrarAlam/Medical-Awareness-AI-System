# ==========================================
# Medical Awareness App Entry Point (Flask)
# ==========================================

from flask import Flask, request, render_template
import os
import time
from crews import medical_awareness_crew

app = Flask(__name__)


# ==========================================
# Core Function
# ==========================================
def run_medical_awareness(topic):
    if not topic:
        return "Topic is required"

    retries = 4

    for attempt in range(retries):
        try:
            result = medical_awareness_crew.kickoff(
                inputs={"topic": topic}
            )
            return str(result)

        except Exception as e:
            error_message = str(e)
            print(f"Attempt {attempt + 1} failed: {error_message}")

            # Handle Gemini quota exceeded (429)
            if "429" in error_message or "quota" in error_message.lower():
                if attempt < retries - 1:
                    print("Quota exceeded. Waiting 35 seconds before retry...")
                    time.sleep(35)
                    continue

            # Handle Gemini high demand (503)
            elif "503" in error_message or "high demand" in error_message.lower():
                if attempt < retries - 1:
                    print("Model busy. Waiting 10 seconds before retry...")
                    time.sleep(10)
                    continue

            return f"Error: {error_message}"

    return "Gemini API is temporarily busy or quota exceeded. Please try again after 1 minute."


# ==========================================
# Routes
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

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