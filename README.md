## Title: CareerGap Agent: Resume vs. Job Description Analyzer

## Overview

My project is an AI-powered Career Gap Analyzer. It takes a user's Resume and a target Job Description (JD) as input. Instead of just giving a generic similarity score, it builds a structured knowledge graph of the user's skills versus the job requirements. It identifies specific "Skill Gaps" and then autonomously uses a search tool to find the best, up-to-date learning resources (tutorials/documentation) to fill those gaps.

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

- [ ] **Step 2: Analysis Nodes:** Built the analyze_job_node and analyze_resume_node to extract entities from text. Built the compare_gaps_node to logically derive missing skills.

- [ ] **Step 3: Tool Integration:** Integrated TavilySearchResults. Built the research_resources_node which iterates over the missing skills list and calls the tool for each one.

- [ ] **Step 4: Graph Construction:** Wired the nodes into a StateGraph. Configured LangSmith tracing for debugging. Added the final report_node to format the output.

## Conclusion:

I had planned to achieve an agent that can turn a stressful job application process into an actionable learning plan. I think I have successfully achieved this. The agent effectively identifies that a user is missing a specific skill (e.g., "LangGraph") and immediately provides a URL to learn it. This demonstrates the power of combining logical processing (LangGraph) with external knowledge retrieval (Tools).
