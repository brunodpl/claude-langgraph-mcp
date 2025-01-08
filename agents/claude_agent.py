from typing import Dict, Any
from .base_agent import BaseAgent
from anthropic import Anthropic
import os

class ClaudeAgent(BaseAgent):
    """Agent class for Claude integration."""
    def __init__(self, name: str):
        super().__init__(name)
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process input using Claude API."""
        messages = input_data.get("messages", [])
        
        response = await self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            messages=messages
        )
        
        self.update_state(
            messages=messages + [response.content],
            current_step="completed"
        )
        
        return {
            "response": response.content,
            "state": self.get_state()
        }