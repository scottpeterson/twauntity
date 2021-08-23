#!/usr/bin/env python3
import requests
import json
from collections import Counter
import re
import config


def analyze_tweet(id):
  # tweet id
  id = id

  url = f"https://api.twitter.com/2/tweets/search/recent?query=conversation_id:{id}&tweet.fields=in_reply_to_user_id,author_id,created_at,conversation_id&max_results=100"

  headers = {"Content-Type": "application/json", "Authorization": f"Bearer {config.bearer_token}"}

  r = requests.get(url = url, headers = headers)
  response = r.json()

  bigString = ""

  # put all strings into one big string
  for text in response["data"]:
    bigString = bigString + " " + text["text"]

  # Cleaning text and lower casing all words
  for char in '-.,\n':
      bigString=bigString.replace(char,' ')
  bigString = bigString.lower()

  # split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s) 
  word_list = bigString.split()

  stopwords = ["i", "me", "a", "for", "and", "to", "the", "it", "but", "this", "in", "is", "you", "it's", "i've", "can", "that", "your", "be", "of", "been", "some", "not", "which", "with", "like", "my", "all", "as", "know", "on", "has", "them", "well", "or", "would", "very", "what", "more", "than", "day", "yeah", "also", "much", "having", "an", "just", "does", "any" "only", "their", "its", 
  "are", "have", "if", "made", "will", "i've", "from", "ever", "go", "only"]

  # remove nothing words
  resultwords = [word for word in word_list if word not in stopwords]

  sorted = Counter(resultwords).most_common()

  print(sorted)


analyze_tweet("1429543981483020289")