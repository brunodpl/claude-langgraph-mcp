# Claude LangGraph MCP Tool

A Multi-Agent Control Protocol tool built with LangGraph, designed to work with Claude and other AI agents. This tool enables complex workflows between different AI agents, with Claude as the primary orchestrator.

## Features

- Multi-agent workflow orchestration
- Integration with Claude API
- Extensible agent architecture
- State management across workflow steps
- Interactive chat interface using Chainlit

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your Anthropic API key
4. Run the application:
   ```bash
   chainlit run main.py
   ```

## Architecture

- `agents/`: Contains agent implementations
  - `base_agent.py`: Base agent class
  - `claude_agent.py`: Claude-specific agent implementation
- `workflow/`: Workflow management
  - `graph.py`: LangGraph workflow definition
- `main.py`: Application entry point

## Usage

The tool uses a three-agent system:
1. Planner: Breaks down tasks into steps
2. Executor: Carries out individual steps
3. Synthesizer: Combines results into final output

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License