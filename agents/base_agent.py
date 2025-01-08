from typing import Dict, Any, Optional
from pydantic import BaseModel, Field

class AgentState(BaseModel):
    """Base state for all agents in the system."""
    context: Dict[str, Any] = Field(default_factory=dict)
    messages: list = Field(default_factory=list)
    current_step: Optional[str] = None
    status: str = "ready"

class BaseAgent:
    """Base agent class that all specialized agents inherit from."""
    def __init__(self, name: str):
        self.name = name
        self.state = AgentState()
    
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process input data and return results."""
        raise NotImplementedError("Subclasses must implement process method")
    
    def update_state(self, **kwargs):
        """Update agent state with new information."""
        for key, value in kwargs.items():
            if hasattr(self.state, key):
                setattr(self.state, key, value)
    
    def get_state(self) -> Dict[str, Any]:
        """Return current agent state."""
        return self.state.dict()