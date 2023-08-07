---
layout: post
title: "Mathematics as a service"
---

What would a market for mathematics look like?

Formal verification might allow an elegant mechanism:
Someone posts a proposition in a formal language like Coq and the first
to submit a proof that passes verification wins the bounty.
Everything can be automated and maybe even trustless.
This has been tried, at proofmarket.org, which was [shut
down](https://medium.com/@pirapira/ten-ethereum-related-pending-projects-you-could-take-c828a2dce88e)
due to consistency bugs in the verifier.
Even without bugs, proof assistants are still difficult to use;
mathematician Thomas Hales [says](https://jiggerwit.wordpress.com/2018/09/18/a-review-of-the-lean-theorem-prover/)
"It is very hard to learn to use [Lean](https://leanprover.github.io/)
proficiently. Are you a graduate student at Stanford, CMU, or Pitt writing a
thesis on Lean? Are you a student at Imperial being guided by Kevin Buzzard?
If not, Lean might not be for you."

If we stick to natural language to avoid the learning curve, things get messy.
How does the market decide what a complete proof is, which proof is first, and
who did it? Perhaps the only tenable solution is to leave these decisions
up to the individuals who post the bounties. How would we
know that bounties would ever get paid? Stack Exchange forces bounties to be
put in escrow and if they're not awarded to someone there's no refund. Another
option is to rely on reputation by using certified identities (e.g. users'
email addresses are verified and
[public](https://www.gtricks.com/google/hide-email-address-online-recaptcha-tool/)
so they can be checked against personal webpages).

Something along these lines might be doable (and if someone wants to build it
I'll donate the domain proofbounty.com) but what's the use case?
Monetary rewards for mathematical problems are [rare](https://mathoverflow.net/questions/66084/open-problems-with-monetary-rewards)
and mathematicians generally already earn a salary, so the interest would
likely be modest.
Students (anywhere in the world) are plausible suppliers though, perhaps
even [high school students](https://www.imo-official.org/results.aspx),
while consumers could be anyone with a research grant usable for paying
"research assistants", or industry and non-profit research groups.
A market that brings these two sides together could be of some value.

Paid question answering has been tried before, e.g.
[Google Answers](http://answers.google.com/answers/browse/1707.html) which
wasn't very popular.
Did it fail due to lack of network effects,
lack of [innovative mechanisms](https://thenextweb.com/us/2010/07/09/will-you-pay-to-comment-online/),
or an essential flaw in the concept? I don't know.
[Bounties](https://www.bountysource.com/) [on](https://gitstart.com/)
GitHub issues seem to be a bit more successful.

In addition to bounties, there could be a prediction market.
The time of resolution may have to be indefinite, though, since
resolving "proposition X will be publicly proved by date Y" would in general
require determining the nonexistence of a public proof, which is at least
somewhat error-prone.
However, prediction markets are basically illegal so it's a moot point.

