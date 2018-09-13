
### print(tweet.text.encode('utf=8))  changes normall text to utf8 format,the pi does not understand unicode and ascii

# importing the module
import tweepy

def tweet_send(message):
    # personal details
    consumer_key ="PrVAMU3WgCL8yRyU0P8fnc1yU"
    consumer_secret ="NUkAq6Y16N5FrPX2hsvRAQcn3B0mU85b3xyzHUmMpu0Vt6otBo"
    access_token ="947744588697042945-AVjCrdprkbLGDr8RCxMC3XmO6ehQDXr"
    access_token_secret ="KtioiJD8RNTHMvBSCce4VXnD1bqKTbym9Z1fwYNmXaveR" 

    # authentication of consumer key and secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # authentication of access token and secret
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # update the status
    # tweet = message
    api.update_status(status = message) # in case encounter failure, set status = message and uncomment prev assignment

tweet_send('ALARM!, Security piCam Update ... someone might be on your doorstep pls @_the_ike')
