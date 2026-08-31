from langchain.chat_models import init_chat_model

from settings import settings


class Models:
    DEEPSEEK_V4_FLASH: str = "deepseek-v4-flash"
    DEEPSEEK_V4_PRO: str = "deepseek-v4-pro"

    @classmethod
    def flash(cls):
        return  init_chat_model(
            Models.DEEPSEEK_V4_FLASH,
            base_url="https://api.deepseek.com",  # deepseek api路径兼容 OpenAI
            api_key=settings.deepseek_api_key
        )

    @classmethod
    def chat(cls):
        return init_chat_model(
            "deepseek-chat",
            base_url="https://api.deepseek.com",
            api_key=settings.deepseek_api_key
        )