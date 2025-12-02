"""
Researcher Agent - Responsible for gathering information on topics
"""
import os
from typing import List, Dict, Any, Optional
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


class ResearcherAgent:
    """
    An agent that researches topics and gathers comprehensive information.
    Uses LLM to simulate web research and knowledge gathering.
    Supports both OpenAI and DeepSeek APIs.
    """

    def __init__(
        self,
        model_name: str = "deepseek-chat",
        temperature: float = 0.7,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None
    ):
        # Default to DeepSeek if base_url not specified
        if base_url is None:
            base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")

        # Use DeepSeek API key if available, otherwise fall back to OpenAI
        if api_key is None:
            api_key = os.getenv("DEEPSEEK_API_KEY") or os.getenv("OPENAI_API_KEY")

        self.llm = ChatOpenAI(
            model=model_name,
            temperature=temperature,
            api_key=api_key,
            base_url=base_url
        )
        self.name = "Researcher"

        self.system_prompt = """You are an expert researcher with deep knowledge across multiple domains.
Your job is to provide comprehensive, well-structured research on any given topic.

When researching a topic:
1. Break down the topic into key subtopics
2. Provide factual information from multiple perspectives
3. Include relevant statistics, examples, and case studies
4. Cite potential sources (even if simulated)
5. Identify areas that need fact-checking

Format your research as a structured report with clear sections."""

    def research(self, topic: str, context: str = "") -> Dict[str, Any]:
        """
        Conduct research on a given topic.

        Args:
            topic: The topic to research
            context: Additional context or specific aspects to focus on

        Returns:
            Dictionary containing research findings
        """
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", "Research the following topic: {topic}\n\nAdditional context: {context}\n\nProvide a comprehensive research report.")
        ])

        chain = prompt | self.llm

        response = chain.invoke({
            "topic": topic,
            "context": context or "General overview needed"
        })

        return {
            "agent": self.name,
            "topic": topic,
            "findings": response.content,
            "needs_fact_checking": True
        }

    def focused_research(self, topic: str, specific_questions: List[str]) -> Dict[str, Any]:
        """
        Conduct focused research answering specific questions.

        Args:
            topic: The main topic
            specific_questions: List of specific questions to answer

        Returns:
            Dictionary containing targeted research
        """
        questions_text = "\n".join([f"{i+1}. {q}" for i, q in enumerate(specific_questions)])

        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", """Research the topic: {topic}

Answer these specific questions:
{questions}

Provide detailed, evidence-based answers to each question.""")
        ])

        chain = prompt | self.llm

        response = chain.invoke({
            "topic": topic,
            "questions": questions_text
        })

        return {
            "agent": self.name,
            "topic": topic,
            "questions": specific_questions,
            "findings": response.content,
            "needs_fact_checking": True
        }
