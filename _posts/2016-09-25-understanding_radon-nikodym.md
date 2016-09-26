---
layout: post
title: Understanding the Radon-Nikodym theorem
---

_Note: "Almost everywhere" will be with respect to the Lebesgue measure._

Say we have a probability distribution function (df) which is not
differentiable, e.g.
$$F(x) = x [0 \leq x < 1] + [1 \geq x]$$.
Then $$F$$ is not differentiable everywhere, but it
still has a density $$f$$ such that $$F(x) = \int_{-\infty}^x f$$, namely $$f(x) =
[0 \leq x < 1]$$, or anything equal to $$f$$ almost everywhere.

So we should relax differentiability as a requirement for the existence of
densities.
If there is an $$f$$ such that $$F$$ is the Lebesgue integral of $$f$$, that's
enough.

Non-decreasing functions such as dfs are differentiable almost everywhere, so
we know $$F'$$ exists (uniquely) almost everywhere.

If we start with an $$f$$ which integrates to $$F$$, then $$F' = f$$ almost
everywhere and we can say $$f$$ is the density of $$F$$.
This is because Lebesgue-measure-0 sets don't affect integrals.

If we start with $$F$$, then $$F'$$ doesn't always give us a density for $$F$$.
This is because Lebesgue-measure-0 sets do affect derivatives.
Example: $$F(x) = [0 \leq x]$$.
Clearly this example and any discontinuous dfs will not have densities.
But being continuous is not enough.

It turns out that having a density in the almost everywhere sense means being
'absolutely continuous'.
Two definitions of absolute continuity of $$F$$:

* $$F(A)=0$$ for every $$A$$ for which $$\lambda(A)=0$$

* For every $$\epsilon$$ there is a $$\delta$$ s.t. for each collection of finite
  intervals $$[a_i, b_i], i=1,\ldots,k$$ we have
  $$ \sum_{i=1}^k |F(b_i) - F(a_i)| < \epsilon \text{ if }
    \sum_{i=1}^k (b_i - a_i) < \delta$$
  (a strict strengthening of uniform continuity.)

We can generalize the definition of absolute continuity to be relative to an
arbitrary measure.
If $$\mu$$ and $$v$$ are measures on $$(\Omega, \mathcal{B})$$, then $$\mu$$ is
absolutely continuous w.r.t $$v$$ iff for every $$A \in \mathcal{B}$$, if
$$v(A) = 0$$ then $$\mu(A) = 0$$.
This is written $$\mu << v$$ (think of the $$<$$ signs as arrows pointing in the
direction of the implication).
So "absolute continuity" by itself is respect to $$\lambda$$.

This gives us an analogous definition of _density with respect to a measure_:

Radon-Nikodym theorem:
If $$\mu$$ and $$v$$ are probability ($$\sigma$$-finite) measures on a measurable
space $$(\Omega, \mathcal{B})$$ such that $$v$$ is absolutely
continuous w.r.t. $$\mu$$, then there exists a nonnegative density function
$$\frac{dv}{d\mu}: \Omega \rightarrow \mathbb{R}$$ s.t. $$v(A) = \int_A
\frac{dv}{d\mu} d\mu$$ for all $$A \in \mathcal{B}$$.

Facts: $$\frac{dv}{d\mu}$$ is $$\mu$$-measurable and unique up to a set of
$$\mu$$-measure $$0$$.
Although $$\frac{dv}{d\mu}$$ is sometimes called a Radon-Nikodym derivative,
it is not a derivative in the sense of a derivative at a point.
Thus we merely call it a "density".

Note that the theorem only holds for $$\sigma$$-finite measures, $$\lambda$$
isn't actually included.

