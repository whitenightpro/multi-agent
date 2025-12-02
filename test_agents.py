"""
Quick test script to verify the multi-agent system is working
"""
import os
from dotenv import load_dotenv

from src.agents.researcher import ResearcherAgent
from src.agents.fact_checker import FactCheckerAgent
from src.agents.writer import WriterAgent


def test_agents():
    """Quick test of individual agents"""
    load_dotenv()

    # Check for API key (DeepSeek preferred, OpenAI as fallback)
    deepseek_key = os.getenv("DEEPSEEK_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")

    if not deepseek_key and not openai_key:
        print("❌ No API key found!")
        print("\nFor DeepSeek (Recommended):")
        print("  export DEEPSEEK_API_KEY='your-key'")
        print("\nOr for OpenAI:")
        print("  export OPENAI_API_KEY='your-key'")
        return False

    # Display which API is being used
    if deepseek_key:
        print("✓ Using DeepSeek API\n")
    else:
        print("✓ Using OpenAI API\n")

    print("Testing Multi-Agent System...\n")

    try:
        # Test Researcher
        print("1. Testing Researcher Agent...")
        researcher = ResearcherAgent()
        research = researcher.research(
            "Python programming",
            "Brief overview only"
        )
        print(f"✓ Researcher working! Generated {len(research['findings'])} characters\n")

        # Test Fact-Checker
        print("2. Testing Fact-Checker Agent...")
        fact_checker = FactCheckerAgent()
        fact_check = fact_checker.fact_check(
            research['findings'][:500],  # Use truncated content for speed
            "Python programming"
        )
        print(f"✓ Fact-Checker working! Generated {len(fact_check['fact_check_report'])} characters\n")

        # Test Writer
        print("3. Testing Writer Agent...")
        writer = WriterAgent()
        summary = writer.write_summary(
            "Python programming",
            research['findings'][:500],
            max_paragraphs=2
        )
        print(f"✓ Writer working! Generated {len(summary['content'])} characters\n")

        print("="*60)
        print("✅ All agents are working correctly!")
        print("="*60)
        print("\nYou can now run: uv run main.py")
        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        return False


if __name__ == "__main__":
    test_agents()
