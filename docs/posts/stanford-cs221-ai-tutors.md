---
date: 2025-09-26
tags:
  - ai
  - generative-ai
  - ai-assistants
  - chatbots
---

# Stanford CS221 AI tutoring

[Stanford CS221 Autumn 2025](https://stanford-cs221.github.io/autumn2025/assignments/hw1_foundations/index.html) ([via](https://simonwillison.net/2025/Sep/24/stanford/)): Studenti jsou v rámci hodnocených úkolů motivováni využít interaktivní AI tutory (viz níže). (Mimochodem, netriviálním problémem této pomůcky je [ověření, že AI tutor je skutečně pedagogicky užitečný](https://www.youtube.com/watch?v=KNUFNTj-yMQ). V tomto případě student přikládá odkaz na celou konverzaci.)

> **Learn basic NumPy operations with an AI tutor!** Use an AI chatbot (e.g., ChatGPT, Claude, Gemini, or Stanford AI Playground) to teach yourself how to do basic vector and matrix operations in NumPy (import numpy as np). AI tutors have become exceptionally good at creating interactive tutorials, and this year in CS221, we're testing how they can help you learn fundamentals more interactively than traditional static exercises.

<!-- more -->

>
> There are many ways to do this. For example, you can simply ask the chatbot "Teach me basic NumPy operations interactively". We provide a prompt template for you to use, but feel free to use your own: 
> ```
> Teach me basic NumPy operations. Keep the session ~15–20 minutes and interactive.
>
> Guidelines
> - Adjust difficulty: if I miss 2 in a row → slow + simpler; if I get 2 quickly → a bit harder or add a twist.
> - Use tiny, deterministic examples (small numbers, short tables, brief ASCII diagrams, code blocks). Show actual *run-throughs* (step-by-step states) if helps.
> - Use Code if it clarifies: ≤2 Python/NumPy blocks, each ≤20 lines; ideally no imports beyond `import numpy as np`.
> - Do NOT solve graded work. If I paste any, refuse and make a similar practice item.
> - Be CONCISE. Don't make notation complicated/unnecessary. Focus on intuitions. Code blocks should be short with simple variable names.
> - I may interrupt and ask to start somewhere else. Simply adjust and adapt from there.
>
> Suggested flow (flexible; use judgment)
> 1) Start by explaining the topic in a few simple, but technically accurate sentences (explain core idea (≤6 sentences): intuition + minimal notation + why it matters + one common pitfall). Use basic notations and visualizations if necessary (CS221 requires basic math/programming backgrounds). For topics about programming, OK to start with concise code blocks
> 2) Quick check-in (≤1–2 min): ask 2 short questions about prior exposure and specific goal.
> 3) Exercises: use a tiny instance and show intermediate states. Give exercises that build on each other. OK to give multiple exercises at the same time.
>    - e.g., for graph search: a 4–5 node weighted graph; show the frontier/priority-queue after each of 2–3 steps and which edges relax.
>    - for DP/MDP/RL/Logic/ML, do an equivalently small, concrete step-by-step trace.
>    - If code clarifies, include one concise NumPy block.
> 4) 3 quick checks: increasing difficulty; give a hint first; reveal answers only after I try or ask.
> 5) Assessment and feedback: Give me feedback on my performance - what I understood well, what needs improvement, and specific concepts to review further.
> 6) Session reflection: Ask me for feedback on how the tutoring session went - what worked well, what could be improved, and if the pacing/difficulty was appropriate.
> 7) Recap: a 60-second summary
> ```
>
> **What we expect**: Provide a link to the chat session transcript with the AI tutor. The session should be ~15–20 minutes and interactive!
