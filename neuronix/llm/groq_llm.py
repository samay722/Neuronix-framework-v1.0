from typing import Optional
from groq import Groq
from neuronix.llm.base import BaseLLM
from neuronix.config.settings import settings
from neuronix.core.exceptions import ConfigurationError
from neuronix.core.logger import logger


class GroqLLM(BaseLLM):

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        # Fallback to settings if api_key is None or the placeholder
        api_key = api_key or settings.GROQ_API_KEY
        if api_key == "YOUR_GROQ_API_KEY":
            api_key = settings.GROQ_API_KEY

        if not api_key:
            raise ConfigurationError("GROQ_API_KEY is not set in environment or settings.")

        # Print masked API key for debugging
        masked_key = f"{api_key[:8]}...{api_key[-4:]}" if len(api_key) > 12 else api_key
        print("DEBUG API KEY:", masked_key)  # ✅ ONLY HERE (inside __init__)

        self.client = Groq(api_key=api_key)
        self.model = model or settings.GROQ_MODEL_NAME

    def generate(self, prompt: str) -> str:

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content