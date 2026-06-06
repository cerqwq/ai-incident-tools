# 🚨 AI Incident Tools

AI事故响应工具，支持事故管理、根因分析、事后分析。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ 事故响应计划设计
- 🔍 根因分析
- 📝 事后分析报告
- 📖 运维手册设计
- 🔔 告警规则生成
- 📅 On-Call轮换设计

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_incident_tools import create_tools

tools = create_tools()

# 事故响应计划
plan = tools.design_incident_response_plan("科技公司")

# 根因分析
rca = tools.analyze_root_cause("服务响应缓慢", logs)

# 事后分析报告
postmortem = tools.generate_postmortem(incident)

# 运维手册
runbook = tools.design_runbook("API服务", scenarios)

# 告警规则
alerts = tools.generate_alert_rules("API服务", slos)

# On-Call轮换
rotation = tools.design_oncall_rotation(5, "24/7")
```

## 📁 项目结构

```
ai-incident-tools/
├── tools.py       # 事故响应工具核心
└── README.md
```

## 📄 许可证

MIT License
