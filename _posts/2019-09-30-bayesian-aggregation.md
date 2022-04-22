---
layout: post
title: Belief aggregation with computational constraints
---

Imagine a risk-neutral set of traders, each with a common prior which is
updated with some private information.
The traders buy and sell contingent claims until prices reach an equilibrium.
The resultant prices are the conditional expectations of the terminal payoffs
under a probability measure $$\mathbb{P}$$.
Is $$\mathbb{P}$$ equal to the posterior obtained by updating the
common prior with the combined private information?
At least under certain conditions,
[yes](https://web.stanford.edu/~ost/papers/aggregation.pdf).

Great, so maybe there should be an efficient distributed algorithm to do
Bayesian inference by splitting up the dataset, doing inference on each
worker, and then aggregating the results?
Well, presumably yes -- if workers have an exact representation of their
posteriors.
But if the workers obtain their posteriors approximately by MCMC sampling, the
answer so far is no.
Distributed
[Bayesian consensus methods](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41849.pdf)
exist that use heuristics such as weighted averaging but they "lack rigorous
justification and provide no guarantees on the quality of inference".

So, do precise distributed Bayesian inference methods exist?
If yes, we unlock a new world of Bayesian big data.
If no, what is the character of belief aggregation in markets with
computationally bounded Bayesian traders?

