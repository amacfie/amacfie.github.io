---
layout: post
title: "The Fundamental Theorem of Asset Pricing is Bayesianism"
excerpt_separator: <!--more-->
---

If uncertainties encode bet preferences as represented by probabilities,
Bayesianism is a collection of Dutch book arguments proving that probabilities
must be consistent with each other (defining a probability measure) to be
rational.
Weisberg has [an excellent paper][weisberg] that explains the details.
On the other hand, the Fundamental Theorem of Asset Pricing proves that for
prices to be arbitrage-free, they must be [conditional expectations](https://en.wikipedia.org/w/index.php?title=Conditional_expectation&oldid=858130631#Conditional_expectation_with_respect_to_a_sub-%CF%83-algebra).
<!--more-->
Details on the relevant results are found in
"The Mathematics of Arbitrage", by Delbaen and Schachermayer.
Having a consistent probability function has been [shown][scoring] to be
equivalent to minimizing a proper scoring rule.
And conditional expectations have been [shown][bregman] to minimize
Bregman divergences.
Et cetera.
The correspondance between these theories is alluded to by [Nau][nau].


[weisberg]: https://web.archive.org/web/20181217223439/https://jonathanweisberg.org/pdf/VarietiesvF.pdf
[nau]: https://web.archive.org/web/20180319141859/https://faculty.fuqua.duke.edu/~rnau/definettiwasright.pdf
[bregman]: https://www.semanticscholar.org/paper/On-the-optimality-of-conditional-expectation-as-a-Banerjee-Guo/56df317c39f685e75b340c8538b699088ffa918c
[scoring]: https://web.archive.org/web/20181030055011/http://www.princeton.edu/~osherson/papers/nuEll11.pdf

