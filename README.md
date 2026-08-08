# Healthcare Smart Assistant

A simple AI-powered healthcare chatbot built as a learning project to gain hands-on experience with **Python, LLMs, LangChain, FastAPI, and frontend-backend communication**.

> **Note:** This is a learning project and is not intended to provide professional medical advice, diagnosis, or treatment.

---

## Description

This project started as a basic command-line chatbot and was later converted into a simple web-based Healthcare Smart Assistant.

The main purpose of building this project was to gain practical experience with the basic components involved in developing an LLM-powered application.

Through this project, I explored how to:

- Integrate an LLM into a Python application
- Work with LangChain and message history
- Create APIs using FastAPI
- Connect a JavaScript frontend with a Python backend
- Use system prompts to control model behavior
- Control response creativity using temperature
- Limit response length using max tokens
- Manage environment variables securely

This project is intentionally kept simple as a **learning project**, rather than being a production-ready healthcare application.

---

## Screenshots

### Initial CLI Version → Web Version

<div align="center">
  <img
    width="400"
    alt="Initial CLI Chatbot"
    src="https://github.com/user-attachments/assets/527e0cbb-e936-4fb6-b122-3c61e373271a"
  />
  <img
    width="400"
    alt="Healthcare Smart Assistant"
    src="https://github.com/user-attachments/assets/17efbcd8-7d5d-46cd-89b3-31aa5bc6b9a0"
  />
</div>

The project initially started as a simple CLI chatbot and was later converted into a web-based Healthcare Smart Assistant.

---

## Tech Stack

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- Python
- FastAPI
- Uvicorn

### LLM Framework

- LangChain

### Model Provider

- Mistral AI

### Configuration

- python-dotenv

---

## LLM & Model

The application uses the **Mistral Small** model through LangChain.

The model is configured as:

```python
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.3,
    max_tokens=250
)
