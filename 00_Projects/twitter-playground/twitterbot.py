# Twitter's API is not free anymore, so this is just an exercise to practice
import tweepy
import time

# in order to trully have access: change 'consumer_key' and 'consumer_secret' for your account keys
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
# same for token key and secret
auth.set_access_token('token key', 'secret token')

# let's ask for access to the API
api = tweepy.API(auth)

public_tweets = api.home_timeline()
# usually what the api returns has lots of info, so by doing iterable.text we can access what we can read, the content
# it often is an iterable, so we can iterate with a for loop to get all the items
for tweet in public_tweets:
    print(tweet.text)

# now let's print about me
user = api.me()
# we can access many features about 'me'
print(user.name)
print(user.screen_name)
print(user.followers_count)

# let's avoid the twitter limit error (we can't access full speed their servers)


def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)  # ms


# bot that follows back
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    # we can check all of our followers names
    print(follower.name)
    # instead of following back all of them, let's only follow back a specified user
    if follower.name == 'changeforusernameyouwanttofollowback':
        follower.follow()

# bit that likes its own tweets

search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
        # we can also retweet:
        tweet.retweet()
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
