"""
Writer Agent - Responsible for creating polished content from research
"""
import os
from typing import Dict, Any, Optional, List
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


class WriterAgent:
    """
    An agent that transforms research findings into well-written content.
    Can create various content formats based on verified research.
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
        self.name = "Writer"

        self.system_prompt = """You are an expert content writer skilled at transforming research into engaging, clear, and accurate content.

Your writing should be:
1. Clear and accessible to the target audience
2. Well-structured with logical flow
3. Engaging and interesting
4. Factually accurate based on provided research
5. Free of jargon unless necessary (with explanations when used)

You can write in various formats: articles, blog posts, reports, summaries, etc.
Always maintain accuracy while making the content compelling."""

    def write_article(
        self,
        topic: str,
        research_content: str,
        fact_check_report: str,
        style: str = "informative",
        target_length: str = "medium"
    ) -> Dict[str, Any]:
        """
        Write an article based on research and fact-checking.

        Args:
            topic: The topic of the article
            research_content: Verified research content
            fact_check_report: Fact-checker's report
            style: Writing style (informative, conversational, technical, journalistic)
            target_length: Target length (short, medium, long)

        Returns:
            Dictionary containing the written article
        """
        length_guidance = {
            "short": "500-800 words, focus on key points",
            "medium": "1000-1500 words, comprehensive coverage",
            "long": "2000+ words, in-depth analysis"
        }

        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", """Write a {style} article on the topic: {topic}

Research Content:
{research}

Fact-Check Report:
{fact_check}

Target Length: {length}

Instructions:
- Use the research as your source material
- Address any concerns raised in the fact-check report
- Write in a {style} style
- Include a compelling introduction and conclusion
- Use headings and subheadings for organization
- Only include verified information""")
        ])

        chain = prompt | self.llm

        response = chain.invoke({
            "topic": topic,
            "research": research_content,
            "fact_check": fact_check_report,
            "style": style,
            "length": length_guidance.get(target_length, length_guidance["medium"])
        })

        return {
            "agent": self.name,
            "topic": topic,
            "style": style,
            "content_type": "article",
            "content": response.content
        }

    def write_summary(
        self,
        topic: str,
        research_content: str,
        max_paragraphs: int = 3
    ) -> Dict[str, Any]:
        """
        Write a concise summary of research findings.

        Args:
            topic: The topic being summarized
            research_content: Research content to summarize
            max_paragraphs: Maximum number of paragraphs

        Returns:
            Dictionary containing the summary
        """
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", """Create a concise summary of the following research on: {topic}

Research Content:
{research}

Write a clear, accurate summary in {paragraphs} paragraphs or less.
Capture the most important points and key takeaways.""")
        ])

        chain = prompt | self.llm

        response = chain.invoke({
            "topic": topic,
            "research": research_content,
            "paragraphs": max_paragraphs
        })

        return {
            "agent": self.name,
            "topic": topic,
            "content_type": "summary",
            "content": response.content
        }

    def write_comparison(
        self,
        topic: str,
        perspectives: Dict[str, str],
        cross_check_report: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Write a comparison piece analyzing different perspectives.

        Args:
            topic: The topic being compared
            perspectives: Dictionary of different perspectives/sources
            cross_check_report: Optional cross-check analysis

        Returns:
            Dictionary containing the comparison content
        """
        perspectives_text = "\n\n".join([
            f"Perspective {i+1} ({name}):\n{content}"
            for i, (name, content) in enumerate(perspectives.items())
        ])

        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", """Write a comparison analysis on: {topic}

Different Perspectives:
{perspectives}

{cross_check}

Create a balanced comparison that:
1. Presents each perspective fairly
2. Identifies key differences and similarities
3. Analyzes the strengths and weaknesses of each view
4. Provides an objective synthesis""")
        ])

        chain = prompt | self.llm

        response = chain.invoke({
            "topic": topic,
            "perspectives": perspectives_text,
            "cross_check": f"\nCross-Check Analysis:\n{cross_check_report}" if cross_check_report else ""
        })

        return {
            "agent": self.name,
            "topic": topic,
            "content_type": "comparison",
            "content": response.content
        }

    def refine_content(
        self,
        original_content: str,
        feedback: str,
        focus_areas: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Refine existing content based on feedback.

        Args:
            original_content: The content to refine
            feedback: Specific feedback to address
            focus_areas: Optional list of areas to focus on during refinement

        Returns:
            Dictionary containing refined content
        """
        focus_text = "\n".join([f"- {area}" for area in (focus_areas or [])])

        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", """Refine the following content based on the feedback provided.

Original Content:
{content}

Feedback:
{feedback}

{focus}

Provide an improved version that addresses all feedback while maintaining the core message and accuracy.""")
        ])

        chain = prompt | self.llm

        response = chain.invoke({
            "content": original_content,
            "feedback": feedback,
            "focus": f"Focus particularly on:\n{focus_text}" if focus_areas else ""
        })

        return {
            "agent": self.name,
            "content_type": "refined_content",
            "content": response.content
        }
