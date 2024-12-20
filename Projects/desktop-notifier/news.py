import requests
import xml.etree.ElementTree as ET

RSS_FEED = "https://techcrunch.com/feed/"

def fetch_feed(url):
    try:
        response =requests.get(url, timeout=10)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print("Error fetching RSS feed: ", e)
        return None



def parse_feed(feed_content):
    try:
        root = ET.fromstring(feed_content)
        channel = root.find('./channel')

        if channel is None:
            print("Channel element not found!")
            return []

        news_items = []
        for item in channel.findall('./item'):
            news = {
                'title': item.find('title').text if item.find('title') is not None else 'No Title',
                'link': item.find('link').text if item.find('link') is not None else 'No Link',
                'description': item.find('description').text if item.find(
                    'description') is not None else 'No Description',
                'pubDate': item.find('pubDate').text if item.find('pubDate') is not None else 'No Date'
            }
            news_items.append(news)
        return news_items
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return []


def main():
    feed_content = fetch_feed(RSS_FEED)
    if feed_content:
        top_news = parse_feed(feed_content)
        for i, item in enumerate(top_news[:3]):
            print(f"{i + 1}. Title: {item['title']}")
            print(f"   Link: {item['link']}")
            print(f"   Published: {item['pubDate']}")
            print(f"   Description: {item['description'][:100]}...")  # Truncated description
            print("---")
        return top_news