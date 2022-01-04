# from psaw import PushshiftAPI
# api = PushshiftAPI()

# import datetime as dt

# start_epoch=int(dt.datetime(2017, 1, 30).timestamp())

# submissions = api.search_submissions(after=start_epoch,
#                             subreddit='wallstreetbets',
#                             filter=['url','author', 'title', 'subreddit'])

# for submission in submissions:
#     print(submission.title)
import praw

reddit = praw.Reddit(
    client_id="lgFgtNzEtdL6UQ",
    client_secret="fDMBU3SlX6eVv5KceWvqc3VYNO54zg",
    user_agent="uottahack2021",
    username="Ok_Usual9821",
    password="uottahack2021"
)

print(reddit.read_only)

for submission in reddit.subreddit("wallstreetbets").top(limit=10):
    data = submission.title
    #print(data.encode('cp1252', errors='replace').decode('cp1252'))
    print(data.encode('cp1252', errors='ignore')) #cp1252
    # print(submission.title)