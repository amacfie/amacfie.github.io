---
layout: post
title: "Some algorithmic aspects of AGI"
---

As in any field of computer science, certain computational problems and
algorithms arise in artificial general intelligence ([AGI](https://en.wikipedia.org/wiki/Artificial_general_intelligence)),
both as central objects of study and ad hoc components of systems.
Computational complexity theory and design and analysis of algorithms are
theoretical fields that look at computational problems and algorithms in
general.
What can these fields say about AGI beyond their obvious uses?
Some thoughts follow.

We could approximate [agent intelligence scores][scores] by doing
(non-asymptotic) analysis of key algorithms in the agent, e.g. in AIXI-like
agents there is a Solomonoff prior algorithm and an expectimax algorithm.
More is known about analysis of algorithms than analysis of agents, so
this might make things easier.
Simplified agent scores could also mean simpler self-improvement processes.

(Why non-asymptotic?
The tendency for constants to be small may be sufficient for common use cases,
but if we want AIs themselves to have a notion of algorithm efficiency,
they will not automatically have the human judgement necessary (to detect
large constants) in a non-negligible set of cases.
AIs might be more likely to come up with "weird" algorithms anyway.)

A general benefit of defining more practical agent scores is reducing the
reliance on experiments for evaluating agent performance.
In particular, in the AI safety literature it is clear that running powerful
agents (even in controlled environments) can be problematic.
And of course, formal analysis may have the same advantages over experiments
for agents that it does for algorithms (more precise, general, etc.).

Now, if computing agent scores even approximately is sufficiently hard to do,
formal agent evaluation and perhaps some forms of self-improvement may not
work.
In this case we're left with experimental evaluations and their concomitant
pros and cons.
My ["expected-reward analysis"][aoaapa] was supposed to approximate agent
scores but I'm pretty sure it's too impractical for humans to perform, given
how hard some other problems are (the non-linearity is its strength and its
weakness).
A framework of "generalized" approximation algorithms as in Vadim's [_Optimal
Polynomial-Time Estimators_ draft][optimalpredictors] may be more fruitful.

Computational complexity theory investigates the set of solutions to a given
computational problem.
Let's take Kolmogorov complexity (KC).
KC is, of course, incomputable, but we'll settle for a good approximation.
I'm curious about the complexity of approximating KC, i.e. what's the optimal
polynomial-time approximation factor?
No constant approximation factors are possible according to the usual
worst-case error approach, but using expected error it's a different story.
A more "general" analysis is desired.
If key problems such as KC turn out to be impossible or trivial to approximate
in theory, perhaps this tells us that the problems aren't in fact the right
ones to be solving.
This kind of analysis was done for "Heuristic Driven Theory Projection" at
[AGI 2013][robere] by Robert Robere.


[aoaapa]: http://arxiv.org/abs/1601.03411
[optimalpredictors]: https://github.com/antiquark/FAI/tree/master/Optimal%20Predictors
[robere]: http://link.springer.com/chapter/10.1007%2F978-3-642-39521-5_2
[scores]: http://arxiv.org/abs/0712.3329
