"""
Multi-Agent Research System - Example Usage
"""
import os
from dotenv import load_dotenv

from src.orchestrator.multi_agent_orchestrator import MultiAgentOrchestrator


def example_simple_workflow():
    """
    Demonstrates the simple linear workflow: Research -> Fact-Check -> Write
    """
    print("\n" + "="*80)
    print("EXAMPLE 1: Simple Workflow")
    print("="*80)

    orchestrator = MultiAgentOrchestrator()

    result = orchestrator.simple_workflow(
        topic="The impact of artificial intelligence on healthcare",
        context="Focus on practical applications and current implementations",
        writing_style="informative",
        content_length="medium"
    )

    print("\n📄 FINAL ARTICLE:")
    print("-" * 80)
    print(result["article"]["content"])
    print("-" * 80)

    # Save results
    orchestrator.save_workflow_results(result, "output_simple_workflow.json")

    return result


def example_iterative_workflow():
    """
    Demonstrates the iterative workflow with refinement based on fact-checking
    """
    print("\n" + "="*80)
    print("EXAMPLE 2: Iterative Workflow")
    print("="*80)

    orchestrator = MultiAgentOrchestrator()

    result = orchestrator.iterative_workflow(
        topic="Quantum computing and its potential applications",
        initial_context="Cover both theoretical foundations and practical uses",
        writing_style="informative",
        content_length="medium"
    )

    print("\n📄 FINAL ARTICLE:")
    print("-" * 80)
    print(result["article"]["content"])
    print("-" * 80)

    # Get a summary
    summary = orchestrator.get_summary(result)
    print("\n📋 SUMMARY:")
    print("-" * 80)
    print(summary)
    print("-" * 80)

    # Save results
    orchestrator.save_workflow_results(result, "output_iterative_workflow.json")

    return result


def example_comparative_workflow():
    """
    Demonstrates the comparative workflow analyzing multiple perspectives
    """
    print("\n" + "="*80)
    print("EXAMPLE 3: Comparative Workflow")
    print("="*80)

    orchestrator = MultiAgentOrchestrator()

    result = orchestrator.comparative_workflow(
        topic="Remote work vs. office work",
        perspectives=[
            "Benefits and challenges from an employee perspective",
            "Impact on company productivity and culture",
            "Environmental and societal implications"
        ],
        writing_style="analytical"
    )

    print("\n📄 COMPARATIVE ANALYSIS:")
    print("-" * 80)
    print(result["comparison"]["content"])
    print("-" * 80)

    # Save results
    orchestrator.save_workflow_results(result, "output_comparative_workflow.json")

    return result


def main():
    """
    Main function to run example workflows
    """
    # Load environment variables (for DeepSeek or OpenAI API key)
    load_dotenv()

    # Check for API key (DeepSeek preferred, OpenAI as fallback)
    deepseek_key = os.getenv("DEEPSEEK_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")

    if not deepseek_key and not openai_key:
        print("⚠️  WARNING: No API key found in environment variables.")
        print("\nFor DeepSeek (Recommended):")
        print("  export DEEPSEEK_API_KEY='your-deepseek-key-here'")
        print("\nOr for OpenAI:")
        print("  export OPENAI_API_KEY='your-openai-key-here'")
        print("\nOr create a .env file with:")
        print("  DEEPSEEK_API_KEY=your-deepseek-key-here")
        return

    # Display which API is being used
    if deepseek_key:
        print("\n✓ Using DeepSeek API")
    else:
        print("\n✓ Using OpenAI API")

    print("\n" + "="*80)
    print("Multi-Agent Research & Content Creation System")
    print("="*80)
    print("\nThis system demonstrates three types of workflows:")
    print("1. Simple: Research → Fact-Check → Write")
    print("2. Iterative: Research → Fact-Check → Refined Research → Write")
    print("3. Comparative: Multiple Research Perspectives → Cross-Check → Comparison")
    print("\n" + "="*80)

    # Uncomment the workflow you want to run:

    # Example 1: Simple workflow
    example_simple_workflow()

    # Example 2: Iterative workflow (uncomment to run)
    # example_iterative_workflow()

    # Example 3: Comparative workflow (uncomment to run)
    # example_comparative_workflow()

    print("\n✅ All examples completed!")
    print("Check the output JSON files for detailed workflow information.")


if __name__ == "__main__":
    main()
