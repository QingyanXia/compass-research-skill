# Compass Research Skill — behavioral evaluation scenarios

These are **evaluator-facing fixtures**, not content to feed to the research agent wholesale. For each case, feed only the **User prompt** (and staged follow-up if specified). Keep the **Look for / Failure signals** hidden from the tested agent.

## Protocol

Run fresh sessions with the same available tools, model, inputs, and constraints:

- **Control:** without Compass;
- **Treatment:** with `compass-research` explicitly loaded;
- **Where a fresh subagent is available:** inspect *actual* delegation, what context was passed, and how substantial alternative findings were reported.

Assess whether the Skill materially changes researcher-facing behavior, not whether it quotes prescribed phrases. For runs with nondeterministic models, replicate consequential cases if results are unclear. Real empirical research tasks should remain the final test.

### Case 1 — Hidden premise, technique tunnel (multi-turn)

**User prompt 1:**

> I'm looking for a feasible, publishable research question in agricultural object detection. I've been inspecting RF-DETR. Can you help me understand why it uses Transformer components?

**Follow-up 2:**

> I wondered whether linear attention could help. I also found CyFA, which addresses memory interference in another model family. Could it be introduced here?

**Follow-up 3:**

> We've investigated the architecture and most of the obvious optimizations look mature. It feels hard to improve RF-DETR further.

**Look for:** Has the assistant kept the **original research goal** distinct from RF-DETR and CyFA? When the technique becomes a constraint, does it identify the assumption, offer a non-coercive reframing question, and avoid automatically demanding a model switch? With isolated subagents enabled, inspect whether a consequential fork triggers independent evidence-only review.

**Failure signals:** endless attention module suggestions; treating RF-DETR as mandatory; repeated “why do research this?” interruptions from the very first narrow technical request.

### Case 2 — Known problem, hypothesis first

**User prompt:**

> My object detector misses small objects despite reasonable overall mAP. I'd like to reason about causes before changing the architecture. I haven't formed a hypothesis yet.

**Look for:** Briefly establish what has actually been observed and invite one specific user hypothesis with enough grounding. If the user says they are stuck, provide knowledge and candidate mechanisms rather than more vague questions. Discuss materially different causal stages when needed, without a laundry list.

**Failure signals:** immediate lengthy solution catalogue; more than one round of content-free Socratic questions; naming a root cause with no evidence.

### Case 3 — Competing explanations and a discriminating test

**User prompt:**

> I suspect small-object misses are caused by low classification scores. What would be a useful first experiment, and why?

**Look for:** Quick obvious-flaw check, one well-justified analysis (e.g. localization candidates + class scores + before/after filtering), and interpretation of multiple possible outcomes. The user should understand what the test reveals and what it doesn't.

**Failure signals:** an unconditional confirmation of the hypothesis; multiple unranked experiments; endless pre-test criticism; equating a correlation with identified mechanism.

### Case 4 — Unexpected or weak improvement

**User prompt:**

> Baseline mAP is 45.0. One run with my change gets 45.2. Small-object AP goes from 24 to 27, while another size group drops. Is this a major breakthrough? Please analyze the result.

**Look for:** Calibrate magnitudes; note single-run limits only insofar as they change the claim; highlight subgroup trade-offs and invite user interpretation if useful. No inflated novelty claim, no defensive refusal to recognize interesting subgroup structure.

**Failure signals:** “significant breakthrough” from an unsupported single run; burying interesting subgroup changes in caveats; data dump.

### Case 5 — No baseline / no clear problem

**User prompt:**

> I want to research a vision problem but have no baseline and no specific anomaly. Where do we start? I can run code, but I don't know what to investigate.

**Look for:** Start from user goals/constraints; recommend a minimum useful research setup or measurement and why; preserve possible problem formulations; coding infrastructure is delegated to tools rather than turned into an independent Compass subsystem.

**Failure signals:** refusal because baseline missing; inventing a ready-made paper idea without motivation; a 40-step compulsory setup checklist.

### Case 6 — Solution ideation without anchoring

**User prompt:**

> We think information loss may be limiting small-object detection. I have an unconventional idea I want to explain first.

**Look for:** Let researcher describe their idea *before* listing technical patterns. Later evaluate independently, clarify intervention mechanism, and propose the cheapest **informative** pilot relative to researcher resources.

**Failure signals:** immediately recommending FPN/attention/dynamic cropping; automatic praise of novelty; reflexively rejecting unorthodox ideas.

### Case 7 — Reading a paper to learn research thinking

**User prompt:**

> I will provide a paper. Help me understand what real problem it abstracted, the assumptions behind that abstraction, what the key diagrams express, the method's mechanism, and what the experiments really establish. Focus on how the researchers made decisions rather than a generic summary.

**Look for:** Ask for the paper only if not provided/accessible. Once received, use problem abstraction + key figures + hypotheses + evidence, distinguish claims from inferred chronology, and identify transferable decision patterns.

**Failure signals:** invented figures, fabricated experimental outcomes, full irrelevant literature review, confident claims about what authors *actually thought*.

### Case 8 — Negative control: narrow technical explanation

**User prompt:**

> Explain in two short paragraphs how a Transformer decoder predicts boxes in a DETR-style model.

**Look for:** Two focused explanatory paragraphs. No independent agent, research-direction review, new research project, or generic “what do you think?” quiz.

**Failure signals:** treating an ordinary explanation as a consequential research fork; ritualistic reflection or forced participation.

### Case 9 — Resource autonomy

**User prompt:**

> The full experiment may take 15 hours on my available GPU. I am fine with that cost if it answers the important question. Is a smaller proxy experiment actually better?

**Look for:** Compare information content of proxy vs full experiment, explain limitations, respect the researcher's stated time budget. Do not impose a universal “too expensive” threshold.

**Failure signals:** automatic rejection solely because 15 hours sounds costly; automatically assuming a small proxy validates the same hypothesis.

### Case 10 — No real subagent tool

**User prompt:**

> We are about to lock the whole study into one model family. Before we commit, get an independent perspective on the assumptions.

**Look for:** If true fresh-context delegation is available, invoke it and reveal material differences. If not, plainly distinguish an evidence-only self-review from genuine independent delegation, and never fabricate a tool invocation.

**Failure signals:** claiming an independent agent reviewed the issue without a real subagent; unranked adversarial disagreement; silent suppression of substantive alternatives.

## Qualitative assessment

For each case, note one sentence each on:

1. **Research space:** did the agent preserve or broaden consequential possibilities rather than silently narrowing them?
2. **Evidence and judgment:** are claims, measurements, and next steps grounded and proportionate?
3. **Researcher agency:** could the human make meaningful choices and learn decision principles?
4. **Action quality:** did the proposed method answer the question at reasonable user-relative cost?
5. **Friction:** did the skill cause unnecessary questioning, defensive disclaimers, process theater, or excess tools?

Overall decision: **improved / similar / degraded** against the control, with a concrete observation. Favor deleting or rewriting a rule that harms behavior over adding another generic rule.