# Django Chatbot Terminal Client

This project provides a minimal Django scaffold plus a terminal chatbot command powered by ChatterBot.

## What is included

- Django project configuration
- A `chatbot` Django app
- A custom management command for an interactive terminal chat session
- A small built-in training set for the bot

## Setup

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```


### 3. Run Django setup

Create the SQLite database and apply Django migrations:

```bash
python manage.py migrate
```

### 4. Start the chatbot

```bash
python manage.py chatbot
```

Or run the helper script from the project root:

```bash
bash run_chatbot.sh
```

### 5. Start the web UI

Run the browser-based interface with:

```bash
bash run_webui.sh
```

Then open `http://127.0.0.1:8000/` in your browser.

Discloser Some portions of this project were created with help from GitHub Copilot (AI-assisted code suggestions).


