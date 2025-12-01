from langgraph.graph import StateGraph, END
from schemas import AgentState
from nodes import (
    analyze_job_node,
    analyze_resume_node,
    compare_gaps_node,
    research_resources_node,
    report_node
)

def build_graph():
    """Constructs and compiles the LangGraph workflow."""
    
    workflow = StateGraph(AgentState)

    # Add Nodes
    workflow.add_node("analyze_jd", analyze_job_node)
    workflow.add_node("analyze_resume", analyze_resume_node)
    workflow.add_node("find_gaps", compare_gaps_node)
    workflow.add_node("research", research_resources_node)
    workflow.add_node("report", report_node)

    # Add Edges (Linear flow)
    workflow.set_entry_point("analyze_jd")
    workflow.add_edge("analyze_jd", "analyze_resume")
    workflow.add_edge("analyze_resume", "find_gaps")
    workflow.add_edge("find_gaps", "research")
    workflow.add_edge("research", "report")
    workflow.add_edge("report", END)

    # Compile
    return workflow.compile()

# Expose the compiled app
app = build_graph()