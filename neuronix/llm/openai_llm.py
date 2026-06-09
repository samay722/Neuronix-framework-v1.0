import os
from typing import Optional
from openai import OpenAI
from neuronix.llm.base import BaseLLM
from neuronix.core.exceptions import ConfigurationError, LLMError
from neuronix.core.logger import logger
from neuronix.config.settings import settings

class OpenAILLM(BaseLLM):
    def __init__(self, model_name: Optional[str] = None):
        api_key = settings.OPENAI_API_KEY
        if not api_key:
            raise ConfigurationError("OPENAI_API_KEY is not set in environment or settings.")
            
        self.client = OpenAI(api_key=api_key)
        self.model_name = model_name or settings.OPENAI_MODEL_NAME
        logger.info(f"Initialized OpenAI LLM with model {self.model_name}")
        
    def generate(self, prompt: str) -> str:
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=self.model_name,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            logger.error(f"Error generating response from OpenAI: {str(e)}")
            raise LLMError(f"OpenAI generation failed: {str(e)}")
