
"""
Quick and dirty script to calculate blog post publish rate and efficiency from an RSS/Atom feed.

$ python3 blog-post-publish-rate.py --start 2025-08-01 --end 2025-11-01 --feed https://dev-rel.org/blog/feed.xml --effort 2.5
Articles: 4
Authors: 3
Days: 93
Weeks: 13.29
Publish Rate (articles/week): 0.30
Publish Efficiency: 4.0143
"""

import sys
import argparse
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def parse_args():
	parser = argparse.ArgumentParser(description="Calculate blog post publish rate and efficiency.")
	parser.add_argument('--start', required=True, help='Start date (YYYY-MM-DD)')
	parser.add_argument('--end', required=True, help='End date (YYYY-MM-DD)')
	parser.add_argument('--feed', required=True, help='Blog feed URL (RSS/Atom)')
	parser.add_argument('--effort', type=float, default=100.0, help='Effort percentage (default: 100)')
	parser.add_argument('--info', action='store_true', help='Print extra info')
	return parser.parse_args()

def fetch_feed(url):
	try:
		response = requests.get(url)
		response.raise_for_status()
		return response.text
	except Exception as e:
		print(f"Error fetching feed: {e}", file=sys.stderr)
		sys.exit(1)

def parse_date(date_str):
	# Try common date formats
	fmts = [
		"%Y-%m-%dT%H:%M:%S%z",
		"%Y-%m-%dT%H:%M:%S",
		"%Y-%m-%d",
		"%a, %d %b %Y %H:%M:%S %Z",
		"%a, %d %b %Y %H:%M:%S %z",
		"%a, %d %b %Y %H:%M:%S GMT",
		"%a, %d %b %Y %H:%M:%S"
	]
	for fmt in fmts:
		try:
			return datetime.strptime(date_str, fmt)
		except Exception:
			continue
	return None

def parse_feed(feed_xml, start, end):
	root = ET.fromstring(feed_xml)
	ns = {'atom': 'http://www.w3.org/2005/Atom', 'rss': 'http://purl.org/rss/1.0/'}
	articles = []
	authors = set()
	# Try Atom first
	for entry in root.findall('.//{http://www.w3.org/2005/Atom}entry'):
		date_el = entry.find('{http://www.w3.org/2005/Atom}published') or entry.find('{http://www.w3.org/2005/Atom}updated')
		author_el = entry.find('{http://www.w3.org/2005/Atom}author/{http://www.w3.org/2005/Atom}name')
		if date_el is not None:
			pub_date = parse_date(date_el.text)
			if pub_date and start <= pub_date <= end:
				articles.append(pub_date)
				if author_el is not None:
					authors.add(author_el.text)
	# Try RSS
	for item in root.findall('.//item'):
		date_el = item.find('pubDate')
		# RSS author can be <author> or <dc:creator>
		author_el = item.find('author')
		if author_el is None:
			# Try Dublin Core creator
			for child in item:
				if child.tag.endswith('creator'):
					author_el = child
					break
		if date_el is not None:
			pub_date = parse_date(date_el.text)
			if pub_date and start <= pub_date <= end:
				articles.append(pub_date)
				if author_el is not None and author_el.text:
					authors.add(author_el.text.strip())
	return articles, authors

def main():
	args = parse_args()
	start = datetime.strptime(args.start, "%Y-%m-%d")
	end = datetime.strptime(args.end, "%Y-%m-%d")
	feed_xml = fetch_feed(args.feed)
	articles, authors = parse_feed(feed_xml, start, end)
	num_articles = len(articles)
	num_authors = len(authors)
	num_days = (end - start).days + 1
	num_weeks = num_days / 7.0
	publish_rate = num_articles / num_weeks if num_weeks > 0 else 0
	efficiency = publish_rate / (num_authors * (args.effort / 100.0)) if num_authors > 0 and args.effort > 0 else 0
	print(f"Articles: {num_articles}")
	print(f"Authors: {num_authors}")
	print(f"Days: {num_days}")
	print(f"Weeks: {num_weeks:.2f}")
	print(f"Publish Rate (articles/week): {publish_rate:.2f}")
	print(f"Publish Efficiency: {efficiency:.4f}")
	if args.info:
		print(f"Authors: {', '.join(authors)}")

if __name__ == "__main__":
	main()




