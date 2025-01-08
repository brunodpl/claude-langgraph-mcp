import os
import chainlit as cl
from dotenv import load_dotenv
from agents.claude_agent import ClaudeAgent
from workflow.graph import create_workflow

# Load environment variables
load_dotenv()

# Initialize agents
planner = ClaudeAgent("planner")
executor = ClaudeAgent("executor")
synthesizer = ClaudeAgent("synthesizer")

# Create workflow
workflow = create_workflow({
    "planner": planner,
    "executor": executor,
    "synthesizer": synthesizer
})

@cl.on_chat_start
async def start():
    await cl.Message(content="Hello! I'm your AI assistant. How can I help you today?").send()

@cl.on_message
async def main(message: cl.Message):
    # Initialize workflow state
    state = {
        "input": message.content,
        "agents": {},
        "output": ""
    }
    
    # Process through workflow
    async for event in workflow.astream(state):
        if "agent_response" in event:
            await cl.Message(content=event["agent_response"]).send()

if __name__ == "__main__":
    cl.run()