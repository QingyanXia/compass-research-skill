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
- Give the agent an **evidence-only packet**: the original research goal, confirmed observations, essential experimental setup, data/measurements, and **genuine researcher-defined constraints**. Distinguish these from the current model or technique, which may be useful existing work but is not automatically mandatory.
- Withhold the lead agent's favored causal hypothesis, proposed implementation, and draft conclusion **unless one is itself an essential fact**. Do not conceal contradictory evidence. If the current model is relevant context, identify it as **currently explored, not fixed**.
- Ask an independent question such as:

> From the original goal and these facts, identify the key assumption that currently narrows the research direction. **Temporarily remove that assumption**: is there a credible, materially different path to the same goal without requiring the current model, technique, or problem framing? Compare it with continuing the present route. Preserve actual user constraints, distinguish evidence from conjecture, and do not force an alternative if none is credible. Return only the consequential choice and its basis.

- **A variant within the contested premise does not count as an independent frame.** For example, replacing architectural modification of one detector with another way of adapting that same detector may broaden methods, but does not test whether the detector itself must remain central.
- The review informs **researcher-facing choice**, not a hidden verdict. Present any credible premise-independent route **before** a detailed plan for the current route; explain the difference and your recommendation without silently folding it into that plan. The researcher chooses. If no consequential alternative emerges, do not invent one or dump the entire review.

## Platform portability and failure behavior

A Skill can **request** delegation but cannot guarantee the runtime supplies it. If no true isolated subagent tool is available, make an evidence-only reassessment yourself as a weaker fallback and do not claim an independent agent ran. State this when independence matters to the user's choice.

One subagent is the default; do not create standing critic agents, automatic debates, mandatory consensus, or routine logs. Persist a newly discovered research lead only if it materially matters later, using the existing research state.