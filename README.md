# CodeAlpha Python Programming Internship

A collection of four Python projects completed during the **CodeAlpha Python Programming Internship**. Each project targets a different domain—game development, finance, natural language processing, and automation—demonstrating practical Python skills from fundamentals through real-world integrations.

---

## Overview

| Project | File | Purpose | Dependencies |
|---------|------|---------|--------------|
| Hangman Game | [`hangman.py`](hangman.py) | Interactive console word-guessing game | None (stdlib) |
| Stock Portfolio Tracker | [`copy_of_stock_portfolio_tracker.py`](copy_of_stock_portfolio_tracker.py) | Real-time stock tracking with API & visualization | See [`requirements.txt`](requirements.txt) |
| Conversational Chatbot | [`conversational_chatbot.py`](conversational_chatbot.py) | Rule-based chatbot powered by NLP | See [`requirements.txt`](requirements.txt) |
| Task Automation | [`task_automation_with_python_scripts.py`](task_automation_with_python_scripts.py) | Automated file organization by type | None (stdlib) |

---

## Skills Demonstrated

### Core Python
- Functions, loops, conditionals, and dictionaries
- User input handling and input validation
- Modular code structure with reusable functions
- Interactive CLI menus and game loops

### APIs & Data
- REST API integration ([Alpha Vantage](https://www.alphavantage.co/) for stock data)
- JSON parsing and error handling
- Data manipulation with **pandas**
- Financial calculations (portfolio value, profit/loss)

### Data Visualization
- Plotting with **matplotlib** and **seaborn**
- Time-series visualization of stock prices
- Custom charts with labels, grids, and formatting

### Natural Language Processing (NLP)
- Text preprocessing and tokenization with **NLTK**
- Named entity and linguistic analysis with **spaCy**
- Stop-word removal and intent-based response generation
- Dual preprocessing pipelines (NLTK vs spaCy)

### Automation & File Systems
- Directory creation and file traversal with `os`
- File moving and organization with `shutil`
- Extension-based classification and batch processing

---

## Projects in Detail

### 1. Hangman Game

A classic Hangman game played entirely in the terminal. The player guesses letters to reveal a hidden programming-related word before running out of attempts.

**Features**
- Random word selection from a curated word list
- ASCII art hangman stages (7 stages)
- Letter validation and duplicate-guess detection
- Win/loss detection with clear feedback

**Dependencies:** None — uses Python standard library only (`random`).

**Run**
```bash
python hangman.py
```

**Skills:** Game logic, string manipulation, set operations, user interaction, control flow.

---

### 2. Stock Portfolio Tracker

A portfolio management tool that fetches live stock prices and tracks investment performance. Originally built in Google Colab with progressive enhancements—from a basic tracker to a version with pre-loaded holdings and price visualization.

**Features**
- Add, remove, and view stocks in a portfolio
- Real-time price lookup via Alpha Vantage API
- Profit/loss calculation per holding and total portfolio value
- Stock price visualization over time (matplotlib + seaborn)
- Interactive menu-driven interface

**Setup**
1. Install dependencies from the repo root: `pip install -r requirements.txt`
2. Get a free API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
3. Set your key in the script (replace the empty `API_KEY` or use an environment variable).

**Packages used:** `requests`, `pandas`, `matplotlib`, `seaborn` (listed in [`requirements.txt`](requirements.txt)).

**Run**
```bash
python copy_of_stock_portfolio_tracker.py
```

**Skills:** API integration, financial data handling, data visualization, error handling, interactive CLI design.

> **Note:** The script contains Colab-specific cells (`!pip install`). For local use, install dependencies via pip and run the final menu-driven section. Avoid committing API keys to version control.

---

### 3. Conversational Chatbot

A rule-based chatbot that understands user intent through natural language preprocessing. Supports both **NLTK** and **spaCy** pipelines for text tokenization and stop-word filtering.

**Features**
- Greeting, farewell, help, joke, and small-talk responses
- Intent detection via keyword matching on preprocessed tokens
- Configurable preprocessing: `nltk` or `spacy`
- Continuous conversation loop until the user exits

**Setup**
1. Install dependencies from the repo root: `pip install -r requirements.txt`
2. Download the spaCy English model:
   ```bash
   python -m spacy download en_core_web_sm
   ```
3. NLTK data (`punkt`, `stopwords`) is downloaded automatically when you run the script.

**Packages used:** `nltk`, `spacy` (listed in [`requirements.txt`](requirements.txt)).

**Run**
```bash
python conversational_chatbot.py
```

**Skills:** NLP fundamentals, text preprocessing, tokenization, stop-word removal, intent matching, conversational UI.

---

### 4. Task Automation — File Organizer

Automates sorting of files in a folder into categorized subfolders based on file extension (Images, Documents, Videos, Audio, Others).

**Features**
- Auto-creates category folders if missing
- Moves files by extension (`.jpg`, `.pdf`, `.mp4`, etc.)
- Fallback **Others** folder for unrecognized types
- Progress logging for each moved file

**Dependencies:** None — uses Python standard library only (`os`, `shutil`).

**Run**
```bash
python task_automation_with_python_scripts.py
```

**Skills:** Scripting, filesystem operations, batch automation, path handling.

> **Note:** The original script was written for Google Colab with Drive mounting. Update `downloads_folder` to a local path (e.g. `C:/Users/You/Downloads`) before running locally.

---

## Tech Stack

| Category | Tools & Libraries |
|----------|-------------------|
| Language | Python 3 |
| NLP | NLTK, spaCy |
| Data | pandas |
| Visualization | matplotlib, seaborn |
| HTTP / APIs | requests, Alpha Vantage |
| Automation | os, shutil |
| Dependency management | [`requirements.txt`](requirements.txt) |
| Environment | Google Colab (development), local Python (execution) |

---

## Dependencies

All third-party packages are listed in [`requirements.txt`](requirements.txt):

| Package | Used by |
|---------|---------|
| `requests` | Stock Portfolio Tracker |
| `pandas` | Stock Portfolio Tracker |
| `matplotlib` | Stock Portfolio Tracker |
| `seaborn` | Stock Portfolio Tracker |
| `nltk` | Conversational Chatbot |
| `spacy` | Conversational Chatbot |

**Hangman** and **Task Automation** need no external packages — only the Python standard library.

**One-time setup after `pip install`:**
```bash
python -m spacy download en_core_web_sm
```

NLTK corpora (`punkt`, `stopwords`) download automatically when you run the chatbot.

---

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/CodeAlpha_tasks.git
cd CodeAlpha_tasks
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Run a project
```bash
python hangman.py
python copy_of_stock_portfolio_tracker.py
python conversational_chatbot.py
python task_automation_with_python_scripts.py
```

Only install what you need: Hangman and Task Automation run without step 2. Steps 2–3 apply to Stock Tracker and Chatbot.

---

## Repository Structure

```
CodeAlpha_tasks/
├── hangman.py                              # Console Hangman game
├── copy_of_stock_portfolio_tracker.py      # Stock portfolio tracker + charts
├── conversational_chatbot.py               # NLP chatbot (NLTK / spaCy)
├── task_automation_with_python_scripts.py  # File organization automation
├── requirements.txt                        # Python dependencies
└── README.md                               # Project documentation
```

---

## Internship Summary

Through the CodeAlpha Python Programming Internship, these projects covered:

1. **Python fundamentals** — logic, data structures, and interactive programs  
2. **External integrations** — REST APIs and live data fetching  
3. **Data analysis & visualization** — pandas and plotting libraries  
4. **NLP basics** — preprocessing pipelines and conversational agents  
5. **Practical automation** — filesystem scripts for real-world tasks  

Each project was developed and tested in **Google Colab**, then exported as standalone Python scripts for this repository.

---

## Author

**Roman Ahmad Khan**  
CodeAlpha Python Programming Internship

---

## License

This repository is for educational and portfolio purposes. Feel free to explore and learn from the code.
