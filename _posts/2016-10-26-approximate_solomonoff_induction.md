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
algorithms for a computable resource-bounded version $$m^t$$.
Should we use worst-case error or expected error?
Usually approximation algorithms are analyzed according to their error ratios,
but for approximating $$m$$ we could also look at [statistical distance](https://en.wikipedia.org/wiki/Statistical_distance).
Alternatively, we could approximate Kolmogorov complexity (or a
resource-bounded version), and use that to approximate $$m$$.
Or we could restrict the class of programs to search through according to
something other than resource bounds.
We could even consider programs which return approximately matching strings.
At least some of these notions of approximation lead to trivial optimal
solutions, so they can't all be right.
If we somehow boil these approaches down into a single error function, then we
can, say, search for polynomial time algorithms which minimize the error.
But until we decide what to optimize, the Solomonoff prior doesn't say anything
useful about how to make optimal predictions.

