from abc import ABC, abstractmethod
import math

import numpy
from pydantic import BaseModel

class Scorer(BaseModel, ABC):
    @abstractmethod
    def score(self, comment: 'Comment', t: float):
        pass

# *Trivial*

class Random(Scorer):
    def score(self, comment: 'Comment', t: float):
        return numpy.random.rand()

class Ratio(Scorer):
    def score(self, comment: 'Comment', t: float):
        if comment.num_up + comment.num_down == 0:
            return 0
        else:
            return ((-comment.num_down + comment.num_up) /
                (comment.num_down + comment.num_up))

class Difference(Scorer):
    def score(self, comment: 'Comment', t: float):
        return comment.num_up - comment.num_down

class Perfect(Scorer):
    def score(self, comment: 'Comment', t: float):
        return comment.upvote_prob

# *Greedy*

class BayesAvg(Scorer):
    prior_votes: int = 7

    def score(self, comment: 'Comment', t: float):
        return (comment.num_up - comment.num_down) / (
            comment.num_up + comment.num_down + self.prior_votes
        )

# https://www.evanmiller.org/how-not-to-sort-by-average-rating.html
class Reddit(Scorer):
    def score(self, comment: 'Comment', t: float):
        up = comment.num_up
        down = comment.num_down
        if up + down == 0:
            return 0
        return (((up + 1.9208) / (up + down) - 1.96 * math.sqrt(
                    (up * down) / (up + down) + 0.9604
                ) / (up + down)
            ) / (1 + 3.8416 / (up + down))
        )

# *Future-aware heuristics*

# https://medium.com/hacking-and-gonzo/how-hacker-news-ranking-algorithm-works-1d9b0cf2c08d
# note that for negative net upvotes this actually gives newer comments a
# disadvantage
class HN(Scorer):
    gravity: float = 1.8

    def score(self, comment: 'Comment', t: float):
        age = t - comment.created_at
        return (comment.num_up - comment.num_down) / (age+2)**self.gravity

# https://stackoverflow.com/questions/27781751/what-is-youtube-comment-system-sorting-ranking-algorithm
# not sure if this is correct: is it (1/3)*(s/10+a) or 1/(3*(s/10+a))?
class YouTube(Scorer):
    def score(self, comment: 'Comment', t: float):
        if comment.num_up + comment.num_down == 0:
            ratio = 0
        else:
            ratio = comment.num_up / (comment.num_down + comment.num_up)
        c = ratio
        s = t * 60
        a = (t - comment.created_at) * 60
        x = 1/3 * (s/10 + a) * abs(a-3*s)
        n = x * (c/4 + 1)
        return n


class ModifiedBayes(Scorer):
    prior_votes: int = 7
    decay_rate: float = 1
    gravity: float = 1

    def score(self, comment: 'Comment', t: float):
        age = t - comment.created_at
        prior_vote_val = (age + 1)**(-self.decay_rate)
        return ((comment.num_up - comment.num_down + self.prior_votes *
            prior_vote_val) / ( self.prior_votes + (age+1)**self.gravity)
        )

