import os
from typing import Optional
import google.generativeai as genai
from neuronix.llm.base import BaseLLM
from neuronix.core.exceptions import ConfigurationError, LLMError
from neuronix.core.logger import logger
from neuronix.config.settings import settings

class GeminiLLM(BaseLLM):
    def __init__(self, model_name: Optional[str] = None):
        api_key = settings.GEMINI_API_KEY
        if not api_key:
            raise ConfigurationError("GEMINI_API_KEY is not set in environment or settings.")
            
        genai.configure(api_key=api_key)
        self.model_name = model_name or settings.GEMINI_MODEL_NAME
        try:
            self.model = genai.GenerativeModel(self.model_name)
            logger.info(f"Initialized Gemini LLM with model {self.model_name}")
        except Exception as e:
            logger.error(f"Failed to initialize Gemini model: {str(e)}")
            raise ConfigurationError(f"Gemini initialization error: {str(e)}")
        
    def generate(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Error generating response from Gemini: {str(e)}")
            raise LLMError(f"Gemini generation failed: {str(e)}")
