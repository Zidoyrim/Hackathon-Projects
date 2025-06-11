from data_fetcher import fetch_cybersecurity_trends
from summarizer import summarize_with_llama
from email_sender import send_email

def run_digest():
    print("🔍 Fetching cybersecurity fraud content...")
    items = fetch_cybersecurity_trends()
    print(f"✅ {len(items)} relevant items found.")

    email_body = summarize_with_llama(items)
    send_email(email_body)

if __name__ == "__main__":
    run_digest()