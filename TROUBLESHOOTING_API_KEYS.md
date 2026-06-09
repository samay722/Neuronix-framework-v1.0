# 🔧 API Key Troubleshooting Guide

Common issues and solutions for API key configuration in Neuronix.

---

## ❌ Common Problems & Solutions

### 1. "API Key is not set in environment or settings"

**Problem:** You're getting an error that a specific API key is missing.

**Cause:** The API key environment variable is not defined.

**Solutions:**

**Option A: Using `.env` file**
```bash
# Make sure these files exist:
# ✓ .env (NOT .env.example)
# 
# Add your API key:
# GROQ_API_KEY=your_key_here
```

**Option B: Using environment variables**
```bash
# macOS/Linux:
export GROQ_API_KEY="your_key_here"
python test_run.py

# Windows PowerShell:
$env:GROQ_API_KEY = "your_key_here"
python test_run.py

# Windows CMD:
set GROQ_API_KEY=your_key_here
python test_run.py
```

**Option C: Using setup script**
```bash
python setup.py
```

**Verification:**
```bash
python -c "from neuronix.config.settings import settings; print(settings.GROQ_API_KEY)"
```

---

### 2. "Invalid API Key" or "Unauthorized"

**Problem:** API key exists but provider rejects it.

**Causes:**
- Key is expired
- Key has trailing/leading spaces
- Wrong key for the provider
- Key has been revoked

**Solutions:**

1. **Check for spaces:**
```bash
# Make sure no spaces around = sign
✓ GROQ_API_KEY=gsk_abc123
✗ GROQ_API_KEY = gsk_abc123   (spaces around =)
✗ GROQ_API_KEY=gsk_abc123     (trailing space)
```

2. **Get a new key:**
   - GROQ: https://console.groq.com/keys
   - OpenAI: https://platform.openai.com/api-keys
   - Gemini: https://aistudio.google.com/app/apikey
   - Anthropic: https://console.anthropic.com/keys
   - DeepSeek: https://platform.deepseek.com/api-keys

3. **Verify the right key:**
   - Make sure you're using the correct provider's key
   - Don't mix up keys between providers

4. **Check expiration:**
   - Some providers allow setting key expiration
   - Log in to provider console and check your keys

---

### 3. "Module not found: openai", "No module named google"

**Problem:** Python library for LLM provider is not installed.

**Cause:** Dependencies not installed.

**Solutions:**

```bash
# Install all dependencies
pip install -r requirements.txt

# Or install specific provider:
pip install openai              # For OpenAI
pip install google-generativeai # For Gemini
pip install anthropic           # For Anthropic Claude
pip install groq                # For Groq
```

---

### 4. "Connection refused" or "Cannot connect to API"

**Problem:** Cannot reach the LLM provider's API.

**Causes:**
- No internet connection
- Provider API is down
- Firewall/proxy blocking
- Using Ollama but it's not running

**Solutions:**

1. **Check internet:**
```bash
ping google.com  # Check connectivity
```

2. **For Ollama specifically:**
```bash
# Make sure Ollama is running:
ollama serve

# In another terminal, verify it's working:
curl http://localhost:11434/api/tags
```

3. **Check firewall:**
   - Make sure firewall isn't blocking HTTPS connections
   - Try disabling temporarily to test

4. **Check provider status:**
   - Visit provider's status page
   - GROQ: https://status.groq.com
   - OpenAI: https://status.openai.com
   - Gemini: https://status.cloud.google.com
   - Anthropic: https://status.anthropic.com

---

### 5. "Rate limit exceeded"

**Problem:** Too many requests in a short time.

**Cause:** Hit the provider's rate limits.

**Solutions:**

1. **Wait:** Most limits reset after a short time
   ```bash
   # Wait a few minutes and try again
   sleep 300  # Wait 5 minutes
   python test_run.py
   ```

2. **Upgrade your plan:**
   - GROQ: Upgrade from free tier
   - OpenAI: Check usage dashboard
   - Others: Upgrade to higher tier plan

3. **Add delays in code:**
```python
import time
from neuronix.llm import GroqLLM

llm = GroqLLM()
for i in range(5):
    response = llm.generate(f"Test {i+1}")
    time.sleep(2)  # Wait 2 seconds between requests
```

---

### 6. ".env file not found" or not being read

**Problem:** Settings are not picking up values from `.env`.

**Causes:**
- File in wrong location
- Filename is wrong
- Using `.env.example` instead of `.env`

**Solutions:**

1. **Verify `.env` exists in project root:**
```bash
# macOS/Linux:
ls -la | grep ".env"

# Windows:
dir | findstr ".env"
```

2. **Make sure it's named `.env` exactly:**
```bash
# Not .env.example, not .env.txt, but .env
cp .env.example .env
```

3. **Verify location:**
```
d:\Neuronix-framework v1.0\
├── .env           ✓ Correct location
├── .env.example
├── setup.py
└── neuronix/
```

4. **Check permissions:**
```bash
# macOS/Linux:
chmod 600 .env  # Make file readable by owner only (secure)
```

---

### 7. Wrong provider being used

**Problem:** Using a provider you didn't intend.

**Cause:** `DEFAULT_LLM_PROVIDER` setting not set correctly.

**Solutions:**

1. **Check current setting:**
```bash
python -c "from neuronix.config.settings import settings; print(settings.DEFAULT_LLM_PROVIDER)"
```

2. **Update `.env`:**
```bash
# Make sure this line is set:
DEFAULT_LLM_PROVIDER=groq  # Change to your provider

# Options: groq, openai, anthropic, gemini, deepseek, ollama
```

3. **Explicit provider in code:**
```python
from neuronix.llm import OpenAILLM, GroqLLM

# Explicit:
llm = OpenAILLM()  # Use OpenAI specifically

# Or dynamic:
from neuronix.llm import get_llm
llm = get_llm("openai")  # Use OpenAI
```

---

### 8. Ollama connection refused

**Problem:** Cannot connect to local Ollama instance.

**Error:** `Connection refused` or `Failed to establish connection`

**Solutions:**

1. **Start Ollama:**
```bash
ollama serve
```

2. **Verify it's running:**
```bash
curl http://localhost:11434/api/tags
```

3. **Check `.env` configuration:**
```bash
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL_NAME=llama3
DEFAULT_LLM_PROVIDER=ollama
```

4. **Pull a model if not present:**
```bash
ollama pull llama3
ollama list  # Check available models
```

5. **Check port is not in use:**
```bash
# macOS/Linux:
lsof -i :11434

# Windows PowerShell:
Get-Process -Id (Get-NetTCPConnection -LocalPort 11434).OwningProcess
```

---

### 9. "Invalid model name"

**Problem:** Model name doesn't exist for the provider.

**Solutions:**

1. **Check available models for each provider:**

```python
# GROQ models:
# llama-3.1-8b-instant
# gemma2-9b-it
# mixtral-8x7b-32768

# OpenAI models:
# gpt-4o
# gpt-4o-mini
# gpt-3.5-turbo

# Gemini models:
# gemini-1.5-flash
# gemini-1.5-pro

# Anthropic models:
# claude-3-5-sonnet-20241022
# claude-3-opus-20240229
# claude-3-haiku-20240307

# DeepSeek models:
# deepseek-chat
# deepseek-coder

# Ollama models:
ollama list  # List installed models
```

2. **Update `.env` with correct model:**
```bash
OPENAI_MODEL_NAME=gpt-4o-mini
```

3. **Or specify in code:**
```python
from neuronix.llm import OpenAILLM
llm = OpenAILLM(model_name="gpt-4o-mini")
```

---

### 10. "ConfigurationError: ANTHROPIC_API_KEY is not set"

**Problem:** Anthropic API key not found.

**Note:** Anthropic is also called "Claude"

**Solutions:**

```bash
# 1. Get your key from:
# https://console.anthropic.com/keys

# 2. Add to .env:
ANTHROPIC_API_KEY=sk-ant-...

# 3. Verify:
python -c "from neuronix.config.settings import settings; print(settings.ANTHROPIC_API_KEY[:10])"
```

---

## 🧪 Debugging Steps

### Step 1: Verify `.env` file exists
```bash
python -c "import os; print(os.path.exists('.env'))"
```

### Step 2: Check if variable is set
```bash
python -c "from neuronix.config.settings import settings; print(f'GROQ_API_KEY: {settings.GROQ_API_KEY}')"
```

### Step 3: Test specific provider
```python
from neuronix.llm import get_llm
from neuronix.config.settings import settings

try:
    provider = settings.DEFAULT_LLM_PROVIDER
    print(f"Using provider: {provider}")
    
    llm = get_llm(provider)
    print(f"✓ Successfully initialized {provider}")
    
    response = llm.generate("Hello!")
    print(f"✓ Got response: {response[:50]}...")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
```

### Step 4: Check Python version
```bash
python --version  # Should be 3.10+
```

### Step 5: Check installed packages
```bash
pip list | grep -E "groq|openai|google|anthropic|deepseek"
```

---

## 📞 Getting Help

1. **Check documentation:**
   - Read [SETUP_GUIDE.md](SETUP_GUIDE.md)
   - Read [QUICKSTART.md](QUICKSTART.md)

2. **Run setup script:**
   ```bash
   python setup.py
   ```

3. **Check provider docs:**
   - GROQ: https://console.groq.com/docs
   - OpenAI: https://platform.openai.com/docs
   - Gemini: https://ai.google.dev/docs
   - Anthropic: https://docs.anthropic.com
   - DeepSeek: https://platform.deepseek.com/docs
   - Ollama: https://github.com/ollama/ollama

---

## ✅ Verification Checklist

- [ ] `.env` file exists and is readable
- [ ] API key is copied completely (no truncation)
- [ ] No spaces around `=` in `.env`
- [ ] `DEFAULT_LLM_PROVIDER` is set correctly
- [ ] Python version is 3.10+
- [ ] Required dependencies are installed
- [ ] `.env` file is not in `.gitignore` (for local use)
- [ ] API key hasn't expired
- [ ] Provider account has active/valid status
- [ ] Test passes: `python test_run.py`

---

**Still having issues? Check the specific provider documentation or run `python setup.py` for interactive help.**
