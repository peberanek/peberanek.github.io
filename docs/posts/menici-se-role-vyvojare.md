---
date:
  created: 2025-06-23
  updated: 2025-06-30
tags:
  - ai
  - generative-ai
  - simon-willison
  - vibe-coding
  - software-development
  - intelligence-augmentation
  - creativity
---

# Měnící se role vývojáře

V diskusích z vývojáři občas zaznívá, že se místo psaní kódu stávají spíše 'prompt operátory'. Níže přidávám několik souvisejících postřehů z blogu Simona Willisona. Případná zvýraznění jsou ode mě.

Nejprve komentář k odporu zaměstanců Amazonu více využívat generativní AI:

> > “It’s more fun to write code than to read code,” said Simon Willison, an A.I. fan who is a longtime programmer and blogger, channeling the objections of other programmers. “If you’re told you have to do a code review, it’s never a fun part of the job. When you’re working with these tools, it’s most of the job.” [...]
>
> It took me about 15 years of my career before I got over my dislike of reading code written by other people. It's a difficult skill to develop! I'm not surprised that a lot of people dislike AI-assisted programming paradigm when the end result is less time writing, more time reading!
>
> > “If you’re a prototyper, this is a gift from heaven,” Mr. Willison said. “You can knock something out that illustrates the idea.”
>
> Rapid prototyping has been a key skill of mine for a long time. I love being able to bring half-baked illustrative prototypes of ideas to a meeting - my experience is that the quality of conversation goes up by an order of magnitude as a result of having something concrete for people to talk about.
>
> These days I can vibe code a prototype in single digit minutes.  
-- [Simon Willison](https://simonwillison.net/2025/May/28/amazon-some-coders/)

Využít [_vibe coding_](https://en.wikipedia.org/wiki/Vibe_coding) k prototypování mi přijde jako skvělý nápad. Myslím, že jedním z důvodů, proč lidé tuto možnost nevidí, a automaticky jej zavrhují, je jakási nejasnost nebo zmatení pojmů. Dokonce jsem se setkal s názorem (na konferenci o generativní AI ve vzdělávání), že vibe coding je nebezpečný, protože vede k nasazování software s potenciálními bezpečnostními chybami, klidně i na produkci. Když jsem se snažil vysvětlit, že jej přece můžu využít jen na rychlou tvorbu prototypů, kde jsou rizika minimální, bylo mi odpovězeno, že to není vibe coding. Myslím, že jakékoliv diskusi týkající se umělé inteligence by hodně pomohlo nejprve si ujasnit pojmy, abychom si rozuměli.

<!-- more -->

Dále, programování s asistencí generativní AI je mnohem více o supervizi:

> So you can think really big thoughts and the leverage of having those big thoughts has just suddenly expanded enormously. I had this tweet two years ago where I said **"90% of my skills just went to zero dollars and 10% of my skills just went up 1000x"**. And this is exactly what I'm talking about - **having a vision, being able to set milestones towards that vision, keeping track of a design to maintain or control the levels of complexity as you go forward**. Those are hugely leveraged skills now compared to knowing where to put the ampersands and the stars and the brackets in Rust.  
-- [Kent Beck](https://www.youtube.com/watch?v=aSXaxOdVtAQ&t=12m30s) ([via](https://simonwillison.net/2025/Jun/22/kent-beck/))

Ta čísla jsou očividně nadsazená. Nicméně, tím jak agenti dokáží generovat stále kvalitnější kód se hodnota pouhé schopnosti "psát kód" skutečně snižuje.

A kód, který dnes dokáží agenti - _pod vedením programátora_ - vygenerovat, začíná být skutečně dobrý:

> Armin Ronacher had Claude and Claude Code do almost all of the work in building, testing, packaging and publishing a new Python library [...] [sloppy-xml-py](https://github.com/mitsuhiko/sloppy-xml-py), a lax XML parser (and violation of everything the XML Working Group hold sacred) which ironically is necessary because LLMs themselves frequently output "XML" that includes validation errors. [...]
>
> It's useful, well defined, the code is readable with just about the right level of comments, everything is tested, the documentation explains everything I need to know, and it's been shipped to PyPI.
>
> I'd be proud to have written this myself.
>
> This example is not an argument for replacing programmers with LLMs. **The code is good because Armin is an expert programmer who stayed in full control throughout the process. As I wrote the other day, a skilled individual with both deep domain understanding and deep understanding of the capabilities of the agent.**  
-- [Simon Willison](https://simonwillison.net/2025/Jun/21/my-first-open-source-ai-generated-library/)

Jinými slovy, zkušeného schopného programátora GenAI nástroje mohou zbavit rutinních úkolů, jako je fyzické psaní kódu a jeho testování. A naopak člověka bez zkušeností mohou zavést do slepé uličky, protože nebude schopen vidět problémy jako vadný design nebo bezpečnostní zranitelnosti. _Augmentation, not a replacement._

Zajímavá historická paralela: [_computer_](https://en.wikipedia.org/wiki/Computer_(occupation)) byl svého času název profese vykonávané lidmi. Nebudu překvapen, pokud jednoho dne bude _programmer_ (nebo _coder_) také jen softwarová komponenta (podobně jako např. _compiler_), a role vývojáře bude postupně mnohem více o supervizi, ladění funkcionality, použitelnosti a komunikaci s uživateli.

_Update_: Doplněn úvodní komentář k odporu zaměstanců Amazonu.

