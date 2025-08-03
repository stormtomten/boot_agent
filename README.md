# Boot_agent

An AI Agent built alongside [Boot.dev](https://boot.dev)'s [Build an AI Agent in Python](https://boot.dev/courses/build-an-ai-agent-in-python)

- Uses [uv](https://github.com/astral-sh/uv) for package management
- Integrates with the Google Gemini API
- Includes an example calculator project from Boot.dev, which serves as the agent's working directory

## Agent Capabilities

- Intended to work in a set working directory and its subdirectories (attempts to access outside should result in an error)
- Browsing the working directory
- Read and (over)write files
- Run Python code

> **Note:** While the agent is designed to restrict file operations to the working directory it should not be taken for granted that it can't access files and operations outside of it. Use with caution.

## Example Project

This repository includes a calculator example project from Boot.dev for demonstration and testing purposes.  
The calculator project serves as the default working directory for the AI agent.
