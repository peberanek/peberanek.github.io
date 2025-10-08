---
date: 2025-04-15
tags:
  - ai
  - generative-ai
---

# OpenAI GPT-4.1

[OpenAI vydala novou sérii modelů GPT-4.1](https://openai.com/index/gpt-4-1/) ([via](https://buttondown.com/ainews/archive/ainews-gpt-41-the-new-openai-workhorse/)) (číslování je trochu matoucí vzhledem k nedávno vydanému GPT-4.5 research preview). Z příspěvku je zřejmé, že modely jsou cílené primárně na oblast programování a programovacích asistentů/agentů, kde dlouho vládl Claude 3.5 (resp. 3.7) Sonnet, a nově vstoupila Gemini 2.5 Pro. OpenAI inzeruje také zlepšené výsledky v následování instrukcí (oproti GPT-4o), a výrazně větší kontext - až 1 milion tokenů (což by mělo např. pojmout - 8x - celý zdrojový kód Reactu).

<!-- more -->

Není v plánu zpřístupnit nové modely v ChatGPT:

> Note that GPT-4.1 will only be available via the API. In ChatGPT, many of the improvements in instruction following, coding, and intelligence have been gradually incorporated into the latest version of GPT-4o, and we will continue to incorporate more with future releases.

Zajímavá je i cena generovaných (output) tokenů: GPT-4.1 je oproti Claude 3.7 Sonnet a Gemini 2.5 Pro zhruba o polovinu levnější ($8 oproti $15 za 1 milion tokenů). Výrazně lépe vychází oproti o1 ($60), nemluvě o o1-pro ($600). Poměr vůči o3 ($4.40) nedokážu odhadnout vzhledem k nutnosti generovat reasoning tokeny.

Dlouhý kontext:

> Thomson Reuters tested GPT‑4.1 with CoCounsel, their professional grade AI assistant for legal work. Compared to GPT‑4o, they were able to improve multi-document review accuracy by 17% when using GPT‑4.1 across internal long-context benchmarks—an essential measure of CoCounsel’s ability to handle complex legal workflows involving multiple, lengthy documents. In particular, they found the model to be highly reliable at maintaining context across sources and accurately identifying nuanced relationships between documents, such as conflicting clauses or additional supplementary context—tasks critical to legal analysis and decision-making.

> In our initial testing, latency to first token for GPT‑4.1 was approximately fifteen seconds with 128,000 tokens of context, and a minute for a million tokens of context. GPT‑4.1 mini and nano are faster, e.g., GPT‑4.1 nano most often returns the first token in less than five seconds for queries with 128,000 input tokens.

## Poznámky
* Ve zpracování obrazu vychází GPT-4.1 a GPT-4.1-mini téměř stejně (viz článek), přičemž mini stojí pouze 1/5 ceny.
* V oblasti 'Academic knowledge' vychází GPT-4.1 (i GPT-4.1-mini!) stejně nebo dokonce lépe než stávající ChatGPT-4o.
