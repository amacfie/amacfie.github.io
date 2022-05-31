---
layout: post
title: "Classic probability puzzles and their solutions"
excerpt_separator: <!--more-->
---

### Envelope paradox

**Problem:**
You are given two blank envelopes which each contain money.
One envelope contains twice as much as the other.
You may choose an envelope and keep the money it contains.
After choosing, you have the option to switch for the other envelope.
Should you switch?

<!--more-->

**Pitfall:**
Clearly there is no reason to switch (or not to switch) since the envelopes are
blank and at no point do you learn anything new about their contents.
However, the following argument seems to show you actually should switch.
Let $$X$$ be the amount of money in the envelope chosen originally.
The other envelope contains an amount of either $$2X$$ or $$X/2$$, each with
probability $$1/2$$.
Thus the expected value of the other envelope is

$$\frac{1}{2} (2X) + \frac{1}{2} (X/2) = \frac{5}{4} X > X.$$

...so you should switch?

**Solution:**
Whenever things get tricky, it's best to be as formal and methodical as
possible.
What do we actually mean by $$X$$?
We're taking $$X$$ to be the amount of money in the envelope we choose
originally.
That means $$X$$ is a random variable whose value depends on the random choice
of the original envelope.
It's true that $$X$$ is equally likely to be either the smaller or larger amount.
Let these be $$x$$ and $$2x$$.
Then we need to find the expected value of the other envelope.
Let the value of the other envelope be $$X'$$.
Implicitly we are finding the expected value of $$X'$$ by conditioning
on the value of $$X$$.
There are two possibilities, and in each case we know what we get:

$$
\begin{align*}
\mathbb{E}(X') &= \mathbb{P}(X' > X)\mathbb{E}(X' | X' > X)
  + \mathbb{P}(X' < X)\mathbb{E}(X' | X' < X) \\
  &= \frac{1}{2}\mathbb{E}(X' | X' > X)
  + \frac{1}{2}\mathbb{E}(X' | X' < X)
\end{align*}
$$

Note that depending on whether $$X' > X$$ or $$X' < X$$ the value of $$X$$ is
different.
If $$X' > X$$, then $$X = x$$ and $$X' = 2X = 2x$$, and if $$X' < X$$, then $$X = 2x$$
and $$X' = X/2 = x$$.
So,

$$
\begin{align*}
\frac{1}{2}\mathbb{E}(X' | X' > X) + \frac{1}{2}\mathbb{E}(X' | X' < X)
  &= \frac{1}{2}\mathbb{E}(X' | X'=2X) \\
  &\qquad {} + \frac{1}{2}\mathbb{E}(X' | X'=X/2) \\
  &= \frac{1}{2}2x + \frac{1}{2}x \\
  &= \frac{3}{2}x \\
  &= \mathbb{E}(X).
\end{align*}
$$

Comparing with the pitfall solution, the key difference is that we cannot
use the same symbol $$X$$ in two cases if our assumption about the value of
$$X$$ is different in each case.
Tricky!

### Monty Hall problem

**Problem:**
In the TV game show Let's Make a Deal, you get to win a prize by opening
one of three doors.
Behind one door is a car and behind the others are goats.
You pick a door, say #1, and without opening #1 the host Monty Hall
intentionally shows you that a goat is behind another door, say
\#3, and gives you the chance to change to #2.
Should you change doors?

**Pitfall:**
You have the choice between two doors, one with a car, the other with a goat.
Reasoning by symmetry, the probability of each configuration is $$1/2$$, so there
is no point switching.

**Solution:**
It's true that we know there are two possible configurations at this point,
but that's not all we know.
We also know that #2 was _not_ a door chosen by Monty as a door with a goat.
This gives us an extra clue that #2 might have the car.

Again, the best way to deal with tricky problems is being as rigorous
as possible.
Let's explicitly set up a probability model as follows.
Let $$C \in \{1,2,3\}$$ be the random variable for the door with the car.
Let $$S_3$$ be the event that Monty chooses #3 to show a goat.
Then we can write down the following conditional probabilities.

$$
\begin{align*}
\mathbb{P}(S_3|C=1)&=\frac{1}{2} \\
\mathbb{P}(S_3|C=2)&=1 \\
\mathbb{P}(S_3|C=3)&=0.
\end{align*}
$$

These are all we need to compute $$\mathbb{P}(C=2|S_3)$$, which is the probability
of winning if we switch.
Using Bayes's rule, we have

$$
\begin{align*}
\mathbb{P}(C=2|S_3)
&= \frac{\mathbb{P}(S_3|C=2)\mathbb{P}(C=2)}{\mathbb{P}(S_3)} \\
&=\frac{\mathbb{P}(S_3|C=2)\mathbb{P}(C=2)}{
  \sum_{i=1}^3 \mathbb{P}(S_3|C=i)\mathbb{P}(C=i)} \\
&=\frac{\mathbb{P}(S_3|C=2)}{
  \mathbb{P}(S_3|C=1)+\mathbb{P}(S_3|C=2)+\mathbb{P}(S_3|C=3)} \\
&=\frac{1}{\frac12+1+0} =\frac23 > \frac{1}{2}.
\end{align*}
$$

### Feminist bank teller question

**Problem:**
Linda is 31 years old, single, outspoken, and very bright.
She majored in philosophy.
As a student, she was deeply concerned with issues of discrimination and
social justice, and also participated in anti-nuclear demonstrations.

Which is more probable?

1. Linda is a bank teller.
2. Linda is a bank teller and is active in the feminist movement.

**Pitfall:**
The description makes it very plausible that Linda is active in the feminist
movement, therefore #2 is more likely than #1.

**Solution:**
This is an example of the conjunction fallacy.
Let $$B$$ be the event Linda is a bank teller, and let $$F$$ be the event that
Linda is active in the feminist movement.
Then we can immediately say $$\mathbb{P}(B) \geq \mathbb{P}(F \cap B)$$
since $$F \cap B \subseteq B$$.
And so #2 cannot be more probable than #1.

In general, if more details are added, we cannot become more confident in a
claim.
This goes against a bias we have to consider situations more plausible if
they are specific and vivid.
For more on cognitive biases and heuristics, see
[_Thinking, Fast and Slow_](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow),
but also see
[the mistakes in that book caused by cognitive biases and heuristics](https://replicationindex.wordpress.com/2017/02/02/reconstruction-of-a-train-wreck-how-priming-research-went-of-the-rails/comment-page-1/#comment-1454).

### Base rate neglect

**Problem:**
A certain disease affects 1 in 1000 people.
A medical diagnostic test for the disease has 95% accuracy, i.e.
95% of the time it gives the correct diagnosis (whether you're diseased
or not).
<!-- you could have a test that's right 95% of the time for a random person
but always says you have the disease when you have it. so we need the
parenthetical -->
Suppose you take the test and it reads positive, what is the probability
that you have the disease?


**Pitfall:**
Since the diagnostic has 95% accuracy, then in my case I can conclude that
the probability I have the disease is 95%.

**Solution:**
Let $$D$$ be the event I have the disease, and let $$P$$ be the event I receive
a positive diagnosis.
We seek $$\mathbb{P}(D|P)$$.
Bayes's rule gives

$$
\begin{align*}
\mathbb{P}(D|P) &= \frac{\mathbb{P}(P|D)\mathbb{P}(D)}{\mathbb{P}(P)} \\
  &= \frac{\mathbb{P}(P|D)\mathbb{P}(D)}{\mathbb{P}(P|D)\mathbb{P}(D)
    + \mathbb{P}(P|\neg D)\mathbb{P}(\neg D)} \\
  &= \frac{(0.95)(0.001)}{(0.95)(0.001)
    + (0.05)(0.999)} \\
  &= 0.019 = 1.9\%.
\end{align*}
$$

So the probability I have the disease is actually very small, even though
I got a positive test.
This is another case of not using all the information we have.
The 95% accuracy needs to be combined with the very low probability that
anyone has the disease.
Problems of this type have been given to doctors and medical students who
often fail to find the solution.

### Birthday paradox

**Problem:**
In a group of 23 people, what is the probability that at least 2 of them
have the same birthday?

**Pitfall:**
The probability must be small since there are only 23 people and 365 possible
birthdays.

**Solution:**
Let $$N$$ be the event no 2 people have the same birthday.
The total number of assignments from people to birthdays is
$$365^{23}$$.
The total number of assignments from people to birthdays with no repeats
is $$365 \cdot 364 \cdot \,\cdots\, \cdot 343$$ since
there are 365 possibilities for the first person's birthday, which leaves
364 possibilities for the next, and so on.
But

$$
\mathbb{P}(N) = \frac{365^{23}}{365 \cdot 364 \cdot\, \cdots\, \cdot 343} = 0.492703.
$$

Then the probability that 2 people share a birthday is $$1-0.492703=0.507297$$.
So the probability isn't small; in fact it's greater than $$1/2$$!
It's true that any given pair of people are unlikely to share a birthday,
but as the size of the group grows, the probability that all pairs do not
share a birthday becomes small.
There are $$\binom{23}{2} = 253$$ different pairs of people in a group of 23.

