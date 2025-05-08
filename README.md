# LangChain Training 🦜🔗 Revised Fork

This repository is a revised fork of the original LangChain course created by **Harrish Neel**. The original course provides a comprehensive introduction to LangChain, covering various integrations, models, and workflows for building applications with language models. 

In this revised fork, I have focused on **leveraging the content with Ollama and Gemma models**, enhancing the examples and workflows to demonstrate their capabilities in various scenarios.

---

## Repository Structure

The repository is organized into the following directories:

### 1. `1_chat_models/`
This directory contains examples of using different chat models, including OpenAI, Anthropic, Google Gemini, and Ollama. Key files include:
- **`1_chat_models_starter.py`**: Basic example of using OpenAI's GPT-4 model.
- **`2_chat_models_ollama.py`**: Demonstrates the use of Ollama's `gemma3:12b-it-qat` model.
- **`5_chat_ollama_firebase_history.py`**: Integrates Ollama with Firebase Firestore to save and retrieve chat message history.

### 2. `2_prompt_templates/`
This directory focuses on creating and using prompt templates for various tasks. Examples include templates for Gemini and other models.

### 3. `3_chains/`
This directory explores LangChain's chain functionality, including:
- **`3_chains_gemini.py`**: Demonstrates chaining prompts with the Google Gemini model.
- **`4_chains_parallel.py`**: Shows how to run multiple chains in parallel using Ollama.

### 4. `4_RAGs/`
This directory focuses on Retrieval-Augmented Generation (RAG) workflows:
- **`1a_basic_rag_ollama.py`**: Demonstrates creating a vector store and using Ollama for RAG.
- **`2a_rag_basics_metadata.py`**: Explores metadata handling in RAG workflows.

### 5. `5_agents/`
This directory contains examples of using LangChain agents for dynamic task execution.

---

## Key Features in This Fork

1. **Integration with Ollama Models**:
   - Added examples showcasing the use of Ollama's `gemma3:12b-it-qat` model for various tasks.
   - Demonstrated how to save and retrieve chat history using Firebase Firestore with Ollama.

2. **Google Gemini Integration**:
   - Enhanced examples to include the use of Google Gemini models for tasks like fact generation and RAG workflows.

3. **Focus on Practical Applications**:
   - Improved workflows for real-world use cases, such as saving chat history, parallel processing, and metadata handling.

---

## Getting Started

### Prerequisites
- Python 3.12 or later
- Install required dependencies:
  ```bash
  pip install -r requirements.txt

## Acknowledgments
This repository is based on the original LangChain course created by Harrish Neel. The revised fork builds upon the foundation laid by Harrish to explore advanced integrations with Ollama and Google Gemini models.
