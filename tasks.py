from crewai import Task
from agents import (
    research_agent,
    simplifier_agent,
    prevention_agent,
    fact_checker_agent,
    response_agent
)

# ==============================
# 1. Research Task
# ==============================
research_task = Task(
    description="""
    Research detailed and accurate medical information about {topic}.

    Include:
    - Causes
    - Symptoms
    - Risk factors
    - Complications
    - General awareness information

    Use only reliable and verified medical sources.
    """,
    expected_output="""
    A structured and detailed medical research report about {topic}.
    """,
    agent=research_agent
)

# ==============================
# 2. Simplification Task
# ==============================
simplify_task = Task(
    description="""
    Convert the researched medical information about {topic}
    into simple, easy-to-understand language.

    Focus on:
    - Key points only
    - Simple explanations
    - Student-friendly language
    """,
    expected_output="""
    A simplified, easy-to-understand explanation of {topic}.
    """,
    agent=simplifier_agent
)

# ==============================
# 3. Prevention Task
# ==============================
prevention_task = Task(
    description="""
    Based on the topic {topic}, provide:
    - Prevention tips
    - Healthy lifestyle recommendations
    - Safety precautions
    - Awareness guidance

    Keep suggestions practical and actionable.
    """,
    expected_output="""
    A structured list of prevention tips and health recommendations for {topic}.
    """,
    agent=prevention_agent
)

# ==============================
# 4. Fact Checking Task
# ==============================
fact_checking_task = Task(
    description="""
    Carefully verify all medical information about {topic}.

    Tasks:
    - Remove false or misleading claims
    - Validate medical accuracy
    - Ensure safe and responsible health information
    - Cross-check consistency between research, simplification, and prevention

    Output only verified content.
    """,
    expected_output="""
    A fully verified and medically accurate version of all {topic} information.
    """,
    agent=fact_checker_agent
)

# ==============================
# 5. Final Response Task
# ==============================
response_task = Task(
    description="""
    Using verified medical information about {topic},
    generate a final user-friendly health awareness report.

    Structure the response clearly and professionally.
    """,
    expected_output="""
    Final structured medical awareness report including:
    - Definition
    - Causes
    - Symptoms
    - Prevention Tips
    - Awareness Note / Disclaimer
    """,
    agent=response_agent
)