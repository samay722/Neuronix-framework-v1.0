from neuronix.llm.base import BaseLLM
from neuronix.llm.groq_llm import GroqLLM
from neuronix.llm.openai_llm import OpenAILLM
from neuronix.llm.gemini_llm import GeminiLLM
from neuronix.core.exceptions import ConfigurationError

def get_llm(provider: str, **kwargs) -> BaseLLM:
    provider = provider.lower().strip()
    if provider == "groq":
        return GroqLLM(**kwargs)
    elif provider == "openai":
        return OpenAILLM(**kwargs)
    elif provider == "gemini":
        return GeminiLLM(**kwargs)
    else:
        raise ConfigurationError(
            f"Unsupported LLM provider: {provider}. "
            "Supported providers: groq, openai, gemini"
        )

__all__ = [
    "BaseLLM",
    "GroqLLM",
    "OpenAILLM",
    "GeminiLLM",
    "get_llm",
]
