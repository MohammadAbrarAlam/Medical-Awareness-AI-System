from crewai import Agent, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

load_dotenv()

# Gemini LLM
llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

# Tool
serper_tool = SerperDevTool()


# 1. Research Agent
research_agent = Agent(
    role="Medical Research Specialist",
    goal="Research accurate medical information about diseases, symptoms, causes, and risk factors.",
    backstory="""
    You are an experienced healthcare researcher who gathers
    trusted medical awareness information from reliable sources.
    """,
    tools=[serper_tool],
    llm=llm,
    verbose=True
)


# 2. Simplifier Agent
simplifier_agent = Agent(
    role="Health Awareness Educator",
    goal="Simplify complex medical information into easy language.",
    backstory="""
    You explain difficult healthcare topics clearly for students
    and the general public.
    """,
    llm=llm,
    verbose=True
)


# 3. Prevention Agent
prevention_agent = Agent(
    role="Preventive Healthcare Advisor",
    goal="Provide practical prevention tips and healthy lifestyle advice.",
    backstory="""
    You specialize in prevention, wellness, and public health awareness.
    """,
    llm=llm,
    verbose=True
)


# 4. Fact Checker Agent
fact_checker_agent = Agent(
    role="Medical Information Validator",
    goal="Verify all medical information and remove inaccurate claims.",
    backstory="""
    You validate healthcare information for safety and accuracy.
    """,
    tools=[serper_tool],
    llm=llm,
    verbose=True
)


# 5. Response Agent
response_agent = Agent(
    role="Medical Awareness Response Generator",
    goal="Generate clear and educational final responses for users.",
    backstory="""
    You organize verified medical information into
    easy-to-read health awareness reports.
    """,
    llm=llm,
    verbose=True
)