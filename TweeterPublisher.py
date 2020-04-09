import tweepy
import json

with open('data.txt') as json_file:
    data = json.load(json_file)

apiKey = data.ApiKey
apiKeySecret = data.ApiKeySecret
accessToken = data.accessToken
accessTokenSecret = data.accessTokenSecret

def publish(text):
    print("so something")
    auth = tweepy.OAuthHandler(apiKey, apiKeySecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    app = tweepy.API(auth)
    app.update_status(text)
