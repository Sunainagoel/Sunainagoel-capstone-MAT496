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

## Project Structure:

![Graph](https://github.com/Sunainagoel/Sunainagoel-capstone-MAT496/blob/main/media/CareerGapAnalyzer_worflow.png)

## A sample run of the project using the CLI Interface:

```commandline
========================================
   CAREER GAP ANALYZER AGENT
========================================
Select an input mode:
1. Run with Sample Data (Python Dev Scenario)
2. Run with Sample Data (Data Science Scenario)
3. Enter Custom Text (Interactive)

Enter choice (1-3): 3

--- Custom Input Mode ---

[1/2] PASTE THE JOB DESCRIPTION BELOW:

(Enter your text. Press Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) on a new line to finish, or just press Enter twice quickly)
Senior Frontend Engineer at TechCorp.
We are looking for a developer with 5+ years of experience in building scalable web applications.
Core requirements:
- Deep expertise in React.js and modern hooks.
- Must use TypeScript for all new development (Strict typing).
- Experience with GraphQL (Apollo Client) is mandatory.
- Knowledge of Docker and CI/CD pipelines (GitHub Actions).
- Strong communication skills and ability to lead code reviews.


[2/2] PASTE THE RESUME BELOW:

(Enter your text. Press Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) on a new line to finish, or just press Enter twice quickly)
Alex Taylor - Web Developer
I have 6 years of experience building web apps for e-commerce.
Skills:
- JavaScript (ES6+), HTML, CSS.
- React.js (Redux, Context API).
- Experience building and consuming RESTful APIs.
- Familiar with Git and Agile methodologies.
- I have managed small teams and deployed apps to Netlify.


----------------------------------------
Starting Agent execution...
----------------------------------------
--- NODE: Analyzing Job Description ---
--- NODE: Analyzing Resume ---
--- NODE: Identifying Gaps ---
--- NODE: Researching Learning Resources (Tool Calling) ---
   Searching resources for: TypeScript
   Searching resources for: GraphQL
   Searching resources for: Apollo Client
--- NODE: Generating Report ---

==============================
FINAL REPORT
==============================

# Career Development Report

## Gap Analysis Summary

Based on the recent gap analysis, it has been identified that there are several key areas for improvement in both technical and soft skills. The current match percentage stands at 50%, indicating a significant opportunity for growth and development. Below are the specific skills that have been identified as areas for improvement:

### Missing Technical Skills
- **TypeScript**
- **GraphQL**
- **Apollo Client**
- **Docker**
- **CI/CD**
- **GitHub Actions**

### Missing Soft Skills
- **Strong communication skills**
- **Ability to lead code reviews**

## Learning Plan

To address these gaps, a comprehensive learning plan has been developed. This plan includes a variety of resources tailored to help you acquire the necessary skills effectively. Here are some recommended resources:

### TypeScript
- **TutorialsTeacher’s Learn TypeScript**: A comprehensive online tutorial that provides a step-by-step learning path for mastering TypeScript. [Learn More](https://medium.com/@theevergrowingdev/%EF%B8%8F-11-free-resources-to-learn-typescript-88531580f0f)
- **Academind’s TypeScript Course for Beginners on YouTube**: A highly popular resource for those new to TypeScript.
- **“TypeScript Deep Dive” by Basarat Ali Syed**: An invaluable free online book that takes learners on an in-depth journey through the intricacies of TypeScript.

### GraphQL
- **Apollo Odyssey**: Apollo's official learning platform offering free hands-on GraphQL tutorials. [Explore Tutorials](https://www.apollographql.com/tutorials/)

### Apollo Client
- **Apollo Client Tutorial**: A short tutorial to get you up and running with Apollo Client. [Get Started](https://www.apollographql.com/docs/react/get-started)

## Conclusion

Embarking on this learning journey is a significant step towards enhancing your professional capabilities and achieving your career goals. By focusing on these key areas, you will not only improve your technical proficiency but also develop essential soft skills that are crucial in today's collaborative work environments.

Remember, every step you take towards learning and development is a step towards a more fulfilling and successful career. Embrace the challenge, stay committed, and celebrate your progress along the way. You have the potential to excel, and with dedication and perseverance, you will undoubtedly reach new heights in your career.

Best of luck on your learning journey! 🎉

---

[Debug] Missing Skills Found: ['TypeScript', 'GraphQL', 'Apollo Client', 'Docker', 'CI/CD', 'GitHub Actions']
```
## How to Run:

### 1. Prerequisites
- Python 3.10+
- OpenAI API Key
- Tavily API Key (Free tier at tavily.com)

### 2. Setup
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Sunainagoel/Sunainagoel-capstone-MAT496.git
    cd Sunainagoel-capstone-MAT496
    ```
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Environment**:
    Create a `.env` file in the root directory:
    ```env
    OPENAI_API_KEY=sk-your-key-here
    TAVILY_API_KEY=tvly-your-key-here
    LANGCHAIN_TRACING_V2=true
    LANGCHAIN_API_KEY=lsv2-your-key-here (optional, for tracing)
    ```

### 3. Usage
Run the CLI application:
```bash
python src/main.py
```
