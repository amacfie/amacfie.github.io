---
layout: post
title: "Computational complexity + finance = ?"
---

In ["Mathematics and Computation"](https://www.math.ias.edu/avi/book), Avi
Wigderson says: "I feel that the many financial models ... invite possible
revisions and extensions in the light of computational complexity theory.
Unlike game theory, the finance side of economics has had precious
few collaborations with ToC [theory of computation] so far, but I expect these
to grow."

These two fields have little overlap currently.
There may be models that
combine the two but they will have to come from people who understand both
worlds.
Finance is a very practical field and it's hard to propose solutions without
understanding the problems of the field at a practical level.
In theoretical computer science there are various subtleties e.g.
different models of computation, safe and unsafe conjectures, et cetera.
And the two fields use very different math.

The paper
["Computational complexity and information asymmetry in financial products"](https://scholar.princeton.edu/sites/default/files/derivative_0.pdf)
by Arora, Barak, Brunnermeier, Ge in 2010
is a great early work in this direction.
The main idea is to analyze when there is a kind of information asymmetry
(specifically with collateralized debt obligations) due to computational
asymmetry in the sense of, say, one-way functions.
However, this concept may or may not see extensions to other problems.

High frequency trading seems a natural domain for a computational view,
but perhaps more information needs to come to light on its fundamental
problems.
Another possibility is arbitrage pricing where traders have both limited
information and limited computational resources.
If there is only limited information, there is an excellent theory based
on the Fundamental Theorem of Asset Pricing
(see "The Mathematics of Arbitrage", by Delbaen and Schachermayer).
If pricing models are computationally nontrivial, computational resources
could be a useful factor to model.

