"""
AI Incident Tools - AI事故响应工具
支持事故管理、根因分析、事后分析
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIIncidentTools:
    """
    AI事故响应工具
    支持：管理、根因、事后
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_incident_response_plan(self, organization: str) -> Dict:
        """设计事故响应计划"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{organization}设计事故响应计划：

请返回JSON格式：
{{
    "severity_levels": ["严重级别"],
    "response_team": ["响应团队"],
    "communication_plan": "沟通计划",
    "escalation": "升级流程"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"plan": content}

    def analyze_root_cause(self, symptoms: str, logs: List[str]) -> Dict:
        """分析根因"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        logs_text = "\n".join(logs[:20])

        prompt = f"""请分析以下事故的根因：

症状：{symptoms}
日志：
{logs_text}

请返回JSON格式：
{{
    "root_cause": "根因",
    "contributing_factors": ["因素"],
    "timeline": "时间线"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"root_cause": content}

    def generate_postmortem(self, incident: Dict) -> str:
        """生成事后分析报告"""
        if not self.client:
            return "LLM客户端未配置"

        incident_text = json.dumps(incident, ensure_ascii=False)

        prompt = f"""请根据以下事故信息生成事后分析报告：

{incident_text}

要求：
1. 事故概述
2. 时间线
3. 根因分析
4. 改进措施"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def design_runbook(self, service: str, scenarios: List[str]) -> str:
        """设计运维手册"""
        if not self.client:
            return "LLM客户端未配置"

        scenarios_text = "\n".join(f"- {s}" for s in scenarios)

        prompt = f"""请为{service}设计运维手册：

场景：
{scenarios_text}

要求：
1. 健康检查
2. 故障排查
3. 扩缩容"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_alert_rules(self, service: str, slos: Dict) -> str:
        """生成告警规则"""
        if not self.client:
            return "LLM客户端未配置"

        slos_text = json.dumps(slos, ensure_ascii=False)

        prompt = f"""请为{service}生成告警规则：

SLO：{slos_text}

要求：
1. 多级告警
2. 静默规则
3. 升级策略"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def design_oncall_rotation(self, team_size: int, coverage: str) -> Dict:
        """设计On-Call轮换"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请设计On-Call轮换：

团队大小：{team_size}
覆盖范围：{coverage}

请返回JSON格式：
{{
    "rotation_pattern": "轮换模式",
    "schedule": "排班表",
    "handoff": "交接流程"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"rotation": content}


def create_tools(**kwargs) -> AIIncidentTools:
    """创建事故响应工具"""
    return AIIncidentTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Incident Tools")
    print()

    # 测试
    plan = tools.design_incident_response_plan("科技公司")
    print(json.dumps(plan, ensure_ascii=False, indent=2))
