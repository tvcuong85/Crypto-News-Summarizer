import feedparser

RSS_URL = "https://cointelegraph.com/rss"

feed = feedparser.parse(RSS_URL)

print("\n📰 Latest Crypto News\n")

for entry in feed.entries[:5]:
    print(f"Title: {entry.title}")
    print(f"Link: {entry.link}")
    print("-" * 50)
