# Multi-Agent System Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                  Multi-Agent Orchestrator                   │
│                                                             │
│  Coordinates workflows and manages agent interactions      │
└─────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────┼─────────┐
                    ▼         ▼         ▼
        ┌───────────────┐ ┌─────────────┐ ┌──────────────┐
        │  Researcher   │ │ Fact-Checker│ │    Writer    │
        │     Agent     │ │    Agent    │ │    Agent     │
        └───────────────┘ └─────────────┘ └──────────────┘
             │                   │               │
             │                   │               │
             ▼                   ▼               ▼
        [Research]         [Verify]         [Create]
        [Findings]         [Claims]         [Content]
```

## Agent Responsibilities

### 1. Researcher Agent
**Role:** Information Gathering
- Conducts comprehensive research on topics
- Provides multiple perspectives
- Identifies key subtopics
- Simulates source citations
- Flags areas needing verification

**Key Methods:**
- `research(topic, context)` - General research
- `focused_research(topic, questions)` - Targeted research

### 2. Fact-Checker Agent
**Role:** Quality Assurance
- Verifies research claims
- Identifies inaccuracies
- Checks for logical consistency
- Detects bias
- Provides accuracy ratings (HIGH/MEDIUM/LOW/UNVERIFIABLE)

**Key Methods:**
- `fact_check(content, topic)` - Main verification
- `verify_specific_claims(claims, context)` - Claim-by-claim analysis
- `cross_check(research_a, research_b, topic)` - Compare sources

### 3. Writer Agent
**Role:** Content Creation
- Transforms research into polished content
- Multiple writing styles (informative, technical, conversational, etc.)
- Various formats (articles, summaries, comparisons)
- Maintains accuracy while engaging readers

**Key Methods:**
- `write_article(topic, research, fact_check, style, length)` - Full articles
- `write_summary(topic, research, max_paragraphs)` - Summaries
- `write_comparison(topic, perspectives, cross_check)` - Comparative analysis
- `refine_content(content, feedback, focus_areas)` - Refinement

## Workflow Types

### Simple Workflow
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Researcher  │────▶│ Fact-Checker │────▶│    Writer    │
│   Research   │     │    Verify    │     │    Write     │
└──────────────┘     └──────────────┘     └──────────────┘
     Topic              Findings             Article
```

### Iterative Workflow
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Researcher  │────▶│ Fact-Checker │────▶│  Researcher  │
│   Initial    │     │   Review 1   │     │   Refined    │
└──────────────┘     └──────────────┘     └──────────────┘
                                                  │
                                                  ▼
                            ┌──────────────┐     ┌──────────────┐
                            │    Writer    │◀────│ Fact-Checker │
                            │    Write     │     │  Final Check │
                            └──────────────┘     └──────────────┘
```

### Comparative Workflow
```
      Topic
        │
    ┌───┴────┬────────┐
    ▼        ▼        ▼
┌────────┐ ┌────────┐ ┌────────┐
│Research│ │Research│ │Research│
│Persp. 1│ │Persp. 2│ │Persp. 3│
└────────┘ └────────┘ └────────┘
    │        │        │
    └────────┼────────┘
             ▼
      ┌─────────────┐
      │Fact-Checker │
      │Cross-Check  │
      └─────────────┘
             │
             ▼
      ┌─────────────┐
      │   Writer    │
      │  Compare    │
      └─────────────┘
```

## Data Flow

### Input
```python
{
    "topic": "Research topic",
    "context": "Additional context",
    "style": "Writing style",
    "length": "Content length"
}
```

### Agent Communication
Agents communicate via structured dictionaries:

```python
# Researcher Output
{
    "agent": "Researcher",
    "topic": "...",
    "findings": "...",
    "needs_fact_checking": True
}

# Fact-Checker Output
{
    "agent": "FactChecker",
    "topic": "...",
    "fact_check_report": "...",
    "status": "reviewed"
}

# Writer Output
{
    "agent": "Writer",
    "topic": "...",
    "content_type": "article",
    "content": "..."
}
```

### Final Output
```python
{
    "workflow_type": "simple|iterative|comparative",
    "topic": "...",
    "research": {...},
    "fact_check": {...},
    "article": {...},
    "workflow_history": [
        {
            "timestamp": "ISO format",
            "step": "step_name",
            "agent": "agent_name",
            "data": {...}
        }
    ]
}
```

## Technology Stack

- **LangChain**: Core framework for agent orchestration
- **LangChain-OpenAI**: OpenAI integration
- **uv**: Fast Python package management
- **python-dotenv**: Environment configuration

## Extension Points

### Adding New Agents
1. Create new agent class in `src/agents/`
2. Implement standard interface (input/output dictionaries)
3. Add to orchestrator initialization
4. Create new workflow methods

### Custom Workflows
1. Extend `MultiAgentOrchestrator` class
2. Define agent interaction sequence
3. Add logging steps
4. Return structured results

### Tool Integration
Future: Add custom tools in `src/tools/` for:
- Web search
- Database queries
- API integrations
- Document parsing

## Best Practices

1. **Agent Independence**: Each agent should work independently
2. **Structured Communication**: Use dictionaries for agent I/O
3. **Logging**: Track all workflow steps for debugging
4. **Error Handling**: Graceful fallbacks for API failures
5. **Temperature Tuning**: Lower for fact-checking, higher for creativity
6. **Workflow History**: Maintain complete audit trail

## Performance Considerations

- **Token Usage**: Monitor cumulative token consumption
- **Parallel Processing**: Future enhancement for multi-perspective research
- **Caching**: Consider caching common research results
- **Async Operations**: Potential for async agent calls

---

For implementation details, see the source code in `src/` directory.
