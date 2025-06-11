import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv("secrets.env")

EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def send_email(html_content):
    # Add preview text (hidden)
    preview_text = """
    <span style="display:none; font-size:0px; color:#ffffff;">
        Your daily AI-curated cybersecurity fraud digest. Trends, breaches, and insights.
    </span>
    """
    html_with_preview = preview_text + html_content

    # Subject with date
    today = datetime.today().strftime('%b %d, %Y')
    subject = f"🚨 Cybersecurity Fraud Digest – {today}"

    msg = MIMEText(html_with_preview, "html")
    msg["Subject"] = subject
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_FROM, EMAIL_PASS)
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        print("✅ Digest sent via Gmail!")
    except Exception as e:
        print(f"❌ Email sending failed: {e}")
        # Save fallback if email fails
        with open("failed_email_backup.txt", "w") as f:
            f.write(html_content)