---
date: 2026-02-21
tags:
  - ai
  - generative-ai
  - open-source
  - simon-willison
  - software-development
---

# Minimalistický počátek projektu llama.cpp

[Simon Willison včera psal](https://simonwillison.net/2026/Feb/20/ggmlai-joins-hugging-face/) o spojení týmu ggml.ai (Georgi Gerganov, [llama.cpp](https://github.com/ggml-org/llama.cpp)) s Hugging Face. Zaujalo mě, jak [minimalistické README (resp. funkcionalitu)](https://github.com/ggml-org/llama.cpp/blob/775328064e69db1ebd7e19ccb59d2a7fa6142470/README.md) llama.cpp projekt na počátku měl. V podstatě "jen" prototyp pro běh modelu Llama 2 (7B) s 4-bitovou kvantizací na MacBooku (na CPU). 

> This was hacked in an evening - I have no idea if it works correctly.
>
> So far, I've tested just the 7B model and the generated text starts coherently, but typically degrades significanlty after ~30-40 tokens.

Uživatel si musí program sám zkompilovat a počítat s řadou omezení.

> Limitations
>
> * Currently, only LLaMA-7B is supported since I haven't figured out how to merge the tensors of the bigger models. However, in theory, you should be able to run 65B on a 64GB MacBook
> * Not sure if my tokenizer is correct. There are a few places where we might have a mistake: [...]
> * I don't know yet how much the quantization affects the quality of the generated text
> * Probably the token sampling can be improved
> * No Windows support
> * x86 quantization support not yet ready. Basically, you want to run this on Apple Silicon

Líbí se mi ta jednoduchost a transparentnost bez nároku na hotový produkt, bez nároku někomu něco prodávat. A přesto je dnes llama.cpp velmi propulární a využívaný nástroj pro běh velkých jazykových modelů na vlastním hardware.
