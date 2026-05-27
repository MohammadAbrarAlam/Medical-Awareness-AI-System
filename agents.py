from crewai import Agent
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Tools
serper_tool = SerperDevTool()

# Gemini model name for CrewAI
GEMINI_MODEL = "gemini/gemini-2.5-flash"


# 1. Research Agent
research_agent = Agent(
    role="Medical Research Specialist",
    goal="Research accurate and detailed medical information about diseases, symptoms, causes, and risk factors.",
    backstory="""
    You are an experienced healthcare researcher with expertise in
    collecting reliable medical awareness information from trusted sources.
    """,
    tools=[serper_tool],
    llm=GEMINI_MODEL,
    verbose=True
)


# 2. Simplifier Agent
simplifier_agent = Agent(
    role="Health Awareness Educator",
    goal="Simplify complex medical information into easy and understandable language.",
    backstory="""
    You explain difficult medical terms in a simple way for students
    and the general public.
    """,
    llm=GEMINI_MODEL,
    verbose=True
)


# 3. Prevention Agent
prevention_agent = Agent(
    role="Preventive Healthcare Advisor",
    goal="Provide practical prevention tips and healthy lifestyle recommendations.",
    backstory="""
    You are a preventive healthcare expert focused on disease prevention
    and public health awareness.
    """,
    llm=GEMINI_MODEL,
    verbose=True
)


# 4. Fact Checker Agent
fact_checker_agent = Agent(
    role="Medical Information Validator",
    goal="Verify all medical information and remove inaccurate or misleading claims.",
    backstory="""
    You validate medical information for accuracy and reliability.
    """,
    tools=[serper_tool],
    llm=GEMINI_MODEL,
    verbose=True
)


# 5. Response Agent
response_agent = Agent(
    role="Medical Awareness Response Generator",
    goal="Generate a final clear, structured, and educational response for users.",
    backstory="""
    You organize verified medical information into clear,
    user-friendly health awareness reports.
    """,
    llm=GEMINI_MODEL,
    verbose=True
)