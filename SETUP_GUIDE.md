# 🔑 Neuronix API Keys Setup Guide

Complete guide to getting API keys for all supported LLM providers.

---

## ⚡ Quick Start (Recommended)

### Option 1: Use Free Tier (GROQ)
**Best for getting started immediately - no credit card required**

1. Go to https://console.groq.com
2. Click **"Sign Up"** or **"Sign In"**
3. Verify your email
4. Navigate to **"API Keys"** in the sidebar
5. Click **"Create API Key"**
6. Copy the key and paste into `.env`:
```
GROQ_API_KEY=your_key_here
DEFAULT_LLM_PROVIDER=groq
```
7. Run the tests to verify setup

---

## 🔐 Complete Setup Guide

### 1. **GROQ** (Recommended - Free Tier)
**⭐ Fastest inference, free tier, no credit card required**

**Steps:**
1. Visit https://console.groq.com
2. Sign up with email/GitHub/Google
3. Click **"API Keys"** in the sidebar
4. Click **"Create API Key"**
5. Copy and save in `.env`:
```
GROQ_API_KEY=gsk_...
DEFAULT_LLM_PROVIDER=groq
```

**Model Options:**
- `llama-3.1-8b-instant` (default, fastest)
- `gemma2-9b-it`
- `mixtral-8x7b-32768`

**Rate Limits:** 30 requests/minute (free)

---

### 2. **OpenAI** (GPT-4, GPT-3.5)
**💰 Premium models, requires paid account**

**Steps:**
1. Visit https://platform.openai.com/api-keys
2. Click **"Create new secret key"**
3. Copy the key immediately (shown only once)
4. Add to `.env`:
```
OPENAI_API_KEY=sk-...
DEFAULT_LLM_PROVIDER=openai
OPENAI_MODEL_NAME=gpt-4o-mini
```

**Model Options:**
- `gpt-4o` (best, expensive)
- `gpt-4o-mini` (recommended, cheaper)
- `gpt-3.5-turbo` (most economical)

**Pricing:** ~$0.15 per 1M input tokens (gpt-4o-mini)

**Set Up Billing:**
1. Go to https://platform.openai.com/account/billing/overview
2. Add a payment method
3. Set usage limits for safety

---

### 3. **Google Gemini** (Free Tier Available)
**🎁 Free tier, good performance**

**Steps:**
1. Visit https://aistudio.google.com/app/apikey
2. Click **"Create API Key"** (or create in new Google Cloud project)
3. Copy the key
4. Add to `.env`:
```
GEMINI_API_KEY=...
DEFAULT_LLM_PROVIDER=gemini
GEMINI_MODEL_NAME=gemini-1.5-flash
```

**Model Options:**
- `gemini-1.5-flash` (recommended, faster)
- `gemini-1.5-pro` (more capable)

**Rate Limits:** 60 requests/minute (free)

---

## 🚀 Getting Started

### Step 1: Copy the template
```bash
cp .env.example .env
```

### Step 2: Choose a provider and get API key

**If unsure, start with GROQ** (free, fast, no credit card):
- Visit https://console.groq.com
- Get your API key
- Add to `.env`

### Step 3: Test your setup

```bash
# Run the test
python test_run.py

# Or use CLI
python -m neuronix.main --help
python -m neuronix.main query "What is AI?"
```

### Step 4: Check the logs
If there are errors, they'll clearly indicate which API key is missing.

---

## 💡 Pro Tips

1. **Start with GROQ** - Free, fast, perfect for development
2. **Use environment variables** - Don't commit `.env` to git
3. **Set rate limit alerts** - Especially important for paid providers
4. **Test before production** - Use small models first to verify setup
5. **Keep keys secret** - Never share or commit API keys

---

## 🔒 Security Best Practices

1. **Never commit `.env` to git**
   ```bash
   echo ".env" >> .gitignore
   ```

2. **Use different keys for dev/prod**
   - Create separate API keys for each environment
   - Rotate keys regularly

3. **Monitor usage**
   - Check provider dashboards for unexpected activity
   - Set spending limits

4. **Use environment variables**
   ```bash
   export GROQ_API_KEY="your_key_here"
   python script.py
   ```

---

## 📚 Additional Resources

- **GROQ:** https://console.groq.com/docs/speech-text
- **OpenAI:** https://platform.openai.com/docs
- **Gemini:** https://ai.google.dev/docs
- **Anthropic:** https://docs.anthropic.com
- **DeepSeek:** https://platform.deepseek.com/docs
- **Ollama:** https://github.com/ollama/ollama

---

## ✅ Verification Checklist

- [ ] `.env` file created (not just `.env.example`)
- [ ] API key added for chosen provider
- [ ] `DEFAULT_LLM_PROVIDER` set correctly
- [ ] Test script runs without "API key not set" errors
- [ ] Got valid response from LLM
- [ ] `.env` added to `.gitignore`
- [ ] Ready for production use

---

**Happy coding! 🚀**
