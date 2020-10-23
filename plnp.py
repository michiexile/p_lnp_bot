import tweepy
import math
import sys

auth = tweepy.OAuthHandler(sys.env["CONSUMERKEY"], sys.env["CONSUMERSECRET"])
auth.set_access_token(sys.env["ACCESSTOKEN"], sys.env["ACCESSSECRET"])
api = tweepy.API(auth)

recent_primes = list(reversed(api.user_timeline('_primes_')))
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
