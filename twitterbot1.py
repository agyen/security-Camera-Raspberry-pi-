
### print(tweet.text.encode('utf=8))  changes normall text to utf8 format,the pi does not understand unicode and ascii


# importing the module
import tweepy
import datetime

def tweet_send():
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
    #x = str(datetime.datetime.now())
    #x = x.split('.')
    #id = str(x[0])
    #send = 'security camera update @AbuoNana' + '  ' + id 
    #api.update_status(status="send text".encode('utf=8'))
    #pi.update_status(status=send)
    
    #print("Error in: Update status")
#tweet_send()  

    # update the status
    tweet = message
    api.update_status(status = tweet)
    
    #try:
    #except tweepy.TweepError as error:
        #if error.api_code == 187:
            # Do something special
            #tweet_send(message)
        #else:
           #raise error
    tweet_send('security camera update @AbuoNana')        
            
            
            
