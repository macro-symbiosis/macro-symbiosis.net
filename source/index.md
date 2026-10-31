# macro-symbiosis

This site holds a research framework under open development. It has three parts:

* **The spine:** a mathematical specification ([companion `r10`](spine/foundational-manifold-companion-2026-10-20-r10.md); the equations themselves in [`r7`](spine/foundational-manifold-2026-10-20-r7.json)), with a [verification script](spine/r10_branch2_witness_check.py) that checks its internal consistency.
* **The corpus:** [guidance](corpus/aperture_generation_guidance.md) and five tiers of *apertures*. Each aperture maps the working concepts of one discipline or tradition onto the spine. Every such mapping is a hypothesis, not a finding.
* **The [protocol](corpus/empirical_validation_protocol.md):** how the main hypothesis, $H_1$, is to be tested. In brief: do independent AI models, conditioned on the spine and corpus, agree when they analyse data they have not seen?

## What is claimed, and what is not

The protocol (§0) separates three kinds of claim:

* **Verified:** the internal consistency of the spine, and only to the extent of the checks recorded in the companion (§5). The verification script runs on every change.
* **Testable hypotheses:** $H_1$ and the predictions of Stages II–IV. **None of them has been tested yet.**
* **Not claimed:** anything about consciousness, its evolution or trajectory, or what the framework brings about.

The framework may be used as a working language for design and practice before it is tested. That use is legitimate in its own terms, but it is not evidence. Exploratory work, which is open and local, is kept separate from confirmatory studies, which are blinded and pre-registered. Exploratory results are never presented as confirmation.

## How it is developed

The spine and corpus are written with AI models and audited by fresh model sessions that have seen no earlier discussion, following Stage I of the protocol. What appears here is a snapshot of a private working repository; the [status page](status.md) says what each part has passed. Material that must stay hidden from the models that will evaluate the framework is not published.

Texts are licensed CC BY-SA 4.0 and code MIT; see [Licence](licence.md).
