# Compass Research Skill

> **Beyond answers. Discover the questions worth asking.**
>
> 不止于寻找答案，更要发现值得追问的问题。

**Compass** 是一个以研究者为主导的科研探索 Agent Skill。它帮助研究者**发现问题、诊断瓶颈、提出并验证假设、设计解决方案、学习论文中的研究思维**，同时保护独立判断与科研品味（Research Taste）。

[English README](README.md)

## 与一般科研 AI 工具的不同

Compass 不以“自动生成论文 Idea”或“自动完成论文”为主要目标。它关注的是：**当研究者面对不确定的实验现象时，如何获得新认识并决定下一步？**

- **发现问题：** 有数据时主动拆解指标、观察异常；没有明确问题时设计有目的的探索实验。
- **诊断问题：** 从现象出发，使用对照比较、横向分解、纵向追踪、机制推演与必要的干预实验，寻找阶段性解释。
- **验证假设：** 将直觉转化为可观察的预测，设计具有区分力的实验，并考虑什么结果会削弱原假设。
- **设计方案：** 研究者先自由表达想法，AI 再补充知识、独立评价和寻找最小充分验证；不盲目迎合，也不因不常见而轻易否定。
- **理解论文：** 学习作者如何将现实抽象成问题、提出假设、选择方法、使用图表与证据支持结论。
- **保护探索空间：** 在重要方向分叉时审视隐含前提；运行环境支持时，调用隔离上下文的子智能体重新分析原始事实。

## 核心哲学

**少即是多。** 核心只有一条科研决策循环：

`研究目标与证据 → 阶段性判断 → 最有信息价值的行动 → 新证据 → 更新判断`

主流程是参考而非必须依次完成的步骤。方法库只在当前需要时加载。我们不因为遇到一个新案例就增加一个新 Hook、新 Agent 或新的强制检查。

**探索开放，行动聚焦。** AI 可以优先推荐一项实验，但必须解释为什么选它；当有实质不同的重要方向时，让研究者看见，而不是悄悄筛掉。

**对创造保持开放，对判断保持独立，对证据保持忠实。** 创造阶段先让研究者形成不受技术清单锚定的想法；分析阶段 AI 给出真正独立的判断；验证阶段让结果说话。

**引导要有灵魂。** 提问是为了教会可迁移的判断方式，不是暴露用户不知道什么，更不是让用户猜 AI 预设的答案。缺少知识时主动解释和示范，不连续机械追问。

**准确表达，不防御也不夸张。** 小变化不能包装成重大突破；较强证据也不能被泛泛的“可能、未必、仍需验证”淡化。AI 应先简洁呈现事实，再引导用户解读，不倾倒大段数据与结论。

## 与研究者的默认分工

| 环节 | 默认协作方式 |
| --- | --- |
| 尚未发现问题 | AI 主动分析、探索；研究者选择关注什么 |
| 原因假设 | 研究者先尝试解释；AI 在需要时补充机制与假设 |
| 设计实验 | AI 推荐最有价值的一项，说明预期信息与判断依据 |
| 分析结果 | AI 先呈现关键事实；研究者解释；AI 再独立补充 |
| 方案构想 | 研究者先自由表达；AI 随后协助技术化和验证 |
| 重大研究分叉 | 尽可能使用隔离上下文的子智能体提供独立视角，保留研究者的方向选择权 |

以上是默认协作方式，不是强制问答流程。用户要求直接讲解、直接提出方案时，也应该直接提供。

## 安装

遵循 [Agent Skills 标准](https://agentskills.io/specification)。**安装的是内层 `compass-research/` 目录**，而不是整个 GitHub 仓库目录。

### Codex：个人范围

下载完整压缩包后：

```bash
unzip compass-research-skill.zip
mkdir -p "$HOME/.agents/skills"
cp -R compass-research-skill/compass-research "$HOME/.agents/skills/"
```

仓库公开发布后，也可以使用 Git：

```bash
git clone https://github.com/QingyanXia/compass-research-skill.git compass-research-skill
mkdir -p "$HOME/.agents/skills"
cp -R compass-research-skill/compass-research "$HOME/.agents/skills/"
```

单个 Codex 项目则复制至 `<项目>/.agents/skills/`。安装后可以直接使用 `$compass-research`，也可以由 Codex 按 Skill 描述自动选择。

### Claude Code

复制到 `~/.claude/skills/compass-research/` 或 `<项目>/.claude/skills/compass-research/`，使用 `/compass-research`。

**注意：** 子智能体调用能力依赖实际运行环境。Skill 会要求关键节点使用真正隔离上下文的子智能体，但如果运行环境没有该工具，不能把主 Agent 自行换角度思考冒充为独立调用。

## 文件结构

```text
compass-research-skill/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── compass-research/
│   ├── SKILL.md
│   └── references/
│       ├── methods.md                 # 诊断、实验设计与可选工具
│       ├── literature.md              # 目的驱动的论文阅读
│       ├── independent-perspective.md # 独立视角、问题框架审视
│       └── research-state.md          # 精简研究状态
└── tests/
    ├── scenarios.md
    └── validate_structure.py
```

## 测试与发布状态

这是覆盖完整设计范围的 **v1.0 正式发布候选版**，不是删减功能的 MVP。包含结构验证与盲测场景，但**结构正确不代表模型行为已经通过真实测试**。

```bash
python3 tests/validate_structure.py
```

正式发布前，应在全新会话中进行“无 Skill / 使用 Skill”的对照测试，检查 AI 是否保护探索空间、有效设计实验、避免过度防御与信息倾倒，以及关键分叉是否真实调用独立子智能体。见 [tests/scenarios.md](tests/scenarios.md)。

## 边界

优先服务于 AI / ML / CV 科研，但底层推理原则适用于更广泛的实验研究。不会自动提供训练基础设施、数据集、完整论文投稿流程、常驻多 Agent 团队或审计日志。具体执行可交给 Codex 等可用工具。

许可协议：MIT，见 [LICENSE](LICENSE)。