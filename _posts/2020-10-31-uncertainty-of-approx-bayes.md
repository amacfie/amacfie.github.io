---
layout: post
title: Uncertainty due to computational approximation in Bayesian inference
---

In Bayesian inference, we can factor approximate computation (e.g.
linearization) into the actual posterior probabilities.

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
our options are:
* some sort of prior, treating the approximation as random from the space
  of approximations;
* average-case analysis of $$\tilde{f}$$.

Note that if the mean of the pmf $$P(f(a)=\cdot \,|\, a, \tilde{f}(a))$$
is $$f(a)$$ then $$P(X = a \,|\, \text{we only compute } \tilde{f}) =  P(X=a)$$.
So accounting for uncertainty due to approximation is equivalent to
"de-biasing" it.

Example:
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

<!--
technically P(A|B) = P(B|A)P(A)/P(B) but we're assuming P(A)=P(B) because
they're both uniform distributed on some "large" discrete interval
-->

(We assume the location of the atom is a priori uniformly distributed on a
large integer interval.)
For more theory see
[this post](http://amacfie.github.io/2017/10/10/probability-riemann-hypothesis/).

