import tweepy
import math
import os

auth = tweepy.OAuthHandler(os.environ["CONSUMERKEY"], os.environ["CONSUMERSECRET"])
auth.set_access_token(os.environ["ACCESSTOKEN"], os.environ["ACCESSSECRET"])
api = tweepy.API(auth)

recent_primes = list(reversed(api.user_timeline(screen_name='_primes_')))
for prime in recent_primes:
    if not prime.favorited:
        prime.favorite()
        p = int(prime.text)
        plnp = int(p/math.log(p))
        try:
            api.update_status(status="{}\nhttps://twitter.com/_primes_/status/{}".format(plnp, prime.id),
                          in_reply_to_status_id=prime.id)
        except tweepy.error.TweepError:
            continue
