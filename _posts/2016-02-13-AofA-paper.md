---
layout: post
title: "On arXiv: Analysis of Algorithms and Partial Algorithms"
---

Say there's a computational problem, e.g. sorting.
For each input array
$$w$$, algorithm $$A$$ takes $$c_A(w)$$ steps, and algorithm $$B$$ takes
$$c_B(w)$$ steps.
Normally we compare $$A$$ and $$B$$ by grouping inputs by length, finding
the worst/average case of $$A$$ and $$B$$ for each length, and comparing the
two resulting running time sequences asymptotically.

What if we didn't want to use asymptotics and we cared about finite input
lengths?
The problem then is we might not get a definitive answer.
One algorithm might be faster on inputs of length $$2$$, the other might be
faster on inputs of length $$3$$.
We can get around this if we weight each input length and find the expected
running time over all input lengths.
But now the issue is that the expectation may not converge.

In general, $$c_A(w)$$ is unbounded.
However, instead of minimizing $$c_A(w)$$, why not maximize
$$1/c_A(w)$$, which is bounded?

This gives rise to a definition of what we'll call an _algorithm score_:
$$S(A) = E(1/c_A)$$.
One interesting property of these algorithm scores is that if an algorithm
doesn't terminate on some inputs, that's fine.
We just say $$1/c_A(w) = 0$$ for those $$w$$ and carry on with the expectation.
In normal analysis of algorithms, if an algorithm doesn't terminate on an
input, there's no obvious way to say anything about its performance.

Do algorithm scores agree with our usual idea of what makes an algorithm
efficient?
Smoothed analysis was the answer to the question "why is the simplex method
efficient in practice but not in theory?".
Are there other algorithms that are inexplicably fast or slow in practice until
we use algorithm scores instead of running time sequences?
These are open questions.

Automated theorem proving algorithms must not halt on some inputs so they
become analyzable now with algorithm scores.
One implication of this is that
"[logical uncertainty](http://lesswrong.com/lw/l4p/logical_uncertainty_reading_list/)"
modules may be analyzed indirectly.

Further details on these ideas may be found in the
[pdf](http://arxiv.org/abs/1601.03411).
