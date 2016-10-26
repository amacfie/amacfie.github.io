---
layout: post
title: What is approximate Solomonoff induction?
---

_Solomonoff's prior_ $$m$$ is a probability measure on
finite strings which is defined [here](http://www.scholarpedia.org/article/Algorithmic_probability#Discrete_Universal_A_Priori_Probability).
It is argued that $$m$$ is the optimal prior for making predictions in an unknown
environment.
Since it is incomputable, presumably we would get approximately good
predictions if we approximate $$m$$.
The question is, how?
We could consider approximation algorithms for $$m$$, or approximation
algorithms for a computable bounded version $$m^t$$.
Usually approximation algorithms are analyzed according to their error ratios,
but for approximating $$m$$ we could also look at [statistical distance](https://en.wikipedia.org/wiki/Statistical_distance).
Alternatively, we could approximate Kolmogorov complexity, and use that to
approximate $m$.
Or we could restrict the class of programs to search through.
We could even consider programs which return approximately matching strings.
If we somehow boil these down into a single error function, then we can, say,
search for polynomial time algorithms which minimize the error.
But until we decide what to optimize, the Solomonoff prior doesn't say anything
useful about how to make optimal predictions.

