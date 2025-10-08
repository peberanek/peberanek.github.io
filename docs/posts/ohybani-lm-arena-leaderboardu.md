---
date:
  created: 2025-04-08
  updated: 2025-04-12
tags:
  - ai
  - generative-ai
  - lm-arena
  - andrej-karpathy
  - meta
  - llama
---

# Ohýbání LM Arena Leaderboardu

Andrej Karpathy [vyjádřil jistou nedůvěru](https://youtu.be/7xTGNNLPyMI?t=11815) k výsledkům na [LM Arena Leaderboard](https://lmarena.ai/?leaderboard) v posledních měsících. Příkladem je třeba oblíbený Claude 3.7 Sonnet, v žebříčku až okolo 15. místa. A hle, Meta nám tak trochu podvádí, resp. jejich model (na 2. místě) je jiný než modely, které reálně vydali:

> Meta’s interpretation of our policy did not match what we expect from model providers. Meta should have made it clearer that “Llama-4-Maverick-03-26-Experimental” was a customized model to optimize for human preference. As a result of that we are updating our leaderboard policies to reinforce our commitment to fair, reproducible evaluations so this confusion doesn’t occur in the future.  
-- [lmarena.ai](https://x.com/lmarena_ai/status/1909397817434816562) ([via](https://buttondown.com/ainews/archive/ainews-llama-4s-controversial-weekend-release/))

Pokud se jedná o upravený model, který není normálně k dispozici, říkám si proč nebyl z žebříčku odebrán.

_Update_: Zdá se, že Llama-4-Maverick-03-26-Experimental už byla z žebříčku odebrána, a [Llama-4-Maverick-17B-128E-Instruct](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) si nevede nijak oslnivě. Dnes okolo 32. místa.
