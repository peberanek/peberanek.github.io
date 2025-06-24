---
date: 2025-03-05
---

# `llm`

Dneska jsem vyzkoušel nástroj do příkazové řádky, nazvaný jednoduše [llm](https://llm.datasette.io/en/stable/). Jednou z výhod je, že dokáže volat i lokální modely běžící přes [Ollamu](https://ollama.com/).

> A CLI utility and Python library for interacting with Large Language Models, both via remote APIs and models that can be installed and run on your own machine.
  
``` sh
llm "Tell me a joke about LLMs."
```

Nainstaloval jsem přes [uv](https://docs.astral.sh/uv/) ([možno použít i pip](https://llm.datasette.io/en/stable/setup.html#installation)):
``` sh
uv tool install llm
```

Mám OpenAI API Key, tak jsem ho hned využil:
``` sh
llm keys set openai
```

Vypsat dostupné modely lze následovně:
``` sh
llm models
llm models default # (1)!
```

1.  Vypíše defaultní model (`gpt-4o-mini`).

Interaktivní chat:
``` sh
llm chat
```

Skvělé je, že pomocí [pluginů](https://llm.datasette.io/en/stable/plugins/index.html) lze připojit [řadu dalších modelů](https://llm.datasette.io/en/stable/plugins/directory.html), včetně již zmíněné Ollamy (tu je potřeba mít nainstalovanou, spouštěnou a mít stažený příslušný model):
``` sh
llm install llm-ollama
llm "Tell me a joke about LLMs." -m llama3.2
```