# Compass Research Skill

> **Beyond answers. Discover the questions worth asking.**
>
> **不止于寻找答案，更要发现值得追问的问题。**

**发现问题，审视前提，设计实验，让证据推动研究。**

Compass 是一个以研究者为主导的 AI 科研协作 Skill。它帮助你从实验现象中发现问题，从数据与机制中寻找解释，将想法转化为可验证的实验，并在研究过程中持续拓展自己的视野与判断能力。

[English](README.md)

## 从实验结果走向真正的研究

### 发现值得研究的问题

从一组实验结果、一个已复现的模型、一个异常现象，甚至一个尚未成形的研究念头出发。

Compass 主动比较数据、拆解指标、追踪过程，让隐藏在整体结果中的差异、规律和潜在问题浮现出来。

### 理解现象背后的机制

通过对照比较、横向分解、纵向追踪、机制推演与针对性干预，逐步缩小原因范围。

它关注的不只是哪里表现不好，更是**什么因素正在限制结果，以及什么证据能改变我们的判断**。

### 把假设变成有价值的实验

从研究者的直觉出发，推导可观察的预测，选择能够区分关键解释的实验。

Compass 不只告诉你“做什么”，还会说明**为什么值得做、不同结果意味着什么、下一步该如何决定**。

### 保护真正开放的探索空间

**模型是工具，方法是候选，问题框架本身也是可以重新选择的。**

当某项技术逐渐取代原始目标、研究陷入既有假设时，Compass 会主动审视隐含前提。在支持子智能体的运行环境中，关键方向分叉还可以引入隔离上下文的独立视角。

### 让原创想法得到认真对待

你可以先自由表达直觉、联想和不成熟的想法。

随后，Compass 利用领域知识与实验证据独立评价，帮助寻找作用机制、补充不同可能性，并把想法推进到最小充分验证。

**对创造保持开放，对判断保持独立，对证据保持忠实。**

### 从论文中学习如何做研究

阅读论文时，不止于复述模型结构和指标。

Compass 帮助你理解作者如何将现实问题抽象为研究问题，如何提出假设、选择技术路线、解释关键图表，以及通过实验支撑研究结论。

把别人的研究转化为自己的研究能力。

## Researcher-First：研究者始终处于中心

Compass 采用一条精简、稳定的科研决策循环：

```text
研究目标 + 已有证据
          ↓
      阶段性判断
          ↓
    最有价值的下一步
          ↓
    分析 / 实验 / 探索
          ↓
       新证据
          ↓
       更新判断
```

**探索保持开放，行动保持聚焦，方向由研究者决定。**

AI 发挥信息处理、实验分析、知识整合和执行能力；研究者保留自己的直觉、思考、兴趣与科研品味。

Compass 以准确、简洁的方式呈现结果，让证据强度与结论力度匹配。它帮助研究者看见不同的道路，也帮助研究者理解为什么选择下一步。

## 安装

**可以直接让你的 AI Agent 安装 Compass，无需手动执行命令。**

在 **Codex** 或 **Claude Code** 中复制并发送以下提示词：

```text
请帮我安装 Compass Research Skill：
https://github.com/QingyanXia/compass-research-skill

直接执行安装。识别当前使用的 Agent（Codex 或 Claude Code），从仓库获取 compass-research/ 文件夹，安装到对应的用户级 Skills 目录，并保留其中的 SKILL.md 和 references/。

安装完成后，确认文件完整，告诉我安装路径、调用方式，以及是否需要重启 Agent 才能识别。
```

### 手动安装（可选）

Compass 遵循 [Agent Skills 格式](https://agentskills.io/specification)。安装包含 `SKILL.md` 的 `compass-research/` 目录即可。

**Codex**

```bash
git clone https://github.com/QingyanXia/compass-research-skill.git
mkdir -p ~/.agents/skills
cp -R compass-research-skill/compass-research ~/.agents/skills/
```

使用 `$compass-research` 调用。项目级安装可放在 `<项目>/.agents/skills/`。

**Claude Code**

将 `compass-research/` 复制至 `~/.claude/skills/` 或 `<项目>/.claude/skills/`，使用 `/compass-research` 调用。

## 开始探索

```text
$compass-research 我复现了一个目标检测模型，指标基本正常，
但不知道还有什么值得研究的，请帮我主动寻找问题。

$compass-research 我发现小目标漏检比较严重。
先给我必要的信息，我想自己尝试提出原因假设。

$compass-research 新方法的实验结果不如 Baseline。
先告诉我数据揭示了什么，再一起分析下一步。

$compass-research 我们一直在优化这个模型，
但好像忘了最初为什么选择它。帮我重新审视问题框架。
```

## 设计理念

**最小稳定内核，按需扩展能力。**

[`SKILL.md`](compass-research/SKILL.md) 负责科研判断与协作机制；[`references/`](compass-research/references/) 提供按需使用的诊断、文献与独立视角能力。

我们希望 Compass 的研究能力持续进化，同时始终保持简洁。

## 开源许可

[MIT License](LICENSE)。
