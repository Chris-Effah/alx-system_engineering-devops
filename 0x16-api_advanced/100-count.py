#!/usr/bin/python3
"""
prints titles 
"""


import praw

def count_words(subreddit, word_list, reddit=None, word_count=None):
    """
    a function that counts words
    """
    if reddit is None:
        reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                             client_secret='YOUR_CLIENT_SECRET',
                             user_agent='YOUR_USER_AGENT')
    
    if word_count is None:
        word_count = {}

    # Fetch hot articles from the subreddit
    subreddit_instance = reddit.subreddit(subreddit)
    hot_articles = subreddit_instance.hot(limit=100)

    # Process titles of hot articles
    for submission in hot_articles:
        title_words = submission.title.lower().split()
        for word in word_list:
            if word.lower() in title_words:
                if word.lower() in word_count:
                    word_count[word.lower()] += title_words.count(word.lower())
                else:
                    word_count[word.lower()] = title_words.count(word.lower())

    # Recursively call count_words if there are more pages of hot articles
    if hot_articles._listing.next:
        return count_words(subreddit, word_list, reddit, word_count)
    
    # Print the sorted count of keywords
    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_word_count:
        print(f"{word}: {count}")
