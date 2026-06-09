class NeuronixError(Exception):
    """Base exception for Neuronix framework."""
    pass

class LLMError(NeuronixError):
    """Exception raised for errors in the LLM component."""
    pass

class VectorStoreError(NeuronixError):
    """Exception raised for errors in the VectorStore component."""
    pass

class ConfigurationError(NeuronixError):
    """Exception raised for configuration errors."""
    pass
