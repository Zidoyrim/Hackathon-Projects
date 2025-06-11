import feedparser

CYBER_FEEDS = [
    "https://krebsonsecurity.com/feed/",
    "https://www.bleepingcomputer.com/feed/",
    "https://threatpost.com/feed/",
    "https://www.darkreading.com/rss.xml", 
    "https://info.phishlabs.com/blog/rss.xml",
    "https://blog.talosintelligence.com/rss/",
    "https://unit42.paloaltonetworks.com/feed/",
    "https://www.bankinfosecurity.com/rss",
    "https://krebsonsecurity.com/feed/",
    "https://feeds.feedburner.com/TheHackersNews"
]


KEYWORDS = ["cybersecurity", "fraud", "ransomware", "phishing", "data breach"]

def fetch_cybersecurity_trends():
    results = []
    for feed_url in CYBER_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            content = (entry.title + entry.get("summary", "")).lower()
            if any(keyword in content for keyword in KEYWORDS):
                results.append(f"{entry.title}\n{entry.link}")
    return results