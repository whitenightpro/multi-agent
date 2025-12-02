# DeepSeek API Setup Guide

This guide will help you set up and use DeepSeek API with the Multi-Agent Research System.

## Why DeepSeek?

DeepSeek offers:
- **Cost-Effective**: Significantly cheaper than OpenAI
- **High Quality**: Competitive performance for most tasks
- **OpenAI-Compatible**: Drop-in replacement with minimal changes
- **Fast**: Quick response times

## Getting Your DeepSeek API Key

1. **Visit DeepSeek Platform**
   - Go to [https://platform.deepseek.com](https://platform.deepseek.com)

2. **Sign Up**
   - Create an account using email or social login
   - Verify your email address

3. **Get API Key**
   - Navigate to the API Keys section
   - Click "Create API Key"
   - Copy your API key (starts with `sk-`)
   - Store it securely - you won't be able to see it again

4. **Add Credits (Optional)**
   - DeepSeek may provide free credits for new users
   - Add credits to your account if needed

## Configuration

### Option 1: Environment Variable

**Linux/macOS:**
```bash
export DEEPSEEK_API_KEY='sk-your-key-here'
```

**Windows (PowerShell):**
```powershell
$env:DEEPSEEK_API_KEY='sk-your-key-here'
```

**Windows (Command Prompt):**
```cmd
set DEEPSEEK_API_KEY=sk-your-key-here
```

### Option 2: .env File (Recommended)

Create a `.env` file in the project root:

```env
DEEPSEEK_API_KEY=sk-your-key-here
DEEPSEEK_BASE_URL=https://api.deepseek.com
```

The `.env` file will be automatically loaded by the application.

## Available Models

### deepseek-chat (Default)
- General-purpose chat model
- Best for most tasks including research, writing, analysis
- **Recommended for this project**

### deepseek-coder
- Specialized for code-related tasks
- Better for technical documentation or programming content
- Use when your research topic is code-heavy

## Usage Examples

### Basic Usage (Default Settings)

The system uses DeepSeek by default:

```python
from src.orchestrator.multi_agent_orchestrator import MultiAgentOrchestrator

# Will automatically use DeepSeek if DEEPSEEK_API_KEY is set
orchestrator = MultiAgentOrchestrator()

result = orchestrator.simple_workflow(
    topic="Your topic here",
    context="Additional context"
)
```

### Explicit DeepSeek Configuration

```python
orchestrator = MultiAgentOrchestrator(
    model_name="deepseek-chat",
    api_key="sk-your-key-here",  # Optional if using .env
    base_url="https://api.deepseek.com"
)
```

### Using DeepSeek Coder

```python
orchestrator = MultiAgentOrchestrator(
    model_name="deepseek-coder"
)

result = orchestrator.simple_workflow(
    topic="Python async/await patterns",
    context="Technical deep-dive for experienced developers"
)
```

### Individual Agent Configuration

```python
from src.agents.researcher import ResearcherAgent
from src.agents.fact_checker import FactCheckerAgent
from src.agents.writer import WriterAgent

# Mix models for different agents
researcher = ResearcherAgent(model_name="deepseek-chat")
fact_checker = FactCheckerAgent(model_name="deepseek-chat", temperature=0.2)
writer = WriterAgent(model_name="deepseek-coder")  # Use coder for technical writing
```

## Cost Comparison

**Approximate costs per 1M tokens (as of 2024):**

| Provider | Input | Output |
|----------|-------|--------|
| DeepSeek Chat | $0.14 | $0.28 |
| GPT-4o-mini | $0.15 | $0.60 |
| GPT-4o | $2.50 | $10.00 |

**Example workflow costs:**
- Simple workflow (DeepSeek): ~$0.001-0.003
- Simple workflow (GPT-4o-mini): ~$0.01-0.03
- Iterative workflow (DeepSeek): ~$0.002-0.005
- Iterative workflow (GPT-4o-mini): ~$0.02-0.05

💡 **DeepSeek can be 10-30x cheaper for similar quality!**

## Testing Your Setup

Run the test script to verify everything works:

```bash
uv run test_agents.py
```

Expected output:
```
✓ Using DeepSeek API

Testing Multi-Agent System...

1. Testing Researcher Agent...
✓ Researcher working! Generated 1234 characters

2. Testing Fact-Checker Agent...
✓ Fact-Checker working! Generated 567 characters

3. Testing Writer Agent...
✓ Writer working! Generated 890 characters

============================================================
✅ All agents are working correctly!
============================================================

You can now run: uv run main.py
```

## Troubleshooting

### "API key not found"
- Check your .env file exists and has the correct format
- Verify the API key starts with `sk-`
- Try setting the environment variable directly

### "Invalid API key"
- Verify you copied the complete key
- Check for extra spaces or quotes
- Generate a new API key from the DeepSeek platform

### "Model not found"
- DeepSeek models: `deepseek-chat`, `deepseek-coder`
- Don't use OpenAI model names with DeepSeek API

### Connection errors
- Check your internet connection
- Verify base_url is `https://api.deepseek.com`
- Check if DeepSeek API is experiencing downtime

### Slow responses
- First request may be slower (cold start)
- Subsequent requests should be faster
- Consider reducing content_length if needed

## Switching Between DeepSeek and OpenAI

The system automatically detects which API to use:

**Priority:**
1. If `DEEPSEEK_API_KEY` is set → Uses DeepSeek
2. If only `OPENAI_API_KEY` is set → Uses OpenAI

**Force OpenAI usage:**
```python
orchestrator = MultiAgentOrchestrator(
    model_name="gpt-4o-mini",
    base_url="https://api.openai.com/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)
```

## Best Practices

1. **Use .env file** for API keys (never commit to git)
2. **Start with deepseek-chat** for general tasks
3. **Monitor token usage** via DeepSeek dashboard
4. **Set temperature appropriately**:
   - Research: 0.7
   - Fact-checking: 0.3
   - Creative writing: 0.8+
5. **Test with small workflows** before large batches

## Getting Help

- **DeepSeek Documentation**: [https://platform.deepseek.com/docs](https://platform.deepseek.com/docs)
- **DeepSeek Discord**: Community support and discussions
- **Project Issues**: [Report issues on GitHub]

---

Ready to start? Set your API key and run:
```bash
export DEEPSEEK_API_KEY='your-key'
uv run main.py
```
