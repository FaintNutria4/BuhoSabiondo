import tweepy
import json

with open('data.json') as json_file:
    data = json_file.read()

obj = json.loads(data)

apiKey = obj['apiKey']
apiKeySecret = obj['apiKeySecret']
accessToken = obj['accessToken']
accessTokenSecret = obj['accessTokenSecret']

def publish(text):
    print("so something")
    auth = tweepy.OAuthHandler(apiKey, apiKeySecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    app = tweepy.API(auth)
    app.update_status(text)