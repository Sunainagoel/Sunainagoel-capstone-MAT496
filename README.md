## Title: CareerGap Agent: Resume vs. Job Description Analyzer

## Overview

My capstone project, the CareerGap Analyzer, acts as an intelligent career coach. Unlike simple keyword matchers, this agent uses a multi-step AI workflow to deeply analyze the semantics of both a Resume and a Job Description. It doesn't just tell you that you aren't a match; it explains why and, more importantly, how to fix it. By leveraging a directed graph architecture (LangGraph), the agent identifies specific technical and soft skill gaps and immediately searches the live web to provide high-quality, free learning resources. It transforms a passive rejection into an active, actionable learning plan.

## Reason for picking up this project

This project perfectly aligns with the advanced topics of the MAT496 course:

1. **LangGraph:** I implemented a StateGraph architecture to orchestrate the workflow. The agent maintains a persistent state (AgentState) as it moves through extraction, analysis, and research nodes.

2. **Retrieval Augmented Generation (RAG):** I implemented Agentic RAG. Instead of relying on a static, outdated vector store, my agent dynamically retrieves live context from the web using semantic search to augment the final report.

3. **Structured Output:** I used Pydantic models to force the LLM to output strict JSON schemas (SkillAnalysis, GapAnalysis), ensuring the agent doesn't just generate text but processes data.

4. **Tool Calling:** The agent autonomously calls the Tavily Search API to find learning resources. It dynamically generates search queries based on the specific gaps identified in the analysis phase.

5. **LangSmith:** I utilized LangSmith for debugging and tracing. Since this is a multi-step agent, LangSmith allowed me to visualize the inputs/outputs of every node and optimize the system prompts.

## Video Summary Link: 

Make a short -  3-5 min video of yourself, put it on youtube/googledrive, and put its link in your README.md.

- you can use this free tool for recording https://screenrec.com/
- Video format should be like this:
- your face should be visible
- State the overall job of your agent: what inputs it takes, and what output it gives.
- Very quickly, explain how your agent acts on the input and spits out the output. 
- show an example run of the agent in the video

## Plan

I plan to execute these steps to complete my project.

- [X] **Step 1: Environment & Schema Setup:** Set up langgraph and langchain. Defined Pydantic models (SkillAnalysis, GapAnalysis) to handle Structured Output.

- [X] **Step 2: Analysis Nodes:** Built the analyze_job_node and analyze_resume_node to extract entities from text. Built the compare_gaps_node to logically derive missing skills.

- [X] **Step 3: Tool Integration:** Integrated TavilySearchResults. Built the research_resources_node which iterates over the missing skills list and calls the tool for each one.

- [X] **Step 4: Graph Construction:** Wired the nodes into a StateGraph. Configured LangSmith tracing for debugging. Added the final report_node to format the output.

- [X] **Step 5: User Interface & Entry Point:** Built the main.py CLI interface to allow users to select between sample scenarios or custom input. Implemented data.py to store robust test cases for demonstration.

## Conclusion:

I had planned to achieve an agent that can turn a stressful job application process into an actionable learning plan. I believe I have successfully achieved this. The agent autonomously decides that a skill is missing and then spins up a search tool to find a solution. It proves that we can outsource not just "writing" tasks to LLMs, but complex analytical workflows. This tool demonstrates how LangGraph and Agentic RAG can create personalized educational pathways from static data, bridging the gap between where a candidate is and where they need to be. My goal of moving beyond simple "chatbot" interactions and to build something that felt like a true agent—software that can reason, plan, and take action—was successfully achieved.
