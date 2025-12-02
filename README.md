# Multi-Agent Research & Content Creation System

A sophisticated multi-agent system built with LangChain that coordinates specialized AI agents to research topics, verify information, and create high-quality content.

**Now supports DeepSeek API for cost-effective, high-quality AI processing!**

## Overview

This project demonstrates advanced multi-agent collaboration where three specialized agents work together:

- **Researcher Agent**: Gathers comprehensive information on topics
- **Fact-Checker Agent**: Verifies claims and ensures accuracy
- **Writer Agent**: Transforms research into polished content

## Features

### Three Workflow Types

1. **Simple Workflow**: Linear process for straightforward content creation
   - Research -> Fact-Check -> Write

2. **Iterative Workflow**: Refinement loop for higher quality
   - Research -> Fact-Check -> Refined Research -> Final Fact-Check -> Write

3. **Comparative Workflow**: Multi-perspective analysis
   - Multiple Research Perspectives -> Cross-Check -> Comparative Analysis

### Key Capabilities

- Automated research gathering with multiple perspectives
- Critical fact-checking and verification
- Multiple writing styles (informative, conversational, technical, analytical)
- Flexible content lengths (short, medium, long)
- Comprehensive workflow tracking and logging
- JSON export of all workflow steps
- **Supports both DeepSeek and OpenAI APIs**

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for fast, reliable dependency management.

### Prerequisites

- Python 3.11+
- uv (installed)
- DeepSeek API key (recommended) OR OpenAI API key

### Setup

1. Clone or navigate to the project directory:
```bash
cd multi-agent
```

2. Dependencies are already installed via uv. If you need to reinstall:
```bash
uv sync
```

3. Set up your API key:

**Option 1: DeepSeek API (Recommended - More Cost-Effective)**
```bash
export DEEPSEEK_API_KEY='your-deepseek-api-key-here'
```

**Option 2: OpenAI API**
```bash
export OPENAI_API_KEY='your-api-key-here'
```

**Option 3: .env File**
Create a `.env` file in the project root:
```
# For DeepSeek (Recommended)
DEEPSEEK_API_KEY=your-deepseek-key-here

# Or for OpenAI
OPENAI_API_KEY=your-openai-key-here
```

### Getting API Keys

**DeepSeek API:**
1. Visit [https://platform.deepseek.com](https://platform.deepseek.com)
2. Sign up and get your API key
3. Much more cost-effective than OpenAI for most tasks

**OpenAI API:**
1. Visit [https://platform.openai.com](https://platform.openai.com)
2. Sign up and get your API key

## Usage

### Running Examples

The `main.py` file includes three example workflows:

```bash
uv run main.py
```

By default, it runs the simple workflow. Edit `main.py` to uncomment other examples:

```python
# Example 1: Simple workflow
example_simple_workflow()

# Example 2: Iterative workflow (uncomment to run)
# example_iterative_workflow()

# Example 3: Comparative workflow (uncomment to run)
# example_comparative_workflow()
```

### Using in Your Own Code

```python
from src.orchestrator.multi_agent_orchestrator import MultiAgentOrchestrator

# Initialize the orchestrator
orchestrator = MultiAgentOrchestrator()

# Run a simple workflow
result = orchestrator.simple_workflow(
    topic="Your topic here",
    context="Additional context",
    writing_style="informative",
    content_length="medium"
)

# Access the final article
print(result["article"]["content"])

# Save results
orchestrator.save_workflow_results(result, "output.json")
```

### Individual Agent Usage

You can also use agents independently:

```python
from src.agents.researcher import ResearcherAgent
from src.agents.fact_checker import FactCheckerAgent
from src.agents.writer import WriterAgent

# Use researcher
researcher = ResearcherAgent()
research = researcher.research("Artificial Intelligence", "Focus on machine learning")

# Use fact-checker
fact_checker = FactCheckerAgent()
fact_check = fact_checker.fact_check(research["findings"], "Artificial Intelligence")

# Use writer
writer = WriterAgent()
article = writer.write_article(
    "Artificial Intelligence",
    research["findings"],
    fact_check["fact_check_report"]
)
```

## Project Structure

```
multi-agent-research/
├── src/
│   ├── agents/
│   │   ├── researcher.py       # Researcher agent implementation
│   │   ├── fact_checker.py     # Fact-checker agent implementation
│   │   └── writer.py           # Writer agent implementation
│   ├── orchestrator/
│   │   └── multi_agent_orchestrator.py  # Workflow coordination
│   └── tools/                  # (Future: Custom tools)
├── main.py                     # Example usage and demos
├── pyproject.toml              # Project dependencies (uv)
├── uv.lock                     # Locked dependencies
└── README.md                   # This file
```


## Workflow Details

### Simple Workflow

Perfect for quick content generation:

```python
result = orchestrator.simple_workflow(
    topic="Climate change solutions",
    context="Focus on renewable energy",
    writing_style="informative",
    content_length="medium"
)
```

**Process:**
1. Researcher gathers information
2. Fact-checker verifies accuracy
3. Writer creates final content

### Iterative Workflow

Best for high-quality, thoroughly vetted content:

```python
result = orchestrator.iterative_workflow(
    topic="Quantum computing",
    initial_context="Cover applications and theory",
    writing_style="technical",
    content_length="long"
)
```

**Process:**
1. Initial research
2. First fact-check identifies gaps
3. Refined research addresses issues
4. Final fact-check ensures quality
5. Writer creates polished content

### Comparative Workflow

Ideal for analyzing multiple perspectives:

```python
result = orchestrator.comparative_workflow(
    topic="Electric vehicles",
    perspectives=[
        "Environmental impact",
        "Economic considerations",
        "Infrastructure challenges"
    ],
    writing_style="analytical"
)
```

**Process:**
1. Research each perspective independently
2. Cross-check perspectives for consistency
3. Overall fact-check of all findings
4. Writer creates comparative analysis

## Configuration

### Model Selection

**Using DeepSeek (Default):**
```python
orchestrator = MultiAgentOrchestrator(model_name="deepseek-chat")
```

**Using OpenAI:**
```python
orchestrator = MultiAgentOrchestrator(
    model_name="gpt-4o-mini",
    base_url="https://api.openai.com/v1"
)
```

**Or configure individual agents:**
```python
researcher = ResearcherAgent(model_name="deepseek-chat", temperature=0.8)
fact_checker = FactCheckerAgent(model_name="deepseek-chat", temperature=0.2)
writer = WriterAgent(model_name="deepseek-chat", temperature=0.7)
```

### Available Models

**DeepSeek Models:**
- `deepseek-chat` - Main chat model (recommended, cost-effective)
- `deepseek-coder` - Specialized for code-related tasks

**OpenAI Models:**
- `gpt-4o` - Most capable OpenAI model
- `gpt-4o-mini` - Fast and cost-effective
- `gpt-4-turbo` - Previous generation flagship

### Temperature Settings

- **Researcher**: Default 0.7 (balanced creativity/accuracy)
- **Fact-Checker**: Default 0.3 (more deterministic)
- **Writer**: Default 0.7 (creative but accurate)

## Output

Each workflow generates:

1. **Console Output**: Progress updates and final content
2. **JSON File**: Complete workflow history including:
   - All agent interactions
   - Timestamps for each step
   - Intermediate results
   - Final outputs

Example JSON structure:
```json
{
  "workflow_type": "simple",
  "topic": "Your topic",
  "research": {...},
  "fact_check": {...},
  "article": {...},
  "workflow_history": [...]
}
```

## Advanced Features

### Get Summary

Generate a concise summary of any workflow result:

```python
summary = orchestrator.get_summary(result)
print(summary)
```

### Workflow History

Access detailed logs of all agent interactions:

```python
for step in orchestrator.workflow_history:
    print(f"{step['timestamp']}: {step['agent']} - {step['step']}")
```

### Custom Writing Styles

Available styles:
- `informative`: Clear, educational content
- `conversational`: Casual, engaging tone
- `technical`: Detailed, precise language
- `journalistic`: News-style reporting
- `analytical`: Critical analysis and evaluation

## Dependencies

Core dependencies (managed by uv):
- `langchain` - Core LangChain framework
- `langchain-openai` - OpenAI-compatible API integration (works with DeepSeek)
- `langchain-community` - Community tools
- `langchain-core` - Core abstractions
- `python-dotenv` - Environment variable management

**Note:** Despite the name `langchain-openai`, this package works with any OpenAI-compatible API, including DeepSeek.

## Future Enhancements

Potential additions:
- [ ] Web search integration for real-time research
- [ ] Custom tools for specialized research domains
- [x] Support for multiple LLM providers (DeepSeek, OpenAI)
- [ ] Support for more providers (Anthropic, Cohere, etc.)
- [ ] Interactive workflow mode with user feedback
- [ ] Export to multiple formats (PDF, HTML, Markdown)
- [ ] Agent memory for context retention across sessions
- [ ] Parallel processing for comparative workflows

## Contributing

This is a demonstration project. Feel free to fork and extend with:
- New agent types (Editor, Critic, Summarizer)
- Custom workflows
- Integration with external APIs
- Enhanced fact-checking tools

## License

This project is provided as-is for educational and demonstration purposes.

## Troubleshooting

**"No API key found"**
- Ensure your DEEPSEEK_API_KEY or OPENAI_API_KEY is set in environment variables or .env file
- The system will automatically detect which API to use based on available keys

**Import errors**
- Run `uv sync` to ensure all dependencies are installed

**Model not found errors**
- For DeepSeek: Ensure you're using `deepseek-chat` or `deepseek-coder`
- For OpenAI: Try using `gpt-4o-mini` as it's widely available
- Check that your API key has access to the specified model

**API connection errors**
- Verify your API key is correct
- Check your internet connection
- For DeepSeek, ensure base_url is set to `https://api.deepseek.com`

## Learn More

- [LangChain Documentation](https://python.langchain.com/)
- [uv Documentation](https://github.com/astral-sh/uv)
- [DeepSeek API Documentation](https://platform.deepseek.com/docs)
- [OpenAI API Documentation](https://platform.openai.com/docs/)

---

Built with LangChain, uv, and DeepSeek API
