#!/usr/bin/python
import feedparser

d = feedparser.parse('http://www.euro2day.gr/rss.ashx?catid=125')
maxItems = 7
itemCounter = 0

for post in d.entries:
    print(post.title)
    itemCounter = itemCounter + 1
    if itemCounter == maxItems:
        break
