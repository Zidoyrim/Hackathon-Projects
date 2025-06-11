# 🛡️ Cybersecurity Fraud Trends Digest

A daily email digest system that fetches real-time cybersecurity fraud news, summarizes it using a local LLaMA model via Ollama, and delivers it in a clean, readable email format to busy startup founders and product managers.

---

## 🚀 Features

- 🔍 **Live data scraping** from trusted sources like:
  - [Krebs on Security](https://krebsonsecurity.com/)
  - [BleepingComputer](https://www.bleepingcomputer.com/)
  - [Threatpost](https://threatpost.com/)
  - [Dark Reading](https://www.darkreading.com/)
- 🧠 **Local summarization** with [LLaMA 3.2B via Ollama](https://ollama.com)
- 💌 **Gmail integration** to send a 5-minute-read email digest daily
- 📅 **Scheduler** to automate daily updates using `APScheduler`
- 🎙️ Optional transcript support for AI voice/video generation

---

## 📁 Project Structure
Hackathon-Projects/
├── data_fetcher.py        # Scrapes cybersecurity headlines
├── summarizer.py          # Uses Ollama + markdown → HTML formatting
├── email_sender.py        # Sends Gmail emails using SMTP
├── main.py                # Runs the full pipeline manually or on schedule
├── scheduler.py           # Sets up and runs the daily job
├── requirements.txt       # Dependencies
└── secrets.env            # Email credentials (not tracked in Git)

---

## 🛠️ Setup Instructions

1. **Clone this repository**
   ```bash
   git clone: https://github.com/Zidoyrim/Hackathon-Projects.git
   cd Hackathon-Projects

2.pip install -r requirements.txt


3.	Install and run Ollama
	•	Install: https://ollama.com/download
	•	Pull model: ollama pull llama3.2:latest

4.	Create a .env file for Gmail

5. Run command
   python main.py
