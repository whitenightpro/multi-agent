# Quick Reference Guide

## Project Overview
Multi-Agent Research & Content Creation System with DeepSeek API support.

## Quick Start

### 1. Set API Key
```bash
export DEEPSEEK_API_KEY='your-key-here'
```

### 2. Test Setup
```bash
uv run test_agents.py
```

### 3. Run Example
```bash
uv run main.py
```

## File Structure

```
multi-agent-research/
├── src/agents/              # Agent implementations
│   ├── researcher.py        # Research agent
│   ├── fact_checker.py      # Fact-checking agent
│   └── writer.py            # Writing agent
├── src/orchestrator/        # Workflow coordination
│   └── multi_agent_orchestrator.py
├── main.py                  # Example workflows
├── test_agents.py           # Quick test script
└── *.md                     # Documentation
```

## Common Commands

### Run Workflows
```bash
# Simple workflow (default)
uv run main.py

# Edit main.py to enable other workflows
```

### Test Agents
```bash
uv run test_agents.py
```

### Check Dependencies
```bash
uv sync
```

## API Configuration

### DeepSeek (Default)
```env
DEEPSEEK_API_KEY=sk-your-key
DEEPSEEK_BASE_URL=https://api.deepseek.com
```

### OpenAI (Alternative)
```env
OPENAI_API_KEY=sk-your-key
```

## Available Workflows

### 1. Simple Workflow
Research → Fact-Check → Write
```python
orchestrator.simple_workflow(
    topic="Your topic",
    context="Additional context",
    writing_style="informative",
    content_length="medium"
)
```

### 2. Iterative Workflow
Research → Fact-Check → Refined Research → Write
```python
orchestrator.iterative_workflow(
    topic="Your topic",
    initial_context="Context",
    writing_style="informative",
    content_length="medium"
)
```

### 3. Comparative Workflow
Multi-perspective → Cross-check → Compare
```python
orchestrator.comparative_workflow(
    topic="Your topic",
    perspectives=[
        "Perspective 1",
        "Perspective 2",
        "Perspective 3"
    ],
    writing_style="analytical"
)
```

## Agent Parameters

### Models
- **DeepSeek**: `deepseek-chat`, `deepseek-coder`
- **OpenAI**: `gpt-4o-mini`, `gpt-4o`, `gpt-4-turbo`

### Writing Styles
- `informative` - Educational content
- `conversational` - Casual, engaging
- `technical` - Detailed, precise
- `journalistic` - News-style
- `analytical` - Critical analysis

### Content Lengths
- `short` - 500-800 words
- `medium` - 1000-1500 words
- `long` - 2000+ words

## Code Examples

### Basic Usage
```python
from src.orchestrator.multi_agent_orchestrator import MultiAgentOrchestrator

orchestrator = MultiAgentOrchestrator()
result = orchestrator.simple_workflow(
    topic="AI in Healthcare",
    context="Focus on practical applications"
)

print(result["article"]["content"])
```

### Individual Agents
```python
from src.agents.researcher import ResearcherAgent

researcher = ResearcherAgent()
research = researcher.research(
    "Climate Change",
    "Focus on solutions"
)
```

### Custom Configuration
```python
orchestrator = MultiAgentOrchestrator(
    model_name="deepseek-chat",
    api_key="your-key",
    base_url="https://api.deepseek.com"
)
```

## Output Files

Each workflow saves:
- `output_simple_workflow.json` - Simple workflow results
- `output_iterative_workflow.json` - Iterative workflow results
- `output_comparative_workflow.json` - Comparative workflow results

## Troubleshooting Quick Fixes

**No API key found**
```bash
export DEEPSEEK_API_KEY='your-key'
```

**Import errors**
```bash
uv sync
```

**Model errors**
- DeepSeek: Use `deepseek-chat`
- OpenAI: Use `gpt-4o-mini`

## Documentation Files

- `README.md` - Main documentation
- `DEEPSEEK_SETUP.md` - DeepSeek API setup guide
- `ARCHITECTURE.md` - System architecture
- `EXAMPLES.md` - Detailed examples
- `QUICK_REFERENCE.md` - This file

## Getting Help

1. Check `DEEPSEEK_SETUP.md` for API setup
2. See `EXAMPLES.md` for usage examples
3. Review `ARCHITECTURE.md` for system design
4. Run `uv run test_agents.py` to test setup

---

**Quick Test:**
```bash
export DEEPSEEK_API_KEY='your-key'
uv run test_agents.py
uv run main.py
```
