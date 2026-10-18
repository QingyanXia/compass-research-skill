# Compass Research Skill

> **Beyond answers. Discover the questions worth asking.**

**Discover the problem. Challenge the assumption. Design the experiment. Follow the evidence.**

Compass is an AI research skill built around a simple conviction: **the most valuable research partner expands what you can discover—and strengthens your ability to decide what to pursue.**

From a puzzling experiment to a new research direction, Compass helps you explore questions, diagnose mechanisms, test hypotheses, develop solutions, and learn how strong research is built.

[简体中文](README.zh-CN.md)

## From results to research

### Discover what matters

Start with a research idea, a working baseline, unexpected results, or just a phenomenon worth exploring. Compass analyzes behavior across conditions, cases, and stages, then brings forward the observations worth your attention.

### Understand what is happening

Move from symptoms to explanations. Use targeted comparison, subgroup analysis, process tracing, first-principles reasoning, and carefully chosen interventions to locate meaningful bottlenecks.

### Turn ideas into evidence

Make hypotheses testable. Compass helps design experiments that distinguish possible causes, explains **why an experiment is worth running**, and uses both expected and surprising results to update the next move.

### Keep the possibility space open

A model is a tool. A method is a candidate. A framing is a choice.

Compass pays attention to hidden assumptions and moments when a convenient technique quietly becomes the research goal. At consequential forks, it can bring in an independent perspective through a context-isolated subagent in supported environments.

### Create with independent judgment

Your intuition comes first when you want to explore an idea. Compass then brings domain knowledge, honest evaluation, alternative mechanisms, and a focused way to test the core insight.

### Learn how research is made

Read papers through the decisions behind them: how the authors abstracted a real problem, formed hypotheses, designed methods, interpreted figures, and connected evidence to claims. Carry those ways of thinking into your own work.

## Researcher-first by design

Compass is organized around one small research decision loop:

```text
Research goal + evidence
        ↓
Working interpretation
        ↓
Most informative next action
        ↓
Experiment / analysis / exploration
        ↓
New evidence → updated judgment
```

**Open exploration. Focused action. Researcher-owned direction.**

AI handles wide-ranging analysis and purposeful execution; researchers bring questions, intuition, interpretation, and taste. Together, they move from observing an outcome to understanding what to investigate next.

Compass presents evidence in proportion to its strength. It surfaces useful differences without flooding the researcher with charts, and recommends a concrete next step without treating that recommendation as the only road.

## Install

**Install Compass directly through your AI agent—no manual terminal steps required.**

Copy and send this prompt to **Codex** or **Claude Code**:

```text
Install Compass Research Skill for me:
https://github.com/QingyanXia/compass-research-skill

Please perform the installation directly. Identify whether this environment is Codex or Claude Code, fetch the compass-research/ directory from the repository, and place it in the corresponding user-level Skills directory. Keep SKILL.md and the references/ folder intact.

After installation, verify the files and tell me the install path, how to invoke the skill, and whether the agent needs to restart to discover it.
```

### Manual installation (optional)

Compass follows the [Agent Skills format](https://agentskills.io/specification). Install the `compass-research/` directory containing `SKILL.md`.

**Codex**

```bash
git clone https://github.com/QingyanXia/compass-research-skill.git
mkdir -p ~/.agents/skills
cp -R compass-research-skill/compass-research ~/.agents/skills/
```

Invoke with `$compass-research`. For project-specific use, install the folder under `<project>/.agents/skills/`.

**Claude Code**

Copy `compass-research/` into `~/.claude/skills/` or `<project>/.claude/skills/`, then invoke `/compass-research`.

## Try Compass

```text
$compass-research I reproduced an object detector. The benchmark looks fine,
but I don't know what is worth investigating.

$compass-research Small objects are being missed.
Help me understand the evidence; I'd like to form my first hypothesis myself.

$compass-research My proposed method underperformed the baseline.
What did the experiment reveal, and what should we test next?

$compass-research We've spent days optimizing this model.
Let's check whether we've silently made the model itself our goal.
```

## Architecture

A **minimal, stable research kernel** coordinates on-demand methods. The skill lives in [`compass-research/SKILL.md`](compass-research/SKILL.md); focused references live in [`compass-research/references/`](compass-research/references/).

The core stays small. Its capabilities grow through better research judgment and reusable methods, rather than an ever-expanding collection of mandatory steps.

## License

[MIT](LICENSE).
