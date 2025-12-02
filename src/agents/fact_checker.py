"""
Fact-Checker Agent - Responsible for verifying claims and ensuring accuracy
"""
import os
from typing import Dict, Any, List, Optional
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


class FactCheckerAgent:
    """
    An agent that fact-checks research findings and identifies potential inaccuracies.
    Acts as a critical reviewer to ensure information quality.
    Supports both OpenAI and DeepSeek APIs.
    """

    def __init__(
        self,
        model_name: str = "deepseek-chat",
        temperature: float = 0.3,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None
    ):
        # Lower temperature for more consistent, careful fact-checking
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
        self.name = "FactChecker"

        self.system_prompt = """You are a meticulous fact-checker and critical thinker.
Your job is to review research findings and identify:
1. Claims that need verification
2. Potential inaccuracies or misleading statements
3. Missing citations or sources
4. Logical inconsistencies
5. Biases or one-sided perspectives

Be thorough but fair. Rate the overall accuracy and provide specific feedback.

Rating scale:
- HIGH: Well-researched, accurate, balanced
- MEDIUM: Generally accurate but has some gaps or minor issues
- LOW: Contains significant inaccuracies or misleading information
- UNVERIFIABLE: Claims cannot be verified or lack sufficient evidence"""

    def fact_check(self, research_content: str, topic: str) -> Dict[str, Any]:
        """
        Fact-check research content.

        Args:
            research_content: The research content to verify
            topic: The topic being researched

        Returns:
            Dictionary containing fact-check results
        """
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", """Topic: {topic}

Research Content to Fact-Check:
{content}

Provide a detailed fact-check report including:
1. Overall accuracy rating
2. Specific claims that need verification
3. Identified issues or concerns
4. Recommendations for improvement
5. Claims that are accurate and well-supported""")
        ])

        chain = prompt | self.llm

        response = chain.invoke({
            "topic": topic,
            "content": research_content
        })

        return {
            "agent": self.name,
            "topic": topic,
            "fact_check_report": response.content,
            "status": "reviewed"
        }

    def verify_specific_claims(self, claims: List[str], context: str = "") -> Dict[str, Any]:
        """
        Verify specific claims with detailed analysis.

        Args:
            claims: List of specific claims to verify
            context: Additional context for verification

        Returns:
            Dictionary containing verification results for each claim
        """
        claims_text = "\n".join([f"{i+1}. {claim}" for i, claim in enumerate(claims)])

        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", """Verify the following claims:

{claims}

Context: {context}

For each claim, provide:
- Verification status (VERIFIED/PARTIALLY_VERIFIED/UNVERIFIED/FALSE)
- Reasoning
- Potential sources that would support or refute the claim
- Any caveats or nuances""")
        ])

        chain = prompt | self.llm

        response = chain.invoke({
            "claims": claims_text,
            "context": context or "General verification"
        })

        return {
            "agent": self.name,
            "claims_analyzed": claims,
            "verification_report": response.content
        }

    def cross_check(self, research_a: str, research_b: str, topic: str) -> Dict[str, Any]:
        """
        Cross-check two pieces of research for consistency.

        Args:
            research_a: First research content
            research_b: Second research content
            topic: The topic being researched

        Returns:
            Dictionary containing cross-check analysis
        """
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", """Topic: {topic}

Research Source A:
{research_a}

Research Source B:
{research_b}

Cross-check these two research sources and identify:
1. Points of agreement
2. Contradictions or inconsistencies
3. Complementary information
4. Which source appears more reliable and why
5. Recommendations for reconciling differences""")
        ])

        chain = prompt | self.llm

        response = chain.invoke({
            "topic": topic,
            "research_a": research_a,
            "research_b": research_b
        })

        return {
            "agent": self.name,
            "topic": topic,
            "cross_check_report": response.content
        }
