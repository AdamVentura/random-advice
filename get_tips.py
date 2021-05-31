import praw

# Method to get tips from reddit
def GetTips(reddit):
    # Initialize an empty list
    tips = []
    # Create instance of the subreddit LifeProTips
    subreddit = reddit.subreddit("LifeProTips")
    # Iterate through the last 100 "hot" submissions.
    for submission in subreddit.hot(limit = 100):
        # Reformat the title appropriately
        if "[LPT]" in submission.title:
            submission.title = submission.title.replace("[LPT]", '')
        elif "LPT:" in submission.title:
            submission.title = submission.title.replace("LPT:", '')
        elif "LPT" in submission.title:
            submission.title = submission.title.replace("LPT", '')
        # Add title to list
        tips.append(submission.title)
    # When for loop completes, return the title
    return tips