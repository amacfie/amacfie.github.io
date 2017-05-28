---
layout: post
title: "Markov of Chain: Automating Weird Sun tweets"
---

Let's use python to train a Markov chain generator using all the tweets from a
certain list of users, say
[this one](https://twitter.com/Grognor/lists/weird-sun-twitter/members).
We'll use the following libraries.

    from functional import seq
    import markovify
    import re
    import tweepy
    import unidecode

To use the Twitter API, we need to authenticate ourselves.
Register for your personal keys at <https://apps.twitter.com/> and then create
a `config.json` file that looks like this

    {
      "consumer_key":    "...",
      "consumer_secret": "...",
      "access_key":      "...",
      "access_secret":   "..."
    }

Now we can initialize the Twitter API provided by tweepy.

    config = seq.json('config.json').dict()
    auth = tweepy.OAuthHandler(
        config['consumer_key'], config['consumer_secret'])
    auth.set_access_token(config['access_key'], config['access_secret'])
    api = tweepy.API(auth)

First we write the following function (based on [this gist](https://gist.github.com/yanofsky/5436496))
which returns the most recent tweets of a given user.
The API limits us to at most 3240 tweets per user.

    def get_user_tweets(screen_name):
        alltweets = []

        #  200 is the maximum allowed count
        # 'extended' means return full unabridged tweet contents
        new_tweets = api.user_timeline(screen_name=screen_name, count=200,
                                      tweet_mode='extended')

        alltweets.extend(new_tweets)

        # save the id of the oldest tweet less one
        oldest_id = alltweets[-1].id - 1

        # keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:
            # since we're grabbing 200 at a time, we use `max_id` to
            #   ask for a certain range of tweets
            new_tweets = api.user_timeline(
                    screen_name = screen_name, count=200,
                    tweet_mode='extended', max_id=oldest_id)

            alltweets.extend(new_tweets)

            #update the id of the oldest tweet less one
            oldest_id = alltweets[-1].id - 1

            print("...{} tweets downloaded so far".format(len(alltweets)))

        # put each tweet on a single line
        tweet_texts = [re.sub(r'\s*\n+\s*', ' ', tweet.full_text)
                       for tweet in alltweets]

        return tweet_texts

The other interaction with Twitter we need to perform is get all users in a
list.
We'll write a function that fetches the usernames and calls `get_user_tweets`
on each:

    def get_list_tweets(screen_name, list_name):
        '''
        params: `screen_name` is the username of the owner of the list,
        `list_name` is the name of the list found in the URL
        '''

        # get list of all users in list
        user_names = []
        for user in tweepy.Cursor(
                api.list_members,
                screen_name,
                list_name).items():
            user_names.append(user.screen_name)

        # for each user, get their tweets
        list_tweets = []
        for user_name in user_names:
            list_tweets += get_user_tweets(user_name)
        print('Found {1} tweets from @{2}.'
            .format(len(list_tweets), user_name))
        return list_tweets

Let's run `get_list_tweets` and save the output to a file.

    tweets = get_list_tweets('Grognor', 'weird-sun-twitter')

    with open('data/tweetdump.txt', 'w') as f:
        f.write('\n'.join(tweets))

With all of the raw data saved, we're done with the Twitter API and we can
process the data and auto-generate tweets offline.
Assuming the file `tweetdump.txt` has a set of tweets, one per line, we
load them as a list of strings `tweets`.


    tweets = open('data/tweetdump.txt').readlines()

Some processing needs to be done in order to get high quality text from the
tweets.
The next function `process_tweet` is called on each one.

    def process_tweet(tweet):
        # convert to ASCII
        tweet = unidecode.unidecode(tweet)
        # remove URLs
        tweet = re.sub(r'http\S+', '', tweet)
        # remove mentions
        tweet = re.sub(r'@\S+', '', tweet)

        tweet = tweet.strip()

        # append terminal punctuation if absent
        if len(tweet) > 0:
            last_char = tweet[-1]
            if last_char not in '.!?':
                tweet += '.'

        return tweet

    processed_tweets = [ process_tweet(tweet) for tweet in tweets ]

And we remove any tweets that aren't useful.

    def is_excluded(tweet):
        ex = False
        # no RTs
        ex = ex or bool(re.match(r'^RT', tweet))
        # remove whitespace-only tweets
        ex = ex or bool(re.match(r'^\s*$', tweet))
        return ex

    good_tweets = [ tweet for tweet in processed_tweets
                   if not is_excluded(tweet) ]

We save the fully processed tweets for easy access later.

    with open('data/processed_tweets.txt', 'w') as f:
        f.write('\n'.join(good_tweets))

The `markovify` library lets us train, and generate from, a Markov chain very
easily.
Just load the training text and set a state size.

    text = open('data/processed_tweets.txt').read()

    text_model = markovify.Text(text, state_size=3)

    for x in range(5):
        print('* ' + text_model.make_short_sentence(140))

Some favorites:

* It is no coincidence we call them gods because we suppose they are trying to
  convince Robin Hanson.
* Tell anyone who does not produce Scott Alexander.
* Weird sun is a costly signal of the ability to remember sources of
  information, not just the study of complex manifolds.
* If you read The Hobbit backwards, it's about a layer of radioactive ash that
  develops the capacity to become larger.
* When you read a physical book, you get a dust speck in the eye.
* We all continuously scream about how the people in it are breaking the
  awkward silence.
* People are important, but so are lexicographic preferences.
* You don't need an expert Bayesian Epistemologist to ensure it's not a markov
  chain.

