---
layout: post
title: "A (non-expert) perspective on computer algebra research"

---

[Computer algebra](https://amzn.com/1107039037) (CA) a.k.a. symbolic
computation is a field involving mathematics, computer science, and software
engineering, that is focused on algorithms that simplify, manipulate, or
evaluate mathematical expressions and objects.

    In[1]:= Factor[x^2 + x - 2]

    Out[1]= (-1 + x) (2 + x)

As opposed to automated theorem proving or mathematical knowledge management,
CA works with familiar mathematical notation and does not involve
formal logic.
CA software does things like simplify integrals, solve differential
equations, diagonalize matrices, perform operations with finite groups
or fields, factor polynomials, compute Taylor series, et cetera.
CA does focus on some branches of mathematics more than others; indeed the word
"algebra" is in the name.
For many people working in mathematics, CA is profoundly useful as a tool,
although it's very far from replacing pen and paper completely.
Interesting and applicable, it sounds like it should be a great research
field too.
Indeed there are great research opportunities but there are also quirks to be
aware of.


When a CA algorithm works well and solves a common problem, it's a home run.
In 1998 D. Zeilberger won a Steele prize for algorithms that simplify sums, and
they fit exactly those criteria.
And there is community recognition for such accomplishments.
There are certainly plenty of big problems still out there, and building on
previous work is powerful.
It's also nice to be able to write some software to vary your research
activities, and get feedback from users.
There are even (a few) career paths in the field outside academia.
Just training in CA is valuable, too.
Learning the core motifs of CA algorithms and data structures is an
excellent way to deepen your understanding of mathematics.
The concepts of syntax and semantics, especially, illuminate a great deal.


And on the other hand...
CA is full of very hard problems and this hardness has a formal manifestation
in the sense that undecidable problems abound.
Even small sub-problems within algebraic simplification are undecidable.
It's also harder than it looks to build software that actually saves people
time.
In order to use a CA algorithm, one has to type in the input (in the correct
format), wait for it to run, then understand and manipulate the output.
Also, CA research, especially the implementation part, is not necessarily
highly rewarded in academia.
This is emphasized in [W. Stein's presentation](https://wstein.org/papers/talks/2016-06-sage-bp/bp.pdf)
about leaving academia.
There is e.g. a tendency to, on the discovery of a CA algorithm,
announce an "effective" (computable) solution; i.e. the focus is as far away
from practicality as possible.
Finally, CA systems are numerous and this means a lot of duplicated work.
There are major ones like Mathematica, Maple, Magma, and Sage, as well as
minor ones that a lot of work has still gone into, like Mathemagix and
Algebrite.
They all have completely different syntax of course and learning, say
Mathematica well enough to see that this

    Fold[#(#/#2/.{_~_~x_:>x,_->1})&,1,{##}]&

computes the LCM function is time-consuming.

I haven't chosen CA as my field, but you can make your own conclusion!

