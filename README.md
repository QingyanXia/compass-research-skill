# Compass Research Skill

> **Beyond answers. Discover the questions worth asking.**

**Compass** is a researcher-first Agent Skill for scientific discovery, diagnosis, experimentation, and open-ended problem solving. Its purpose is not to automate papers or generate plausible-sounding ideas. It helps researchers **see more of the problem space, make evidence-based decisions, and develop independent research judgment**.

[简体中文](README.zh-CN.md)

## What Compass does

- **Discover problems** from existing results or deliberate exploratory experiments, even when no explicit research question or baseline exists.
- **Diagnose mechanisms** through comparison, subgroup analysis, process tracing, and focused interventions.
- **Turn hypotheses into tests** that generate useful evidence, including results that could weaken the hypothesis.
- **Develop solutions** without rushing to a familiar architecture or prematurely dismissing original human ideas.
- **Read literature for insight**: problem abstraction, hypotheses, decisive figures, methods, evidence, and transferable research reasoning.
- **Protect the exploration space** by recognizing hidden assumptions and, at consequential direction changes, asking a context-isolated subagent for an independent evidence-based perspective when available.

## Philosophy

**Minimal stable kernel, optional methods.** A single research decision loop supports many entry points:

`Goal and evidence → provisional judgment → informative next action → new evidence → updated judgment`

Methods are chosen for their usefulness, not run as a checklist. Domain techniques remain optional. The design favors a small core over ever-growing prompts, agents, hooks, and audit logs.

**Researcher-first, not blindly agreeable.** In ideation, the human gets room to think before the model suggests familiar solutions. During analysis, the model gives its own honest, evidence-grounded assessment. The researcher—not the AI—chooses the problems and directions worth pursuing.

**Open exploration, focused action.** The AI can recommend one next experiment while making material alternatives visible at meaningful forks. It neither buries evidence under defensive caveats nor inflates tiny metric differences into breakthroughs.

## How collaboration feels

| Moment | Default behavior |
| --- | --- |
| No defined research problem | AI explores evidence and designs targeted probes; researcher chooses which findings matter |
| Hypothesis formation | Researcher tries an explanation first; AI supplies knowledge or hypotheses when needed |
| Test design | AI recommends one informative experiment and explains why |
| Results | AI presents measured facts; researcher interprets; AI then independently analyzes |
| Solution creation | Researcher may freely propose ideas before exposure to known implementation patterns |
| Major direction fork | One fresh-context perspective check when supported; important alternatives reach the researcher |

These are adaptive defaults, not compulsory interview steps.

## Install

The skill follows the [Agent Skills open format](https://agentskills.io/specification). **Install the inner `compass-research/` folder**, which contains `SKILL.md`; the repository root is for distribution and testing.

For **Codex**, at user scope, from the downloaded package:

```bash
unzip compass-research-skill.zip
mkdir -p "$HOME/.agents/skills"
cp -R compass-research-skill/compass-research "$HOME/.agents/skills/"
```

Or, after the repository is published, clone and install:

```bash
git clone https://github.com/QingyanXia/compass-research-skill.git compass-research-skill
mkdir -p "$HOME/.agents/skills"
cp -R compass-research-skill/compass-research "$HOME/.agents/skills/"
```

For a single Codex project, copy that same folder into `<project>/.agents/skills/` instead. Then use `$compass-research` explicitly, or allow the runtime to discover it from the description.

For **Claude Code**, copy it into `~/.claude/skills/compass-research/` (or `<project>/.claude/skills/compass-research/`) and use `/compass-research`. Skills are portable, but **true isolated-subagent behavior depends on the host/runtime configuration**. When unavailable, Compass labels the weaker fallback rather than pretending it delegated.

Examples of usage:

- `$compass-research I reproduced a detector. The metrics look normal, but I don't know what is worth studying.`
- `$compass-research Small objects are missed. Help me locate the bottleneck; I want to form the first hypothesis myself.`
- `$compass-research My new method underperformed the baseline. What does the result actually tell us?`
- `$compass-research Let's challenge the assumptions behind choosing this model before committing to it.`

## Repository layout

```text
compass-research-skill/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── compass-research/
│   ├── SKILL.md                     # Small, complete decision kernel
│   └── references/                  # Loaded only for a relevant need
│       ├── methods.md
│       ├── literature.md
│       ├── independent-perspective.md
│       └── research-state.md
└── tests/
    ├── scenarios.md                # Blind and negative test cases
    └── validate_structure.py       # Standard-library format check
```

## Evaluation and status

This is a **full-scope v1.0 release candidate**, not a deliberately feature-reduced demo. The published package includes research discovery, diagnosis, hypothesis testing, solution design, literature reasoning, and independent perspective checks.

It includes a structural validator and an evaluator-facing test set. **Passing file validation is not evidence that the model behaves as intended.** Before marking a public release stable, run the scenarios in fresh model sessions with and without Compass, assess actual tool use at major forks, and refine only demonstrable failures. See [tests/scenarios.md](tests/scenarios.md).

Run structural checks:

```bash
python3 tests/validate_structure.py
```

## Scope and limits

Compass is optimized for AI/ML/CV research but keeps its decision logic applicable to empirical research more broadly. It does not ship model-training code, datasets, automated paper-writing pipelines, always-on multi-agent committees, mandatory runtime hooks, or permanent agent invocation logs.

A Skill is an instruction package. It cannot guarantee model correctness, exhaustive discovery, statistically valid inference, live tool availability, or autonomous independent review where the runtime does not provide one.

## License

MIT. See [LICENSE](LICENSE).
