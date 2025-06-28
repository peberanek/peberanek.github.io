---
date: 2025-06-23
links:
  - posts/ai-jako-spolupracovnik.md
---

# Měnící se role vývojáře

V diskusích z vývojáři občas zaznívá, že se místo psaní kódu stávají spíše 'prompt operátory'. Níže přidávám několik souvisejících postřehů z webu Simona Willisona (zvýraznění níže jsou moje):

> So you can think really big thoughts and the leverage of having those big thoughts has just suddenly expanded enormously. I had this tweet two years ago where I said **"90% of my skills just went to zero dollars and 10% of my skills just went up 1000x"**. And this is exactly what I'm talking about - **having a vision, being able to set milestones towards that vision, keeping track of a design to maintain or control the levels of complexity as you go forward**. Those are hugely leveraged skills now compared to knowing where to put the ampersands and the stars and the brackets in Rust.  
-- [Kent Beck](https://www.youtube.com/watch?v=aSXaxOdVtAQ&t=12m30s) ([via](https://simonwillison.net/2025/Jun/22/kent-beck/))

---

> Armin Ronacher had Claude and Claude Code do almost all of the work in building, testing, packaging and publishing a new Python library [..] [sloppy-xml-py](https://github.com/mitsuhiko/sloppy-xml-py), a lax XML parser (and violation of everything the XML Working Group hold sacred) which ironically is necessary because LLMs themselves frequently output "XML" that includes validation errors. [...]
>
> It's useful, well defined, the code is readable with just about the right level of comments, everything is tested, the documentation explains everything I need to know, and it's been shipped to PyPI.
>
> I'd be proud to have written this myself.
>
> This example is not an argument for replacing programmers with LLMs. **The code is good because Armin is an expert programmer who stayed in full control throughout the process. As I wrote the other day, a skilled individual with both deep domain understanding and deep understanding of the capabilities of the agent.**  
-- [Simon Willison](https://simonwillison.net/2025/Jun/21/my-first-open-source-ai-generated-library/)

Jinými slovy, zkušeného schopného programátora GenAI nástroje mohou zbavit rutinních úkolů, jako je fyzické psaní kódu a jeho testování. A naopak člověka bez zkušeností mohou zavést do slepé uličky, protože nebude schopen vidět problémy jako vadný design nebo bezpečnostní zranitelnosti. _Augmentation, not a replacement._

Zajímavá historická paralela: [_computer_](https://en.wikipedia.org/wiki/Computer_(occupation)) byl svého času název profese vykonávané lidmi. Nebudu překvapen, pokud jednoho dne bude _programmer_ (nebo _coder_) také jen softwarová komponenta (podobně jako např. _compiler_), a role vývojáře bude postupně mnohem více o supervizi, ladění funkcionality, použitelnosti a komunikaci s uživateli.
