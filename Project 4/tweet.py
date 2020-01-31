import twitter
import random

# Get Twitter followers
api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='', access_token_secret='')
followers = api.GetFollowers()

# Pick one at random
randomIndex = random.randint(0, len(followers) - 1)
randomFollower = followers[randomIndex]
print(randomFollower.screen_name)

# Tweet at the random follower
tweet = "@ {} you are the random follower of the day. Turn up!"
api.PostUpdate(tweet)
print(tweet)

