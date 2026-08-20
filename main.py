import os
from dataclasses import dataclass

from langchain.agents import create_agent
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langchain_core.utils.uuid import uuid7
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import InMemorySaver
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from pydantic.types import SecretStr

from settings import settings

@tool
def search(query: str) -> str:
    """搜索内容"""
    return f"搜索【{query}】结果:"


model = ChatOpenAI(
    model="deepseek-v4-flash",
    base_url="https://api.deepseek.com",
    api_key=settings.deepseek_api_key,
)

# 结构化输出
class Answer(BaseModel):
    summary: str
    confidence: float

agent = create_agent(
    model = model,
    tools = [search],
    # 系统提示词。
    system_prompt = "你是一个小猪手.",
)

@dataclass
class Context:
    user_id: str

config: RunnableConfig = {
    "configurable": {
        "thread_id": str(uuid7())
    }
}

# result = agent.invoke(
#     {"messages": [{"role": "user", "content": "Summarize AI trends"}]},
#     config = config,
# )

stream = agent.stream_events(
    {"messages": [{"role": "user", "content": "Summarize AI trends"}]},
    version="v3"
)

for snapshot in stream.values:
    last_message = snapshot["messages"][-1]
    print(last_message.content)