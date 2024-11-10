---
layout: post
title: "Ascending auction bidder strategy"
---

Ascending auctions are a common mechanism for selling a set of products.
The basics are covered in this video:

<iframe width="640" height="360" src="https://www.youtube.com/embed/oHkArtG9zO0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The exact rules of an ascending auction depend on the auctioneer and may
include complexities such as:
* Activity rules, where bidders can never bid on more products than in previous
  rounds
* Anonymous bidding, where information on who bid on what is hidden
* Whether bid prices in each round are fixed by the auctioneer or chosen by
  bidders

Below we review some of the main ideas of optimal bidding strategy, give
practice scenarios, and provide pointers to the relevant literature.


### Terminology

VCG = [Vickrey-Clarke-Groves](https://en.wikipedia.org/wiki/Vickrey%E2%80%93Clarke%E2%80%93Groves_auction) (sealed bid, Vickrey prices)

SAA = simultaneous (multiple products at once) ascending auction (same as SMRA)

SMRA = simultaneous multiple round ascending (same as SAA)

CCA = Combinatorial clock auction (not the same as SAA/SMRA)

[Schelling point](https://en.wikipedia.org/wiki/Focal_point_(game_theory)) = a way for independent parties to intentionally coordinate
on one choice among many

Value bidding = selecting a package to maximize value of package minus cost


### Notation

Products = $$\{1, 2, 3, \ldots, n \}$$

Quantities = $$\{q_1, \ldots, q_n\}$$

Bidders = $$\{1, 2, 3, \ldots, m \}$$

Package: $$x = x(1), \ldots, x(n)$$, where $$x(i)$$ is the quantity of product $$i$$

Valuation of bidder $$i$$ of package $$x$$: $$v_i(x)$$


### Nutshell

Generally SMRA auctions have a cooperative phase and then a competitive phase.
In the cooperative phase, bidders reduce demand (relative to value bidding) in
order to allocate products without bidding prices up.
Bidders must agree on this allocation without communicating.
Typically this implicit allocation is chosen because it's fair, natural,
symmetric, or otherwise "makes sense" given the context of the auction.


### Keys to the game

(More details below.)

* Demand reduction negotiation
  * Bidders try to indirectly find agreeable allocation
  * Selecting quantities: Schelling points based on available info
    * Auction-based, industry-based info
    * E.g. split product units 50/50 if two bidders are expected to be
      interested
  * Negotiation by sending signals within the auction
    * Presumably cheap talk in this context, but it happens
    * Much noise little signal in auctions where bids are constrained
      or hidden
  * If there is an activity rule, once you've submitted low demand, there is no
    way to increase without decreasing somewhere else
* Competition
  * Basically value bidding
  * Usually happens if negotiation fails
* [Complementarity](https://en.wikipedia.org/wiki/Complementary_good)/exposure:
  value bidding fails and "cooperation" is inefficient and less likely.
  * Bids for a quantity $$q$$ can turn into bids for quantities $$< q$$
    so be careful how high you bid if there are complementarities.
  * See literature review below for more discussion.
* Price raising
  * Only do in lots where you're not going to win anything
  * Start early (to maintain activity)


### Demand reduction

Value bidding is no longer a dominant strategy, as it is in VCG/CCA.

Say there is a single product and Bidder 1 bids on quantity 1 at
price=$$1,2,\ldots,10$$.
Assume $$v_2(1)=9, v_2(2)=10$$.

Bidder 2 (B2), strategy 1: bid on $$q=2$$ for $$p=1,\ldots,5$$, then bid on $$q=1$$
  for $$p=6$$.
B2 strategy 2: bid on $$q=1$$ for $$p=1$$.

B2 results:

* CCA, strategy 1: wins $$q=1$$ @ $$p=0$$
* CCA, strategy 2: wins $$q=1$$ @ $$p=0$$

* SMRA, strategy 1: wins $$q=1$$ @ $$p=6$$
* SMRA, strategy 2: wins $$q=1$$ @ $$p=1$$

Thus reducing demand (strategy 2) pays in the SMRA format where it didn't in
the CCA.
When both bidders reduce demand, it's called "cooperation" aka "tacit
collusion".
See the literature review below for more examples.

However, with the activity rule, there can be a risk to reducing too much
at the beginning if there is uncertainty about the cooperative outcome, so
a somewhat gradual reduction may be wise.


### Price raising

Raising prices for other bidders is a realistic motive.
In the SMRA format it's relatively simple because raising auction price is the
same as raising price paid.
You don't have to work backwards from Vickrey price calculations to see what
action would cause an increase in price.
Instead, you simply have to create
excess demand on one or more products where there otherwise would not be.
But, it's risky because your bids might end up being winning bids.

The ideal scenario is as follows:
Two rivals of yours neatly split supply 50-50, and price doesn't increase.
Then you come in and place a bid for $$q=1$$ (no point using higher $$q$$ unless
you need the activity) for a few rounds and then get out before
they decrease their bids.

So this can work for disrupting demand reduction, but only for products you
don't actually want to win (or you'd be raising your own price too).


### Demystifying strategies through experimentation

Try the following mini scenarios one or multiple times to better understand
tactics.

* People are assigned to bidders
* Bidders' valuations may be random (independently among bidders)
  * Other bidders know the possible valuations but not which one was selected
* People gain points according to their valuation, lose points to pay for
  won products
* Possible bonus points for raising rivals' prices
* Goal is not to get more points than opponent but to get more points than others playing as the same player in a different round of the same game
* In an actual auction, the other bidders may not be rational

After gaining familiarity with the mini scenarios, full scale mock auctions may
also be helpful.

#### Scenario: Dealing with uncertainty

1 product, $$q_1=2$$, 2 bidders

$$v_1(1) = 2, v_1(2) = 3$$

* With probability $$1/2$$:
$$v_2(1) = 1, v_2(2) = 2$$
* With probability $$1/2$$:
$$v_2(1) = 0, v_2(2) = 2$$


#### Scenario: Are they price raising?

2 products, $$q_1=q_2=2$$, 2 bidders

$$v_1(x, 1) = 2x + 2$$,
$$v_1(x, 2) = 2x + 3$$

With probability $$1/3$$:

$$v_2(1, y) = 2$$, $$v_2(2, y) = 3$$

Bonus points for bidder 2 only if its score is positive:
price paid by bidder 1 for product 2

With probability $$2/3$$:

$$v_2(x, 1) = v_2(x, 2) = x + 2$$


#### Scenario: Cooperating without an obvious Schelling point

1 product, $$q_1=3$$, 2 bidders

$$v_1(1)=6, v_1(2)=10, v_1(3)=12$$

$$v_2(1)=6, v_2(2)=10, v_2(3)=12$$


#### Scenario: Cooperating with uncertainty 1

1 product, $$q_1=1$$, 2 bidders

* With probability $$1/2$$:
$$v_1(1) = 3$$
* With probability $$1/2$$:
$$v_1(1) = 5$$;

* With probability $$1/2$$:
$$v_2(1) = 4$$
* With probability $$1/2$$:
$$v_2(1) = 6$$


#### Scenario: Classic intra-product exposure

1 product, $$q_1=3$$, 3 bidders

$$v_1(3) = 10$$, otherwise $$v_1(x)=0$$

* With probability $$1/2$$:
$$v_2(1) = v_2(2) = v_2(3) = 5$$
* With probability $$1/2$$:
$$v_2(1) = v_2(2) = v_2(3) = 1$$;

* With probability $$1/2$$:
$$v_3(1) = v_3(2) = v_3(3) = 4$$
* With probability $$1/2$$:
$$v_3(1) = v_3(2) = v_3(3) = 0$$


#### Scenario: Cooperating with uncertainty 2

2 products, $$q_1=q_2=3$$, 2 bidders

$$v_1(1, y) = 3 + \sqrt{2y}$$, $$v_1(2, y) = 5 + \sqrt{2y}$$,
$$v_1(3, y) = 5 + \sqrt{2y}$$

* With probability $$1/2$$:
$$v_2(1, y) = v_2(2, y) = v_2(3, y) = 2 + \sqrt{y}$$
* With probability $$1/2$$:
$$v_2(1, y) = 4 + \sqrt{y}, v_2(2, y) = 7 + \sqrt{y}, v_2(3, y) = 8 + \sqrt{y}$$


#### Scenario: Universal intra-product complementarity

1 product, $$q_1=3$$, 2 bidders

$$v_1(1) = 2, v_1(2) = 5, v_1(3) = 9$$

$$v_2(1) = 1, v_2(2) = 4, v_2(3) = 8$$


#### Scenario: Finding a Schelling point

2 products, $$q_1=q_2=3$$, 2 bidders

$$v_1(x,y) = v_2(x,y) = \sqrt{x} + \sqrt{y}$$


#### Scenario: Inter-product cooperation 1

2 products, $$q_1=q_2=1$$, 2 bidders

* With probability 1/2:
$$v_1(x,y) = \sqrt{5x + 3y}$$
* With probability 1/2:
$$v_1(x,y) = \sqrt{3x + 5y}$$;

* With probability 1/2:
$$v_2(x,y) = \sqrt{5x + 3y}$$
* With probability 1/2:
$$v_2(x,y) = \sqrt{3x + 5y}$$


#### Scenario: Inter-product cooperation 2

4 products, $$q_1=q_2=q_3=q_4=1$$, 2 bidders

* With probability 1/2:
$$v_1(x_1, x_2, x_3, x_4) = \sqrt{5(x_1+x_2) + 3(x_3+x_4)}$$
* With probability 1/2:
$$v_1(x_1, x_2, x_3, x_4) = \sqrt{3(x_1+x_2) + 5(x_3+x_4)}$$;

* With probability 1/2:
$$v_2(x_1, x_2, x_3, x_4) = \sqrt{5(x_1+x_2) + 3(x_3+x_4)}$$
* With probability 1/2:
$$v_2(x_1, x_2, x_3, x_4) = \sqrt{3(x_1+x_2) + 5(x_3+x_4)}$$


### Guide to the literature: Theoretical

Brusco, Sandro, and Giuseppe Lopomo.
2002.
[“Collusion via Signaling in Simultaneous Ascending Bid Auctions with
  Heterogeneous Objects, with and Without Complementarities.”](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.394.3028&rep=rep1&type=pdf)
_The Review of Economic Studies_ 69 (2): 407–36.

Synopsis:
Increasing the ratio of bidders to products decreases cooperation.
Complementaries among products decreases cooperation.
Optimal strategy is attempting to cooperate and value bidding if that fails.
EP is not part of the model.

Grimm, Veronika, Frank Riedel, and Elmar Wolfstetter.
2003.
[“Low Price Equilibrium in Multi-Unit Auctions: The Gsm Spectrum Auction in
  Germany.”](https://www.econstor.eu/bitstream/10419/62770/1/724885277.pdf)
_International Journal of Industrial Organization_ 21 (10): 1557–69.

Synopsis:
In German 1999 auction, products were split 50-50 between two major players
at relatively low prices.
A simple game is defined.
Assume there are $$m$$ bidders, and $$n=mk$$ products each with quantity $$1$$,
bidders have equal valuations with strictly decreasing marginal values.
The optimal strategy is to bid on $$k$$ products each. If someone competes with
you for your $$k$$, value bid.

Brusco, Sandro, and Giuseppe Lopomo.
2009.
[“Simultaneous Ascending Auctions with Complementarities and Known Budget
  Constraints.”](https://www.researchgate.net/profile/Giuseppe_Lopomo/publication/23545651_Simultaneous_ascending_auctions_with_complementarities_and_known_budget_constraints/links/556c30c008aeccd7773a2d0e/Simultaneous-ascending-auctions-with-complementarities-and-known-budget-constraints.pdf)
_Economic Theory_ 38 (1): 105–24.

Synopsis:
Analysis of exposure problem.
For example:
Big bidder has extremely complementary (convex, e.g. $$x^2$$) values. A number of
small bidders have extremely supplementary (concave, e.g. $$\sqrt{x}$$) values.
Due to lack of package bids, big bidder may decide to not bid at all.
However, in spectrum auctions I'm not sure if this is a big factor.
(Not an issue in CCA/VCG.)

Goeree, Jacob K, and Yuanchuan Lien.
2014.
[“An Equilibrium Analysis of the Simultaneous Ascending Auction.”](http://www.centrobaffi.unibocconi.it/wps/allegatiCTP/Exposure-09142010_1.pdf)
_Journal of Economic Theory_ 153: 506–33.

Synopsis: Analysis of exposure problem.

Janssen, Maarten, and Vladimir Karamychev.
2017.
[“Raising Rivals’ Cost in Multi-Unit Auctions.”](https://homepage.univie.ac.at/maarten.janssen/auctions/Raising%20Rivals'%20Cost%20in%20Multi-unit%20Auctions-V1%2011V-Ref.pdf)
_International Journal of Industrial Organization_ 50: 473–90.

Synopsis:
Discussion of when raising prices is optimal or suboptimal, when bidders
have an interest in doing so.


### Guide to the literature: Empirical

Grimm, Veronika, Frank Riedel, and Elmar Wolfstetter.
2003.
[“Low Price Equilibrium in Multi-Unit Auctions: The Gsm Spectrum Auction in
  Germany.”](https://www.econstor.eu/bitstream/10419/62770/1/724885277.pdf)
_International Journal of Industrial Organization_ 21 (10): 1557–69.

Synopsis: See above.

Kwasnica, Anthony M, and Katerina Sherstyuk.
2007.
[“Collusion and Equilibrium Selection in Auctions.”](http://test.scripts.psu.edu/users/a/m/amk17/CollEqmSel.pdf)
_The Economic Journal_ 117 (516): 120–45.

Synopsis:
Lab experiments were conducted on spontaneous cooperation in auctions.
Results (p15): Players cooperate more if they get to play the game many
times.
As the number of bidders per product increases, cooperation decreases.
With complementary products, there was little cooperation.


Cramton, Peter.
2010.
[“Simultaneous Ascending Auctions.”](http://cramton.umd.edu/papers2000-2004/cramton-simultaneous-ascending-auction.pdf)
Wiley Encyclopedia of Operations Research and Management Science.

Synopsis (Sec. 5):
Discusses auctions from around 2000 where bidders signaled and coordinated
to reduce demand.


Bichler, Martin, Vitali Gretschko, and Maarten Janssen.
2017.
[“Bargaining in Spectrum Auctions: A Review of the German Auction in 2015.”](https://homepage.univie.ac.at/maarten.janssen/auctions/bargaining-spectrum-auctions.pdf)
_Telecommunications Policy_ 41 (5-6): 325–40.

Synopsis:
Analysis of German auction in 2015 which featured cooperation, competition,
and signaling. The auction had high transparency and a great range of actions
(submitting bids higher than clock price). E.g. TEF bids on product A that
VOD was bidding on to send message that VOD should reduce demand in product B
where TEF and VOD are negotiating demand reduction.


Cramton, Peter, and Axel Ockenfels.
2017.
[“The German 4G Spectrum Auction: Design and Behaviour.”](http://www.cramton.umd.edu/papers2010-2014/cramton-ockenfels-german-4g-auction.pdf)
Oxford University Press Oxford, UK.

Synopsis:
Analysis of German auction in 2010 which was competitive due to lack of
(or too many) Schelling points.
Specifically there were different ways to divide up the blocks that might have
made sense depending on factors such as future mergers or network sharing
agreements and bidders worked towards conflicting outcomes.

