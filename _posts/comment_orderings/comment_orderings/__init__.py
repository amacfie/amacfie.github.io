from abc import ABC, abstractmethod
from typing import List, Union
import itertools
import math
import random

from pydantic import BaseModel
from scipy import stats
import numpy

from comment_orderings import scores

# https://stackoverflow.com/questions/18441779/how-to-specify-upper-and-lower-limits-when-using-numpy-random-normal
def trunc_norm_sample(mu, sigma, a=0, b=1):
    return stats.truncnorm.rvs(
        (a-mu)/sigma, (b-mu)/sigma, loc=mu, scale=sigma
    )

# https://stackoverflow.com/questions/6824681/get-a-random-boolean-in-python
def random_boolean(p):
    return True if random.random() < p else False


class Comment(BaseModel):
    created_at: float
    upvote_prob: float
    downvote_prob: float
    num_up: int
    num_down: int
    score: float

class Simulation(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    visitors_per_h: float
    prob_comment: float

    downvote_prob_leave: float
    novote_prob_leave: float

    scorer: scores.Scorer
    comments: List[Comment] = []

    def get_vote_probs(self):
        category = numpy.random.choice(
            ['stinker', 'mediocre', 'great'],
            p=[0.1, 0.8, 0.1],
        )
        if category == 'stinker':
            prob_upvote = trunc_norm_sample(mu = 0.05, sigma = 0.1)
            prob_downvote = trunc_norm_sample(mu = 0.5, sigma = 0.2)
        elif category == 'mediocre':
            prob_upvote = trunc_norm_sample(mu = 0.1, sigma = 0.05)
            prob_downvote = trunc_norm_sample(mu = 0.05, sigma = 0.05)
        else:
            prob_upvote = trunc_norm_sample(mu = 0.5, sigma = 0.2)
            prob_downvote = trunc_norm_sample(mu = 0.05, sigma = 0.1)
        return (prob_upvote, prob_downvote)

    def run(self):
        self.comments = []
        num_visitors = math.floor(24 * self.visitors_per_h)
        for t in numpy.linspace(0, 24, num_visitors):
            for comment in self.comments:
                comment.score = self.scorer.score(comment=comment, t=t)
            self.comments.sort(key=lambda comment: comment.score, reverse=True)

            is_commenter = random_boolean(self.prob_comment)
            if is_commenter:
                upvote_prob, downvote_prob = self.get_vote_probs()
                self.comments.append(Comment(
                    created_at = round(t, 3),
                    upvote_prob=round(upvote_prob, 3),
                    downvote_prob=round(downvote_prob, 3),
                    num_up= 0,
                    num_down=0,
                    score= 0,
                ))
            else:
                for comment in self.comments:
                    upvote = random_boolean(comment.upvote_prob)
                    downvote = random_boolean(comment.downvote_prob)
                    if upvote:
                        comment.num_up += 1
                        leave = False
                    elif downvote:
                        comment.num_down += 1
                        leave = random_boolean(self.downvote_prob_leave)
                    else:
                        leave = random_boolean(self.novote_prob_leave)
                    if leave:
                        break

        total_upvotes = sum([ comment.num_up for comment in self.comments ])
        upvotes_per_visitor = total_upvotes / num_visitors
        return upvotes_per_visitor

