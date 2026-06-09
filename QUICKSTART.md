# 🚀 Neuronix - Quick Start

Get started with Neuronix in 5 minutes!

## Option 1: Interactive Setup (Recommended)

### Windows:
```bash
python setup.py
```

### macOS/Linux:
```bash
python3 setup.py
```

This will guide you through:
- Selecting your preferred LLM provider
- Getting an API key
- Configuring your `.env` file
- Testing the setup

---

## Option 2: Manual Setup

### Step 1: Copy the environment template
```bash
cp .env.example .env
```

### Step 2: Get your API key
Pick one provider:

**⚡ GROQ (Free, Recommended)**
```
1. Go to https://console.groq.com
2. Sign up (free, no credit card)
3. Copy your API key
4. Paste in .env:
   GROQ_API_KEY=your_key_here
   DEFAULT_LLM_PROVIDER=groq
```

**🤖 OpenAI**
```
1. Go to https://platform.openai.com/api-keys
2. Create API key
3. Paste in .env:
   OPENAI_API_KEY=sk-...
   DEFAULT_LLM_PROVIDER=openai
```

**🎁 Google Gemini**
```
1. Go to https://aistudio.google.com/app/apikey
2. Create API key
3. Paste in .env:
   GEMINI_API_KEY=...
   DEFAULT_LLM_PROVIDER=gemini
```

### Step 3: Verify setup
```bash
python test_run.py
```

---

## 🧪 Test Your Setup

### Test with default provider
```bash
python test_run.py
```

### Test specific provider
```python
from neuronix.llm import OpenAILLM

try:
    llm = OpenAILLM()
    response = llm.generate("Hello, how are you?")
    print(response)
except Exception as e:
    print(f"Error: {e}")
```

---

## 📖 Full Documentation

For complete setup instructions with all providers and troubleshooting:
```bash
cat SETUP_GUIDE.md
```

Or view: [SETUP_GUIDE.md](SETUP_GUIDE.md)

---

## ⌨️ Using Neuronix

### Python API
```python
from neuronix.rag import RAGPipeline

# Initialize
pipeline = RAGPipeline(document_path="data.txt")

# Ask a question
response = pipeline.ask("What is AI?")
print(response)
```

### CLI
```bash
python -m neuronix.main query "What is machine learning?"
```

### API Server
```bash
python -m neuronix.api.app
# Open: http://localhost:8000
```

---

## 🆘 Troubleshooting

**"API Key is not set"**
- Make sure `.env` file exists (not `.env.example`)
- Check variable name matches exactly
- Restart your terminal

**"Invalid API Key"**
- Double-check the key wasn't truncated
- Verify it's not expired
- Get a new key from the provider

**"Module not found"**
- Install dependencies: `pip install -r requirements.txt`

**"Connection error"**
- Check internet connection
- Verify API endpoint is accessible
- Try a different provider

---

## 💡 Pro Tips

1. **Start with GROQ** - Free, fast, perfect for testing
2. **Keep `.env` secret** - Add `.env` to `.gitignore`
3. **Test before production** - Use test queries first
4. **Monitor usage** - Check provider dashboards for costs

---

## 📚 More Information

- 📖 [SETUP_GUIDE.md](SETUP_GUIDE.md) - Detailed API key instructions
- 🏠 [README.md](README.md) - Full project documentation
- 🧪 [test_run.py](test_run.py) - Test script

---

**Ready? Run: `python setup.py`** 🚀
