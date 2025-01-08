from typing import Dict, Any
from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel

class WorkflowState(BaseModel):
    """State maintained across the workflow."""
    input: str
    agents: Dict[str, Dict[str, Any]] = {}
    output: str = ""

def create_workflow(agents: Dict[str, Any]):
    """Create a workflow graph with the given agents."""
    workflow = StateGraph(WorkflowState)
    
    # Add nodes for each agent
    for agent_name, agent in agents.items():
        workflow.add_node(agent_name, agent.process)
    
    # Add edges based on workflow logic
    workflow.add_edge(START, "planner")
    
    # Add conditional edges
    def should_end(state: WorkflowState) -> str:
        return END if state.output else "executor"
    
    workflow.add_conditional_edges(
        "executor",
        should_end,
        {END: END, "synthesizer": "synthesizer"}
    )
    
    return workflow.compile()