# Research methods: a small, reusable toolbox

Load only for a concrete analytic or experimental design need. **Pick methods by what they can reveal**, not by method name or a fixed checklist. Most cases need one well-chosen analysis, not every method in this document.

## 1. Analyze a phenomenon

Three complementary *views* (not mandatory steps):

| View | Question | Example |
| --- | --- | --- |
| **Contrast** | Relative to what did behavior change? | baseline vs proposed model; train vs validation; before vs after |
| **Horizontal slicing** | Which subsets, conditions, or failure types carry the difference? | object size, class, lighting, domain, error type |
| **Longitudinal / layer-wise tracing** | At what stage or time does the difference emerge? | decoder-layer predictions, learning dynamics, intermediate pipeline outputs |

Distinguish **observing a failure location** from **inferring its cause**. A low final classification score might reflect an upstream representation issue, insufficient supervision, or filtering downstream.

For layer-wise decoder analysis, compare consistent objects/queries or matching criteria where possible, e.g. box geometry, matching quality, class scores, recall by layer and target scale. Do not interpret raw attention visualizations or intermediate scores as a causal explanation on their own.

## 2. Develop an explanation

If the symptom is concrete but the mechanism unclear:

- Draw only the system segment relevant to this symptom: input → relevant transformations → intermediate signals → output or decisions.
- Use basic constraints/first principles, known mechanisms, analogy, and abductive reasoning to derive **one or a few grounded hypotheses**. First principles are a reasoning approach, not an experimental tool that must always be invoked.
- For each active hypothesis, ask: *If it were important, what observable differences would we expect?*
- Choose the next observation or intervention that could make competing explanations predict different outcomes, when feasible.

A provisional mechanism is enough when it is supported sufficiently to guide an informative next experiment. Seeking the “ultimate root cause” is not automatically required.

## 3. Design a discriminating experiment

Minimum design content, expressed briefly rather than in a form:

1. **Question:** what specifically is unknown?
2. **Change and comparison:** what will vary; what must remain comparable?
3. **Measure:** what data or metric directly reflects the proposed mechanism?
4. **Prediction:** what would support, weaken, or redirect the active hypothesis?
5. **Decision:** what will the researcher do differently after each material outcome?

Prefer a single interpretable contrast. Include a stronger alternative only when the choice would change the meaning of results or there is a distinct trade-off. Pre-experiment evaluation of a hypothesis should be limited to obvious flaws; experimental evidence should do the substantive work.

**Ablation** is an intervention/controlled comparison, not a fourth phenomenon-analysis viewpoint. Analyze an ablation with the three views above if useful. Ablations can support attribution to a component under comparable conditions; they do not automatically establish the internal mechanism of an improvement.

**Causal language:** an observed association, diagnostic trace, and intervention support different claims. Give the strongest conclusion the particular evidence justifies; neither overstate nor bury it under generic caveats.

## 4. Explore without a defined problem

Start from existing results when possible. If the model works but there is no promising question, consider an exploratory experiment designed to reveal a behavior boundary or hidden trade-off: controlled shifts in input scale, noise/occlusion, domain, sample density, computational budget, or another task-relevant condition. Choose the dimension based on the actual research goal—not a canonical benchmark checklist.

A good exploratory test can reveal a surprising contrast **or** establish that performance is stable in a condition. Surface several materially different findings to the researcher without flooding them with plots. The researcher chooses what to pursue.

## 5. When results are disappointing

Ask first **what kind of mismatch** occurred:

- Non-learning or unstable training: target the data/loss/optimizer/gradient path; consider fitting a tiny subset or a single batch to test whether learning is possible in a controlled setting. Success on the tiny subset does **not** prove generalization is the only remaining issue, and loss need not literally reach zero in all tasks.
- Good training fit, poor held-out results: inspect data splits, preprocessing, evaluation consistency, distribution change, and subgroup errors as suggested by evidence.
- Correct global metrics, bad local behavior: examine per-group predictions and output-to-ground-truth comparison.
- New method underperforms baseline: compare exactly what changed; use a targeted rollback or ablation before stacking more modules.

This is **conditional troubleshooting**, not six required checks. Do not classify every surprising result as a bug. Distinguish a reproducibility failure, a model limitation, and a new scientific signal.

## 6. After the test

Have the AI report the material observations accurately, invite the researcher's interpretation when useful, and then state what changed in the hypothesis space. If unexpected patterns emerge, name them without selling them as discoveries prematurely. Continue, reframe, test an alternative, or set aside a path according to likely information value, user resources, goals, and taste; avoid fixed retry budgets.

## 7. Cost and execution

Resources are user-relative. Ask about hardware, budget, time, and acceptable expenditure only when unknown constraints change the design. When recommending a cheaper pilot, explain what its result can and cannot establish. A cheap but uninformative test is not “minimum sufficient.” Implement experiments with whatever runtime and tools are actually present; never invent observations or imply an unrun experiment was executed.