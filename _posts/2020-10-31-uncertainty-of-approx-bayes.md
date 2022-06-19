---
layout: post
title: Uncertainty due to computational approximation in Bayesian inference
---

In Bayesian inference, we can factor approximate computation (e.g.
[linearization](https://www3.nd.edu/~esims1/log_linearization_sp12.pdf)) into the actual
posterior probabilities.

Suppose we have a [pmf](https://en.wikipedia.org/wiki/Probability_mass_function)
$$f(x) = P(X=x)$$ which is hard to compute.
If we approximate $$f$$ by $$\tilde{f}$$ then

$$
\begin{align*}
P\left(X = a \,|\, \text{we only compute } \tilde{f}\right)
&= \sum_x x P \left(f(a)=x \,|\, a, \tilde{f}(a) \right)\\
&= E\left(f(a) \,|\, a, \tilde{f}(a) \right)
\end{align*}
$$

What is $$P\left(f(a)=x \,|\, a, \tilde{f}(a)\right)$$?
Well, if $$f$$ is hard to compute then we probably can't gather much data, so
there are various options to produce a subjective belief:
* average-case analysis of $$\tilde{f}$$ with an uninformed prior, e.g.
  probabilistic numerics
* reference classes of "similar" cases
* uniform distribution across worst-case bounds
* past empirical experience
* etc.

Note that if the mean of the pmf $$P(f(a)=\cdot \,|\, a, \tilde{f}(a))$$
is $$f(a)$$ then $$P(X = a \,|\, \text{we only compute } \tilde{f}) =  P(X=a)$$.
So accounting for uncertainty due to approximation is equivalent to
"de-biasing" it.

_Example:_
Suppose $$f$$ has a single atom and our approximation $$\tilde{f}$$ is
modeled as $$f$$ shifted by some unknown amount:
$$\tilde{f}(x) = f(x + Y - 5)$$, where
$$Y \sim {\rm B{\small IN}}(10, 1/2)$$.
If $$\tilde{f}(0) = 1$$, then

$$
\begin{align*}
P(X=0 \,|\, \text{we only compute } \tilde{f})
&= P(f(0) = 1 \,|\, \tilde{f}(0) = 1) \\
&\approxeq P(\tilde{f}(0) = 1 \,|\, f(0) = 1) \\
&=\binom{10}{5} 2^{-10} \doteq 0.246.
\end{align*}
$$

(The approximate equality holds if, say, we assume the location of the atom is
a priori uniformly distributed on a large integer interval.)

Note that this is not completely new. E.g. when [inferring how likely it is
that software is bug-free based on a finite set of
tests](https://www.nist.gov/publications/software-testing-statistical-methods-preliminary-success-estimates-approaches-based-0),
we are putting probability distributions on mathematically determined
statements, assuming the software is deterministic.

Inference is approximated for computational reasons in many places such as
linearization as mentioned already, clustering by compression using a zip
algorithm (instead of computing Kolmogorov complexity), PASS-GLM, MCMC
sampling, numerical methods, approximation algorithms, probabilistic
data structures, et cetera.

Is this ultimately rigorous in a decision theoretic sense? I don't think so,
but
[what is rigorous](http://amacfie.github.io/2017/10/10/probability-riemann-hypothesis/)
can easily be mathematically intractable.
So whatever, it's a heuristic.

