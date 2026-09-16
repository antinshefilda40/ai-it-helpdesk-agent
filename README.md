# AI IT Helpdesk Agent

An educational Agentic AI helpdesk project built for the TNSDC–IBM Agentic AI project submission.

## Problem Statement

IT support teams receive repetitive questions about Wi-Fi, passwords, software, printers, email, and basic system issues. This project demonstrates an AI helpdesk agent that retrieves relevant support knowledge, selects a troubleshooting tool when appropriate, and produces a clear step-by-step response.

## Objectives

- Provide instant answers to common IT support questions.
- Use Retrieval-Augmented Generation (RAG) over a local knowledge base.
- Demonstrate agent-style routing between knowledge retrieval and tools.
- Keep responses safe by avoiding destructive system actions.
- Provide a simple browser interface for demonstration.

## Architecture

User  
↓  
Streamlit UI  
↓  
Helpdesk Agent  
↓  
RAG Retriever + Tools  
↓  
Final Response

## Features

1. RAG retrieval from a local IT support knowledge base.
2. Agent routing based on the user's problem.
3. Network, password, printer, and software troubleshooting tools.
4. IT ticket creation simulation.
5. Knowledge-source display.
6. Simple Streamlit web interface.
7. No API key required for the default demo.

## Example Questions

- My Wi-Fi is connected but there is no internet.
- I forgot my password.
- My printer is not printing.
- My laptop is very slow.
- Create a ticket for a recurring VPN problem.

## Run Locally

```bash
git clone https://github.com/antinshefilda40/ai-it-helpdesk-agent.git
cd ai-it-helpdesk-agent
python -m venv .venv
pip install -r requirements.txt
streamlit run app.py
