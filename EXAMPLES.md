# Example Outputs

This document shows what to expect from each workflow type.

## Simple Workflow Example

### Input
```python
orchestrator.simple_workflow(
    topic="The impact of artificial intelligence on healthcare",
    context="Focus on practical applications and current implementations",
    writing_style="informative",
    content_length="medium"
)
```

### Console Output
```
============================================================
Starting Simple Workflow for: The impact of artificial intelligence on healthcare
============================================================

[1/3] 🔍 Researcher Agent: Gathering information...
✓ Research completed

[2/3] ✅ Fact-Checker Agent: Verifying findings...
✓ Fact-checking completed

[3/3] ✍️  Writer Agent: Creating content...
✓ Writing completed

============================================================
Workflow Complete!
============================================================

📄 FINAL ARTICLE:
--------------------------------------------------------------------------------
[Article content appears here - typically 1000-1500 words]
--------------------------------------------------------------------------------
```

### JSON Output Structure
```json
{
  "workflow_type": "simple",
  "topic": "The impact of artificial intelligence on healthcare",
  "research": {
    "agent": "Researcher",
    "topic": "...",
    "findings": "Comprehensive research content...",
    "needs_fact_checking": true
  },
  "fact_check": {
    "agent": "FactChecker",
    "topic": "...",
    "fact_check_report": "Detailed fact-check analysis...",
    "status": "reviewed"
  },
  "article": {
    "agent": "Writer",
    "topic": "...",
    "style": "informative",
    "content_type": "article",
    "content": "Final polished article..."
  },
  "workflow_history": [
    {
      "timestamp": "2025-12-02T20:15:30.123456",
      "step": "research",
      "agent": "Researcher",
      "data": {...}
    },
    ...
  ]
}
```

## Iterative Workflow Example

### Input
```python
orchestrator.iterative_workflow(
    topic="Quantum computing and its potential applications",
    initial_context="Cover both theoretical foundations and practical uses",
    writing_style="informative",
    content_length="medium"
)
```

### Console Output
```
============================================================
Starting Iterative Workflow for: Quantum computing and its potential applications
============================================================

[1/5] 🔍 Researcher Agent: Initial research...
✓ Initial research completed

[2/5] ✅ Fact-Checker Agent: Reviewing findings...
✓ Fact-checking completed

[3/5] 🔍 Researcher Agent: Refined research based on feedback...
✓ Refined research completed

[4/5] ✅ Fact-Checker Agent: Final verification...
✓ Final fact-checking completed

[5/5] ✍️  Writer Agent: Creating final content...
✓ Writing completed

============================================================
Iterative Workflow Complete!
============================================================

📄 FINAL ARTICLE:
--------------------------------------------------------------------------------
[Enhanced article with refined research appears here]
--------------------------------------------------------------------------------

📋 SUMMARY:
--------------------------------------------------------------------------------
[3-paragraph summary of the article]
--------------------------------------------------------------------------------
```

### Key Differences from Simple Workflow
- Two rounds of research (initial + refined)
- Two fact-checks (initial + final)
- Higher quality output due to iterative refinement
- Addresses gaps identified in first fact-check

## Comparative Workflow Example

### Input
```python
orchestrator.comparative_workflow(
    topic="Remote work vs. office work",
    perspectives=[
        "Benefits and challenges from an employee perspective",
        "Impact on company productivity and culture",
        "Environmental and societal implications"
    ],
    writing_style="analytical"
)
```

### Console Output
```
============================================================
Starting Comparative Workflow for: Remote work vs. office work
Analyzing 3 perspectives
============================================================

[1/3] 🔍 Researcher Agent: Researching 'Benefits and challenges from an employee perspective'...
✓ Research for 'Benefits and challenges from an employee perspective' completed

[2/3] 🔍 Researcher Agent: Researching 'Impact on company productivity and culture'...
✓ Research for 'Impact on company productivity and culture' completed

[3/3] 🔍 Researcher Agent: Researching 'Environmental and societal implications'...
✓ Research for 'Environmental and societal implications' completed

[*] ✅ Fact-Checker Agent: Cross-checking perspectives...
✓ Cross-checking completed

[*] ✅ Fact-Checker Agent: Fact-checking all perspectives...
✓ Fact-checking completed

[*] ✍️  Writer Agent: Creating comparative analysis...
✓ Comparative analysis completed

============================================================
Comparative Workflow Complete!
============================================================

📄 COMPARATIVE ANALYSIS:
--------------------------------------------------------------------------------
[Comprehensive comparison analyzing all perspectives]

Introduction
[Overview of the topic and perspectives being compared]

Perspective 1: Employee Benefits and Challenges
[Detailed analysis]

Perspective 2: Company Productivity and Culture
[Detailed analysis]

Perspective 3: Environmental and Societal Impact
[Detailed analysis]

Synthesis and Conclusions
[Balanced analysis of all perspectives]
--------------------------------------------------------------------------------
```

## Individual Agent Usage Examples

### Researcher Agent Only
```python
researcher = ResearcherAgent()

# General research
result = researcher.research(
    topic="Climate change",
    context="Focus on recent developments"
)

# Focused research with specific questions
result = researcher.focused_research(
    topic="Climate change",
    specific_questions=[
        "What are the latest IPCC findings?",
        "What technology solutions show promise?",
        "How are different countries responding?"
    ]
)
```

### Fact-Checker Agent Only
```python
fact_checker = FactCheckerAgent()

# Fact-check content
result = fact_checker.fact_check(
    research_content="Content to verify...",
    topic="Climate change"
)

# Verify specific claims
result = fact_checker.verify_specific_claims(
    claims=[
        "Global temperatures have risen 1.1°C since pre-industrial times",
        "Renewable energy is now cheaper than fossil fuels",
        "Sea levels could rise 2 meters by 2100"
    ],
    context="Climate change data"
)

# Cross-check two sources
result = fact_checker.cross_check(
    research_a="First source content...",
    research_b="Second source content...",
    topic="Climate change"
)
```

### Writer Agent Only
```python
writer = WriterAgent()

# Write an article
result = writer.write_article(
    topic="Climate change",
    research_content="Research findings...",
    fact_check_report="Fact-check results...",
    style="journalistic",
    target_length="long"
)

# Write a summary
result = writer.write_summary(
    topic="Climate change",
    research_content="Long research document...",
    max_paragraphs=3
)

# Write a comparison
result = writer.write_comparison(
    topic="Energy sources",
    perspectives={
        "Solar": "Solar energy research...",
        "Wind": "Wind energy research...",
        "Nuclear": "Nuclear energy research..."
    },
    cross_check_report="Cross-check analysis..."
)

# Refine content
result = writer.refine_content(
    original_content="Draft article...",
    feedback="Make more concise, add examples",
    focus_areas=["clarity", "engagement"]
)
```

## Workflow History Example

Each workflow maintains a complete history:

```python
for step in orchestrator.workflow_history:
    print(f"{step['timestamp']}: {step['agent']} - {step['step']}")

# Output:
# 2025-12-02T20:15:30.123456: Researcher - research
# 2025-12-02T20:15:45.789012: FactChecker - fact_check
# 2025-12-02T20:16:00.345678: Writer - write
```

## Error Handling Examples

### Missing API Key
```
⚠️  WARNING: OPENAI_API_KEY not found in environment variables.
Please set your OpenAI API key:
  export OPENAI_API_KEY='your-api-key-here'

Or create a .env file with:
  OPENAI_API_KEY=your-api-key-here
```

### API Error
```python
try:
    result = orchestrator.simple_workflow(...)
except Exception as e:
    print(f"Workflow failed: {e}")
    # Handle error appropriately
```

## Performance Notes

### Typical Timing (with gpt-4o-mini)
- Simple Workflow: ~30-60 seconds
- Iterative Workflow: ~60-120 seconds
- Comparative Workflow (3 perspectives): ~90-150 seconds

### Token Usage (approximate)
- Research phase: 500-2000 tokens
- Fact-checking: 300-1000 tokens
- Writing: 800-3000 tokens
- Total per workflow: 2000-8000 tokens

### Cost Considerations (with gpt-4o-mini)
- Simple workflow: ~$0.01-0.03
- Iterative workflow: ~$0.02-0.05
- Comparative workflow: ~$0.03-0.08

*Note: Costs vary based on content length, complexity, and API pricing*

## Tips for Best Results

1. **Be Specific**: Provide clear context in your topics
2. **Choose Appropriate Workflow**:
   - Simple for quick content
   - Iterative for quality
   - Comparative for multi-perspective analysis
3. **Adjust Temperature**: Lower for factual content, higher for creative
4. **Monitor Output**: Review fact-check reports for quality insights
5. **Use Workflow History**: Debug issues by examining step-by-step execution

---

For more examples, see `main.py` and `test_agents.py`.
