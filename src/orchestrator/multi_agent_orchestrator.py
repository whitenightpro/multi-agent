"""
Multi-Agent Orchestrator - Coordinates the research, fact-checking, and writing workflow
"""
from typing import Dict, Any, List, Optional
from enum import Enum
import json
from datetime import datetime

from src.agents.researcher import ResearcherAgent
from src.agents.fact_checker import FactCheckerAgent
from src.agents.writer import WriterAgent


class WorkflowType(Enum):
    """Different workflow types supported by the orchestrator"""
    SIMPLE = "simple"  # Research -> Fact-Check -> Write
    ITERATIVE = "iterative"  # Research -> Fact-Check -> Research (refined) -> Write
    COMPARATIVE = "comparative"  # Multiple research perspectives -> Cross-check -> Compare


class MultiAgentOrchestrator:
    """
    Orchestrates multiple agents to complete complex research and content creation tasks.
    Supports both OpenAI and DeepSeek APIs.
    """

    def __init__(
        self,
        model_name: str = "deepseek-chat",
        api_key: Optional[str] = None,
        base_url: Optional[str] = None
    ):
        self.researcher = ResearcherAgent(
            model_name=model_name,
            api_key=api_key,
            base_url=base_url
        )
        self.fact_checker = FactCheckerAgent(
            model_name=model_name,
            api_key=api_key,
            base_url=base_url
        )
        self.writer = WriterAgent(
            model_name=model_name,
            api_key=api_key,
            base_url=base_url
        )

        self.workflow_history = []

    def log_step(self, step_name: str, agent: str, data: Any):
        """Log workflow step for debugging and transparency"""
        self.workflow_history.append({
            "timestamp": datetime.now().isoformat(),
            "step": step_name,
            "agent": agent,
            "data": data
        })

    def simple_workflow(
        self,
        topic: str,
        context: str = "",
        writing_style: str = "informative",
        content_length: str = "medium"
    ) -> Dict[str, Any]:
        """
        Execute a simple linear workflow: Research -> Fact-Check -> Write

        Args:
            topic: The topic to research and write about
            context: Additional context for research
            writing_style: Style for the final article
            content_length: Target length of the content

        Returns:
            Dictionary containing all workflow outputs
        """
        print(f"\n{'='*60}")
        print(f"Starting Simple Workflow for: {topic}")
        print(f"{'='*60}\n")

        # Step 1: Research
        print("[1/3] 🔍 Researcher Agent: Gathering information...")
        research_result = self.researcher.research(topic, context)
        self.log_step("research", self.researcher.name, research_result)
        print("✓ Research completed\n")

        # Step 2: Fact-Check
        print("[2/3] ✅ Fact-Checker Agent: Verifying findings...")
        fact_check_result = self.fact_checker.fact_check(
            research_result["findings"],
            topic
        )
        self.log_step("fact_check", self.fact_checker.name, fact_check_result)
        print("✓ Fact-checking completed\n")

        # Step 3: Write
        print("[3/3] ✍️  Writer Agent: Creating content...")
        article_result = self.writer.write_article(
            topic,
            research_result["findings"],
            fact_check_result["fact_check_report"],
            style=writing_style,
            target_length=content_length
        )
        self.log_step("write", self.writer.name, article_result)
        print("✓ Writing completed\n")

        print(f"{'='*60}")
        print("Workflow Complete!")
        print(f"{'='*60}\n")

        return {
            "workflow_type": "simple",
            "topic": topic,
            "research": research_result,
            "fact_check": fact_check_result,
            "article": article_result,
            "workflow_history": self.workflow_history
        }

    def iterative_workflow(
        self,
        topic: str,
        initial_context: str = "",
        writing_style: str = "informative",
        content_length: str = "medium"
    ) -> Dict[str, Any]:
        """
        Execute an iterative workflow with refinement based on fact-checking.

        Args:
            topic: The topic to research and write about
            initial_context: Initial context for research
            writing_style: Style for the final article
            content_length: Target length of the content

        Returns:
            Dictionary containing all workflow outputs
        """
        print(f"\n{'='*60}")
        print(f"Starting Iterative Workflow for: {topic}")
        print(f"{'='*60}\n")

        # Step 1: Initial Research
        print("[1/5] 🔍 Researcher Agent: Initial research...")
        initial_research = self.researcher.research(topic, initial_context)
        self.log_step("initial_research", self.researcher.name, initial_research)
        print("✓ Initial research completed\n")

        # Step 2: Fact-Check
        print("[2/5] ✅ Fact-Checker Agent: Reviewing findings...")
        fact_check_result = self.fact_checker.fact_check(
            initial_research["findings"],
            topic
        )
        self.log_step("fact_check", self.fact_checker.name, fact_check_result)
        print("✓ Fact-checking completed\n")

        # Step 3: Refined Research (based on fact-check feedback)
        print("[3/5] 🔍 Researcher Agent: Refined research based on feedback...")
        refined_context = f"Previous research was fact-checked. Address these points:\n{fact_check_result['fact_check_report']}"
        refined_research = self.researcher.research(topic, refined_context)
        self.log_step("refined_research", self.researcher.name, refined_research)
        print("✓ Refined research completed\n")

        # Step 4: Second Fact-Check
        print("[4/5] ✅ Fact-Checker Agent: Final verification...")
        final_fact_check = self.fact_checker.fact_check(
            refined_research["findings"],
            topic
        )
        self.log_step("final_fact_check", self.fact_checker.name, final_fact_check)
        print("✓ Final fact-checking completed\n")

        # Step 5: Write
        print("[5/5] ✍️  Writer Agent: Creating final content...")
        article_result = self.writer.write_article(
            topic,
            refined_research["findings"],
            final_fact_check["fact_check_report"],
            style=writing_style,
            target_length=content_length
        )
        self.log_step("write", self.writer.name, article_result)
        print("✓ Writing completed\n")

        print(f"{'='*60}")
        print("Iterative Workflow Complete!")
        print(f"{'='*60}\n")

        return {
            "workflow_type": "iterative",
            "topic": topic,
            "initial_research": initial_research,
            "initial_fact_check": fact_check_result,
            "refined_research": refined_research,
            "final_fact_check": final_fact_check,
            "article": article_result,
            "workflow_history": self.workflow_history
        }

    def comparative_workflow(
        self,
        topic: str,
        perspectives: List[str],
        writing_style: str = "analytical"
    ) -> Dict[str, Any]:
        """
        Execute a comparative workflow examining multiple perspectives.

        Args:
            topic: The topic to research
            perspectives: List of different perspectives/angles to research
            writing_style: Style for the final comparison piece

        Returns:
            Dictionary containing all workflow outputs
        """
        print(f"\n{'='*60}")
        print(f"Starting Comparative Workflow for: {topic}")
        print(f"Analyzing {len(perspectives)} perspectives")
        print(f"{'='*60}\n")

        # Step 1: Research each perspective
        research_results = {}
        for i, perspective in enumerate(perspectives, 1):
            print(f"[{i}/{len(perspectives)}] 🔍 Researcher Agent: Researching '{perspective}'...")
            result = self.researcher.research(
                topic,
                context=f"Focus on this perspective: {perspective}"
            )
            research_results[perspective] = result["findings"]
            self.log_step(f"research_perspective_{i}", self.researcher.name, result)
            print(f"✓ Research for '{perspective}' completed\n")

        # Step 2: Cross-check the perspectives
        if len(perspectives) >= 2:
            print(f"[*] ✅ Fact-Checker Agent: Cross-checking perspectives...")
            perspectives_list = list(research_results.keys())
            cross_check_result = self.fact_checker.cross_check(
                research_results[perspectives_list[0]],
                research_results[perspectives_list[1]],
                topic
            )
            self.log_step("cross_check", self.fact_checker.name, cross_check_result)
            print("✓ Cross-checking completed\n")
        else:
            cross_check_result = None

        # Step 3: Fact-check each perspective
        print(f"[*] ✅ Fact-Checker Agent: Fact-checking all perspectives...")
        combined_research = "\n\n---\n\n".join([
            f"{perspective}:\n{content}"
            for perspective, content in research_results.items()
        ])
        overall_fact_check = self.fact_checker.fact_check(combined_research, topic)
        self.log_step("overall_fact_check", self.fact_checker.name, overall_fact_check)
        print("✓ Fact-checking completed\n")

        # Step 4: Write comparative analysis
        print(f"[*] ✍️  Writer Agent: Creating comparative analysis...")
        comparison_result = self.writer.write_comparison(
            topic,
            research_results,
            cross_check_result["cross_check_report"] if cross_check_result else None
        )
        self.log_step("write_comparison", self.writer.name, comparison_result)
        print("✓ Comparative analysis completed\n")

        print(f"{'='*60}")
        print("Comparative Workflow Complete!")
        print(f"{'='*60}\n")

        return {
            "workflow_type": "comparative",
            "topic": topic,
            "perspectives": perspectives,
            "research_results": research_results,
            "cross_check": cross_check_result,
            "overall_fact_check": overall_fact_check,
            "comparison": comparison_result,
            "workflow_history": self.workflow_history
        }

    def get_summary(self, workflow_result: Dict[str, Any]) -> str:
        """
        Generate a summary from workflow results.

        Args:
            workflow_result: Results from any workflow

        Returns:
            Summary string
        """
        print("\n📝 Generating summary...\n")

        if "article" in workflow_result:
            content = workflow_result["article"]["content"]
        elif "comparison" in workflow_result:
            content = workflow_result["comparison"]["content"]
        else:
            content = str(workflow_result)

        summary_result = self.writer.write_summary(
            workflow_result["topic"],
            content,
            max_paragraphs=3
        )

        return summary_result["content"]

    def save_workflow_results(self, workflow_result: Dict[str, Any], filename: str):
        """
        Save workflow results to a JSON file.

        Args:
            workflow_result: Results from any workflow
            filename: Output filename
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(workflow_result, f, indent=2, ensure_ascii=False)
        print(f"✓ Results saved to {filename}")
