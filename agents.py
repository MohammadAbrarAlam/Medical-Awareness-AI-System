from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# ==============================
# Gemini LLM
# ==============================
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.3
)

# ==============================
# Tools
# ==============================
serper_tool = SerperDevTool()

# ==============================
# 1. Research Agent
# ==============================
research_agent = Agent(
    role="Medical Research Specialist",
    goal="Research accurate and detailed medical information about diseases, symptoms, causes, and risk factors.",
    backstory="""
    You are an experienced healthcare researcher with expertise in
    collecting reliable medical awareness information from trusted medical sources.
    """,
    tools=[serper_tool],
    llm=llm,
    verbose=True
)

# ==============================
# 2. Simplifier Agent
# ==============================
simplifier_agent = Agent(
    role="Health Awareness Educator",
    goal="Simplify complex medical information into easy and understandable language.",
    backstory="""
    You explain difficult medical terms in simple language for students
    and the general public.
    """,
    llm=llm,
    verbose=True
)

# ==============================
# 3. Prevention Agent
# ==============================
prevention_agent = Agent(
    role="Preventive Healthcare Advisor",
    goal="Provide practical prevention tips and healthy lifestyle recommendations.",
    backstory="""
    You are a preventive healthcare expert focused on disease prevention
    and public health awareness.
    """,
    llm=llm,
    verbose=True
)

# ==============================
# 4. Fact Checker Agent
# ==============================
fact_checker_agent = Agent(
    role="Medical Information Validator",
    goal="Verify all medical information and remove inaccurate or misleading claims.",
    backstory="""
    You validate medical information for accuracy,
    reliability, and safety.
    """,
    tools=[serper_tool],
    llm=llm,
    verbose=True
)

# ==============================
# 5. Response Agent
# ==============================
response_agent = Agent(
    role="Medical Awareness Response Generator",
    goal="Generate a final clear, structured, and educational response for users.",
    backstory="""
    You organize verified medical information into clear,
    user-friendly health awareness reports.
    """,
    llm=llm,
    verbose=True
)