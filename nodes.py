import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from schemas import AgentState, SkillAnalysis, GapAnalysis, Resource
from tools import get_search_tool

# Load environment variables (ensure .env is loaded before initializing LLM)
load_dotenv()

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Initialize Tool
search_tool = get_search_tool()

def analyze_job_node(state: AgentState):
    """Node 1: Extract requirements from the Job Description."""
    print("--- NODE: Analyzing Job Description ---")
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert HR Talent Acquisition Specialist. Extract skills strictly."),
        ("user", "Analyze this Job Description: {jd}")
    ])
    
    extractor = prompt | llm.with_structured_output(SkillAnalysis)
    result = extractor.invoke({"jd": state["job_description"]})
    
    return {"job_requirements": result}

def analyze_resume_node(state: AgentState):
    """Node 2: Extract skills from the Resume."""
    print("--- NODE: Analyzing Resume ---")
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert Resume Analyst. Extract skills strictly."),
        ("user", "Analyze this Resume Text: {resume}")
    ])
    
    extractor = prompt | llm.with_structured_output(SkillAnalysis)
    result = extractor.invoke({"resume": state["resume_text"]})
    
    return {"resume_profile": result}

def compare_gaps_node(state: AgentState):
    """Node 3: Identify gaps between JD and Resume."""
    print("--- NODE: Identifying Gaps ---")
    
    jd_skills = state["job_requirements"]
    resume_skills = state["resume_profile"]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Compare the candidate profile against job requirements. Be critical."),
        ("user", """
        Job Requirements: {jd_skills}
        Candidate Profile: {resume_skills}
        
        Identify strictly what is MISSING in the candidate profile.
        """)
    ])
    
    comparator = prompt | llm.with_structured_output(GapAnalysis)
    result = comparator.invoke({
        "jd_skills": jd_skills.model_dump(),
        "resume_skills": resume_skills.model_dump()
    })
    
    return {"gap_data": result}

def research_resources_node(state: AgentState):
    """Node 4: Use Tools to find resources for missing skills."""
    print("--- NODE: Researching Learning Resources (Tool Calling) ---")
    
    missing_skills = state["gap_data"].missing_technical_skills
    resources = []
    
    if not missing_skills:
        return {"learning_plan": []}

    for skill in missing_skills[:3]: 
        print(f"   Searching resources for: {skill}")
        try:
            search_results = search_tool.invoke(f"best free tutorial for learning {skill}")
            if search_results:
                top_result = search_results[0]
                resources.append(Resource(
                    skill=skill,
                    resource_title=top_result.get("content", "Tutorial"),
                    url=top_result.get("url", "#")
                ))
        except Exception as e:
            print(f"   Error searching for {skill}: {e}")

    return {"learning_plan": resources}

def report_node(state: AgentState):
    """Node 5: Generate the final Markdown report."""
    print("--- NODE: Generating Report ---")
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a Career Coach. Write a Markdown report based on the provided analysis."),
        ("user", """
        Gap Analysis: {gaps}
        Learning Plan: {plan}
        
        Write a friendly but professional conclusion encouraging the candidate.
        Format it nicely with Markdown headers.
        """)
    ])
    
    chain = prompt | llm
    result = chain.invoke({
        "gaps": state["gap_data"].model_dump(),
        "plan": [res.model_dump() for res in state["learning_plan"]]
    })
    
    return {"final_report": result.content}