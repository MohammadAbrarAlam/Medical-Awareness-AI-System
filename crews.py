# ==========================================
# Medical Awareness Crew (Sequential Pipeline)
# ==========================================

from crewai import Crew, Process
from agents import (
    research_agent,
    simplifier_agent,
    prevention_agent,
    fact_checker_agent,
    response_agent
)

from tasks import (
    research_task,
    simplify_task,
    prevention_task,
    fact_checking_task,
    response_task
)

# ==========================================
# Medical Awareness Crew Definition
# ==========================================
medical_awareness_crew = Crew(
    agents=[
        research_agent,
        simplifier_agent,
        prevention_agent,
        fact_checker_agent,
        response_agent
    ],

    tasks=[
        research_task,
        simplify_task,
        prevention_task,
        fact_checking_task,
        response_task
    ],

    # Sequential flow: each task depends on previous output
    process=Process.sequential,

    verbose=True
)