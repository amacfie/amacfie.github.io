---
layout: post
title: "Data from Canadian 700MHz and 2500MHz spectrum auctions"
---

The 700MHz (2014) and 2500MHz (2015) spectrum auctions generated revenues of
5,270,636,002 CAD from 302 licenses and 755,371,001 CAD from 97 licenses.
Both
auctions used a combinatorial clock auction (CCA) format involving an
ascending clock phase followed by a sealed-bid supplementary stage where
bids could be made on packages of products.
Final prices were determined
using Vickrey pricing with a core-adjustment. An activity
rule was used which required bidders to make bids or lose eligibility to
bid in later clock rounds, along with a revealed preference rule which
allows the eligibility limit to be exceeded as long as consistency
checks are satisfied. For full details on the auction formats see the
official documentation
([700MHz rules](http://www.ic.gc.ca/eic/site/smt-gst.nsf/eng/sf10573.html#p4),
[700MHz additional details](http://www.ic.gc.ca/eic/site/smt-gst.nsf/eng/sf08697.html),
[2500MHz rules](http://www.ic.gc.ca/eic/site/smt-gst.nsf/eng/sf10726.html#p4));
and the record of bids placed is [here](http://www.ic.gc.ca/eic/site/smt-gst.nsf/eng/sf11085.html)
for 700MHz and
[here](http://www.ic.gc.ca/eic/site/smt-gst.nsf/eng/sf11170.html)
for 2500MHz.


*Bid consistency*

The revealed preference rule prevents some inconsistent behavior but not all.
By "truthful", we mean bids that are true indications of subjective value,
and by "consistent" we mean bids that are indications of some fixed set of
valuations, possibly not the bidder's actual valuations.

The following table gives the values of Afriat’s critical cost
efficiency index (CCEI) for the 700MHz auction. Recall
that for a CCEI value $$x$$, if $$x < 1$$ there is at least some
intransitivity in preferences (i.e. inconsistent bidding) and $$1-x$$ can be
interpreted as the fraction of expenditure wasted making inefficient
choices (see [this](http://eml.berkeley.edu/~kariv/CFGK_III_A3.pdf)
by S. Kariv for more).

Bidder | CCEI (clock rounds) | CCEI (clock and supp. rounds)
|-
Bell      | 0.930 | 0.417
Bragg     | 0.880 | 0.420
Feenix    | 1     | 1
MTS       | 0.996 | 0.627
Novus     | 1     | 1
Rogers    | 0.998 | 0.742
SaskTel   | 1     | 1
TBayTel   | 1     | 1
Telus     | 0.970 | 0.488
Videotron | 0.879 | 0.560

[Kroemer et al.](https://link.springer.com/article/10.1007/s10726-015-9431-0)
conclude for the 700MHz auction, “the
numbers suggest that bidders deviated substantially from straightforward
bidding” in the clock rounds. But “it is not unreasonable to believe
that bidders tried to bid up to their true valuation in the
supplementary stage” because of higher bid amounts compared to the clock
rounds.

The next table gives CCEI values for the 2500MHz
auction. We extend the definition of CCEI to apply to supplementary bids
as in Kroemer's paper.

Bidder | CCEI (clock rounds) | CCEI (clock and supp. rounds)
|-
Bell      | 0.913 | 0.712
Bragg     | 0.920 | 0.530
Corridor  | 1     | 1
MTS       | 1     | 1
Rogers    | 1     | 1
SSi Micro | 1     | 1
TBayTel   | 1     | 1
Telus     | 0.997 | 0.996
Videotron | 1     | 1
WIND      | 1     | 1
Xplornet  | 1     | 0.578


Kroemer et al. (Sec. 5.2) also point out that the
total number of bids submitted in the 700MHz auction was much smaller
than the number of possible bids, which probably indicates untruthful
bidding since an omitted
package must have valuation less than or equal to its (low) opening price.
The same observation holds for the 2500MHz auction. More exactly, the
auction formats enforced a limit on the number of packages bidders were
allowed to submit, which was in the hundreds, and bidders generally did
not reach the limit.

Ideally, we would determine whether the bids made are consistent with a
non-truthful strategy incorporating gaming and/or coordination.
It is not clear that this is feasible using available models.
Adding a lexicographic preference
for raising rivals’ costs, [Janssen and Karamychev](https://papers.tinbergen.nl/13027.pdf)
show that the Vickrey-Clarke-Groves mechanism does not
have dominant strategies.
Prop. 4 in their paper claims that under
certain conditions bidders will try to prolong the clock stage: “if
other bidders do not change their bids if the clock phase lasts one more
round, then the bidder under consideration prefers to prolong the clock
phase by one round”. The bidder does this by delaying its “switch” from
a parked non-final package that causes excess demand, to the final
package which does not.
However, the conditions under which Prop. 4 holds will not be exactly satisfied
in any real auction.


*Bids, budgets, and final prices*

Bidders may have a notion of a budget – the maximum they are willing to
spend. But how should this correspond to the maximum they should bid? In
general, bidders may end up paying the exact amount of their highest
bid, but looking at the data we see bid prices and final prices can be
very different in practice.
The following tables show figures from both auctions that illustrate this
difference.
All prices are given in CAD.

700MHz auction: highest bid placed.
Average ratio: 0.192. Max ratio: 0.766.

Bidder | Max bid ($$M$$) | Allocation stage final price ($$p$$) | Ratio ($$p/M$$) | Final clock bid
|-
Bell      | 3,999,999,000 | 565,705,517   | 0.141 | 1,366,867,000
Bragg     | 141,894,000   | 20,298,000    | 0.143 | 38,814,000
Feenix    | 60,650,000    | 284,000       | 0.005 | 346,000
MTS       | 73,067,000    | 8,772,072     | 0.120 | 10,853,000
Novus     | 112,359,000   | 0             | 0     | 0
Rogers    | 4,299,949,000 | 3,291,738,000 | 0.766 | 3,931,268,000
Sasktel   | 75,000,000    | 7,556,929     | 0.101 | 11,927,000
TbayTel   | 7,683,000     | 0             | 0     | 0
Telus     | 3,750,000,000 | 1,142,953,484 | 0.305 | 1,313,035,000
Videotron | 677,524,000   | 233,328,000   | 0.344 | 468,530,000


<br />
700MHz auction: (highest) bid placed on package eventually won.
  Average ratio: 0.447. Max ratio: 0.766.

Bidder | Max bid on won package ($$W$$) | Allocation stage final price ($$p$$) | Ratio ($$p/W$$) | Allocation stage Vickrey price
|-
Bell      | 2,583,868,000 | 565,705,517   | 0.219 | 565,705,000  
Bragg     | 51,000,000    | 20,298,000    | 0.398 | 20,298,000   
Feenix    | 425,000       | 284,000       | 0.668 | 284,000      
MTS       | 40,000,000    | 8,772,072     | 0.219 | 3,198,000    
Novus     | N/A           | 0             | N/A   | 0 
Rogers    | 4,299,949,000 | 3,291,738,000 | 0.766 | 3,291,738,000
Sasktel   | 62,400,000    | 7,556,929     | 0.121 | 2,755,000
TbayTel   | N/A           | 0             | N/A   | 0
Telus     | 1,607,300,000 | 1,142,953,484 | 0.711 | 1,142,953,000
Videotron | 490,000,000   | 233,328,000   | 0.476 | 233,328,000


<br />
2500MHz auction: highest bid placed.
  Average ratio: 0.135. Max ratio: 0.277.

Bidder | Max bid ($$M$$) | Allocation stage final price ($$p$$) | Ratio ($$p/M$$) | Final clock bid
|-
Bell      | 542,746,000   | 28,730,000  | 0.053 | 76,214,000   
Bragg     | 35,935,000    | 4,821,021   | 0.134 | 12,091,000   
Corridor  | 9,300,000     | 2,299,000   | 0.247 | N/A          
MTS       | 13,609,000    | 2,242,000   | 0.165 | 2,609,000    
Rogers    | 304,109,000   | 24,049,546  | 0.079 | 52,343,000   
SSi Micro | 851,000       | 0           | 0     | 0            
TBayTel   | 12,001,000    | 1,731,000   | 0.144 | 1,731,000    
Telus     | 1,771,723,000 | 478,819,000 | 0.270 | 1,038,472,000
Videotron | 749,128,000   | 66,552,980  | 0.089 | 231,851,000  
WIND      | 22,609,000    | 0           | 0     | 0            
Xplornet  | 91,974,000    | 25,472,454  | 0.277 | 57,839,000   


<br />
2500MHz auction: (highest) bid placed on package eventually won.
  Average ratio: 0.235. Max ratio: 0.410.

Bidder | Max bid on won package ($$W$$) | Allocation stage final price ($$p$$) | Ratio ($$p/W$$) | Allocation stage Vickrey price
|-
Bell      | 536,563,000   | 28,730,000  | 0.054 | 28,730,000 
Bragg     | 19,000,000    | 4,821,021   | 0.254 | 3,536,000  
Corridor  | 6,440,000     | 2,299,000   | 0.357 | 2,299,000  
MTS       | 11,000,000    | 2,242,000   | 0.204 | 2,242,000  
Rogers    | OR            | 24,049,546  | N/A   | 21,252,000 
SSi Micro | N/A           | 0           | N/A   | 0          
TBayTel   | 12,001,000    | 1,731,000   | 0.144 | 1,731,000  
Telus     | 1,771,723,000 | 478,819,000 | 0.270 | 478,819,000
Videotron | 358,477,000   | 66,552,980  | 0.186 | 61,092,000 
WIND      | N/A           | 0           | N/A   | 0          
Xplornet  | 62,200,000    | 25,472,454  | 0.410 | 22,917,000 


Across both auctions, we see that bidders paid an average of 16% of
their maximum bid placed, where each bidder is equally weighted.


*Misc. notes*

Researchers design approximation algorithms for winner and price
determination in auctions (in e.g. [this paper](https://projecteuclid.org/download/pdf_1/euclid.im/1089229504))
because exact
optimization can be intractable as the number of bids grows, at least in
the worst case. However, in these recent auction instances, theoretical
intractability did not present a problem because the solution was
computable in a small amount of time.
The 2500MHz allocation stage involved 2,239 bids and a
GLPK-powered solver finds the winners and final prices in a couple
minutes on a standard computer.
Simulations involving well over 30,000 random bids still take a feasible amount
of time.

In the 2500MHz auction, there were 4 pairs of package submissions where
the lower-priced package had strictly higher quantities of products.
In this case the lower-priced package is superfluous.
This table shows the packages, submitted by Bell.

| | Price of larger package (CAD) | Price of smaller package (CAD) | Number of products difference
|-
1 | 535,917,000 | 536,214,000 | 3
2 | 536,628,000 | 536,645,000 | 3
3 | 536,401,000 | 536,545,000 | 3
4 | 536,434,000 | 536,563,000 | 3


*Acknowledgement*: Thanks to Z. Gao for pointers.

