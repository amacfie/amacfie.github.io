---
layout: post
title: "Comment ranking algorithms: Hacker News vs. YouTube vs. Reddit"
---

Comments on social sites have to be sorted somehow.
How do big platforms do it -- is it some complicated mix of
recommender systems,
learning-to-rank algorithms,
Markov decision processes,
neural networks, and
learning automata?
Well, maybe in [some cases](https://engineering.linkedin.com/blog/2017/09/serving-top-comments-in-professional-social-networks)
but often it's just a simple formula.
In this article we put the formulas used by Hacker News, YouTube, and
Reddit, along with a few alternatives, to the test, using virtual comment
section simulations.
Spoiler alert: YouTube does not do well.

## The simulation model

240 visitors arrive at equally spaced increments over a 24 hour period.
Each visitor is randomly assigned as a commenter (10%) or a voter (90%).
Commenters leave a single comment, which gets a randomly assigned quality
category: great (10%), mediocre (80%), or stinker (10%).
Great comments have a high probability of receiving upvotes and a low
probability of receiving downvotes;
stinkers are the reverse;
and mediocre comments have a low probability of receiving any votes.
Voters, on the other hand, see the top-ranked comment and vote according
to its probabilities.
At this point they stop reading or keep going based on a probability that
depends on the vote they just gave (0% for upvotes, 50% for downvotes, 15% for
non-votes).
If they don't leave, they see the next-ranked comment and the process continues
until they finally do leave or they read all the comments.
When the simulation concludes, we log the average number of upvotes per
visitor which we use as our utility function.

See [Python source code](https://github.com/amacfie/amacfie.github.io/tree/master/_posts/comment_orderings)
for full details.

Of course this is not a perfect model of every comment section.
These parameter values will not always be accurate, although I did play around
with e.g. the commenter/voter ratio
<!--and how likely a voter is to leave-->
and I got basically the same final conclusions.
Realistically the rate of visitors may vary over time.
A voter's probability of leaving after a certain comment conditional on the
most recent (non-)vote may also depend on how many comments they've already
read.
Comment threads are not represented here.
Vote probabilities may change over time.
Et cetera, et cetera.

## The ranking formulas

Here we use the following symbols

* Number of upvotes received so far: $$n_{+}$$
* Number of downvotes received so far: $$n_{-}$$
* Age of comment, in hours: $$h$$


All ranking methods in our analysis rank comments by scoring each comment
and in descending order.
The scores are determined by the formulas below.

Starting with the basics, we have the _ratio_
$$(n_{+} - n_{-})/(n_{+} + n_{-})$$
and the _difference_ $$n_{+} - n_{-}$$, a.k.a. the number of net upvotes.
We don't expect these to be optimal but they're useful baselines.
Another version of the ratio is
$$n_{+}/(n_{+} + n_{-})$$ which performs similarly.

For testing purposes, we have the _random_ ranking which is, well, just
random, and the _upvote probability_ ranking which ranks according to the true
upvote probability.

Reddit's algorithm, detailed [here](https://www.evanmiller.org/how-not-to-sort-by-average-rating.html),
is a frequentist method for estimating the true voting probabilities
based on $$n_{+}$$ and $$n_{-}$$.
The [Bayesian](https://districtdatalabs.silvrback.com/computing-a-bayesian-estimate-of-star-rating-means)
version of this is what we'll call the _Bayesian average_: the same as
_ratio_ but we imagine that a few extra "phantom" votes have been cast, say 3
downvotes and 3 upvotes.

Hacker News [roughly](https://medium.com/hacking-and-gonzo/how-hacker-news-ranking-algorithm-works-1d9b0cf2c08d)
uses the formula $$(n_{+} - n_{-}) / (h+2)^{1.8}$$,
which is like _ratio_, if we interpret the denominator $$(h+2)^{1.8}$$
as an estimate of the number votes cast.
In fact, this denominator is probably more naturally thought of as an
estimate of the number of votes cast including implicit non-votes.
Non-votes (with a value of 0) would not impact the numerator.

To get a sense of how the simulations look, here are the comments as presented
to the 240th visitor from one run using the Hacker News scoring formula:

$$h$$     | Upvote probability| Downvote probability| $$n_{+}$$  | $$n_{-}$$   | HN score
|-
 7.9 | 0.671 | 0.324 | 47  | 5  | 0.657
14.2 | 0.671 | 0.076 | 82  | 3  | 0.515
21.9 | 0.496 | 0.14  | 110 | 10 | 0.324
23.3 | 0.434 | 0.051 | 72  | 12 | 0.174
 8.9 | 0.162 | 0.03  | 8   | 0  | 0.094
14.1 | 0.112 | 0.054 | 12  | 3  | 0.060
10.9 | 0.184 | 0.058 | 6   | 0  | 0.059
 5.1 | 0.151 | 0.008 | 2   | 0  | 0.058
12.9 | 0.226 | 0.049 | 6   | 0  | 0.046
15.0 | 0.114 | 0.061 | 10  | 6  | 0.024
 7.3 | 0.021 | 0.009 | 1   | 0  | 0.017
13.4 | 0.071 | 0.008 | 1   | 1  | 0.0
 5.2 | 0.489 | 0.038 | 0   | 0  | 0.0
 3.6 | 0.151 | 0.041 | 1   | 0  | 0.0
 1.0 | 0.579 | 0.087 | 0   | 0  | 0.0
 0.7 | 0.047 | 0.024 | 0   | 0  | 0.0
21.7 | 0.158 | 0.222 | 19  | 20 | -0.003
20.7 | 0.048 | 0.017 | 1   | 3  | -0.007
10.4 | 0.055 | 0.044 | 1   | 2  | -0.010
11.3 | 0.041 | 0.027 | 0   | 2  | -0.018
19.5 | 0.104 | 0.166 | 5   | 10 | -0.019
 5.4 | 0.045 | 0.604 | 1   | 3  | -0.054

YouTube also uses a [formula](https://stackoverflow.com/a/39048550) that
involves the age of the comment.
Their system additionally factors in the user's lifetime ratio, which
for our tests we set to 0 as if all users are new.


Lastly, let's consider how we might modify the Bayesian average to take
time into account.
To make new comments more visible we'll make the phantom votes all upvotes
at first, then asymptotically reduce them to non-votes.
We'll also switch to a denominator similar to the Hacker News formula's in
order to estimate non-votes.
This yields the _modified Bayes_ formula

$$\frac{n_{+} - n_{-} + n_p / (h+1)}{n_p + h},$$

where $$n_p$$ is the number of phantom votes.
We use the value $$n_p=7$$ in the simulations.


## Ranking the rankings

Without further ado, voila:

Ranking algorithm                | Average number of upvotes per visitor
|-
_Upvote probability_ | 0.978
_Modified Bayes_       | 0.916
Hacker News          | 0.899
Bayesian average     | 0.878
_Difference_         | 0.848
Reddit               | 0.836
_Ratio_              | 0.813
YouTube              | 0.644
_Random_             | 0.607

NB The averages aren't exact -- I only did enough runs with each formula
to be pretty confident about how they compare.

So Reddit and YouTube perform worse than the simple _difference_, and
Hacker News is the only one of the three better than _Bayesian average_.
Seems reasonable to me but are the results general or just an artifact of
the model?
As always, more work required...

