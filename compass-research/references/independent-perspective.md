# Independent perspective at consequential forks

## Why

An apparently coherent sequence of local research decisions can silently shrink the original exploration space. The reviewer protects the researcher's chance to see **material alternatives and unstated assumptions**; it is not an adversarial critic, a novelty generator, or a committee.

## Trigger

Use **once** when an important decision might lock the project into a bottleneck, problem frame, model family, method, or abandonment of a meaningful path. Strong signals include:

- a candidate tool/model becoming an unexplained requirement;
- repeated attempts to fit a desired technique to a problem;
- technical optimization proceeding without a clear relation to the original goal;
- a consequential negative or surprising result that might deserve reframing;
- commitment of substantial user-valued resources to one interpretation.

Do not trigger because a normal experiment is difficult, the user requests a narrow explanation, or another subagent already reviewed the same unchanged decision.

## Use a genuinely isolated agent when supported

- Call the actual subagent/delegation tool exposed by the host runtime. Verify its available parameters. For systems that support a fresh-history setting (e.g. `fork_turns: none`), use it. Do not invent invocation syntax.
- Give the agent an **evidence-only packet**: the original research goal, confirmed observations, essential experimental setup, data/measurements and constraints.
- Withhold the lead agent's favored causal hypothesis, implementation, and draft conclusion **unless one of those is itself a factual part of what must be analyzed**. Do not conceal contradictory evidence.
- Ask an independent question such as:

> From only these facts and the original research goal, identify any materially different plausible problem framings, mechanisms, or investigation paths that deserve the researcher's awareness. Distinguish evidence from conjecture. Identify an implicit assumption if one is shaping the apparent problem. Do not force disagreement, invent options, rank interests on the researcher's behalf, or write a long survey. Return only consequential insights and a possible discriminating observation.

- Subagent return is input to researcher-facing choice, **not a hidden final verdict**. When it reveals a materially different problem framing or research direction, explicitly show the difference as a **separate, intelligible option**, with the evidence that makes it consequential. Do not silently convert an alternative direction into minor improvements to the existing plan. The lead agent can recommend one route and one next action; the researcher chooses. If no consequential alternative emerges, do not invent one or dump the whole review.

## Platform portability and failure behavior

A Skill can **request** delegation but cannot guarantee the runtime supplies it. If no true isolated subagent tool is available, make an evidence-only reassessment yourself as a weaker fallback and do not claim an independent agent ran. State this when independence matters to the user's choice.

One subagent is the default; do not create standing critic agents, automatic debates, mandatory consensus, or routine logs. Persist a newly discovered research lead only if it materially matters later, using the existing research state.