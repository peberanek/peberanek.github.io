---
date: 2026-01-02
tags:
  - ai
  - claude-code
  - ai-agents
  - automation
  - blogging
  - python
  - software-development
---

# Generování tagů s Agent Skills pro Claude Code

Už dříve jsem psal o [asistentovi v Open WebUI](../posts/ai-asistent-v-open-webui.md), který mi pomáhá generovat tagy pro články na tomto blogu. Vzhledem k tomu, že mám články jako lokální soubory, bylo by jednodužší použít např. Claude Code, který má text článku rovnou k dispozici, bez nutnosti cokoliv manuálně kopírovat do GUI nebo extrahovat seznam tagů z webu. Zároveň mě zaujala nová vlastnost zvaná [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills), která umožňuje agentovi přidávat specializované schopnosti. Níže sdílím své poznámky ke generování tagů právě s pomocí Claude Code.

!!! Poznámka

    Kompletní zdrojový kód je [k dispozici na GitHubu](https://github.com/peberanek/peberanek.github.io).

## Definice vlastního skillu

Nový skill je jednoduše adresář (v mém případě `generate-tags/`), který obsahuje `SKILL.md`, příp. další pomocné soubory. Stačí mi, aby byl skill přístupný jen pro daný repozitář:
``` title="peberanek.github.io/"
.claude/
└── skills
    └── generate-tags
        ├── scripts
        │   └── list_tags.py
        └── SKILL.md
...
```
(Skill lze, nicméně, [zpřístupnit i šířeji](https://code.claude.com/docs/en/skills#where-skills-live).)

Soubor `SKILL.md` obsahuje minimální potřebné instrukce. Jako první jsou definována metadata (tzv. _frontmatter_ ve formáty YAML), která se načítají automaticky. Z nich agent pozná, zda má daný skill použít:
```yaml title="SKILL.md"
---
name: generate-tags
description: Generate the list of tags for a blog post.
---
```

<!-- more -->

Potom je dobré poskytnout další detaily:
````title="SKILL.md"

List existing tags using the following script:
```sh
uv run .claude/skills/generate-tags/scripts/list_tags.py
```

Use the existing tags to update `tags` in the blog post YAML frontmatter. Here is an example of an updated frontmatter:
```yaml
date: 2025-10-11
tags:
  - ai
  - ai-agents
  - ai-predictions
  - sam-altman
```

````

Z textu výše je patrné, že adresář `scripts/` obsahuje skript, díky kterému získá agent seznam existujících tagů aniž by musel pokaždé procházet všechny články (což může být pomalé a drahé). Tímto skriptem se blíže zabývá další kapitola.

## Tvorba pomocného skriptu

Nejjednodužší bylo požádat Claude Code, ať mi pomůže skript vytvořit. Než číst fůru nového kódu, víc se mi osvědčilo postupovat iterativně, a nejprve nechat agenta vysvětlit, jak by postupoval a rovnou ho korigovat. Líbí se mi přístup, že _já přemýšlím, rozhoduji, kontroluji a agent píše_ (Simon Willison něco podobného citoval [na svém blogu](https://simonwillison.net/), bohužel se mi ten post nedaří najít).

První návrh se mi nelíbil. Místo použití balíčku PyYAML se agent rozhodl parsovat metadata pomocí regexu. Pocitově moc složité a křehké. Instruoval jsem ho tedy, že může používat balíčky 3. stran a nainstalovat je pomocí `uv add`. Kód už byl o něco jednodužší a čistější, ale stále nic moc. Pocitově moc dlouhé. Postupným doptáváním jsme se dostali k tomu, že existuje balíček [`python-frontmatter`](https://github.com/eyeseast/python-frontmatter), _který jsem do té doby neznal_ a který implementaci výrazně zjednodušil.

Nakonec jsem agenta instruoval, aby kód zkontroloval pomocí nástrojů [`ruff` (linter a formatter)](https://docs.astral.sh/ruff/) a [`ty` (type checking)](https://docs.astral.sh/ty/). Výsledek už vypadá solidně:

```py title="list_tags.py"
"""
List all unique tags from blog posts.

Scans all markdown files in docs/posts/ and extracts tags from their
YAML frontmatter, then outputs a sorted, deduplicated list.
"""

from typing import cast

import frontmatter
from pathlib import Path


def main() -> None:
    """Main function to list all tags."""
    posts_dir = Path("docs/posts")
    all_tags: set[str] = set()

    for md_file in posts_dir.glob("*.md"):
        post = frontmatter.load(str(md_file))
        if "tags" in post.metadata:
            tags = post.metadata["tags"]
            if isinstance(tags, list):
                all_tags.update(cast(list[str], tags))

    print(sorted(all_tags))


if __name__ == "__main__":
    main()
```

## Použití

Nyní už jen stačí požádat Claude Code, aby vygeneroval tagy pro článek na kterém pracuji (konkrétní soubor lze vybrat po stisknutí `@`). Aby nemusel agent pokaždé žádat o svolení k použití skillu, je možné ho automaticky povolit:
```json title=".claude/settings.json"
{
  "permissions": {
    "allow": ["Skill(generate-tags)"]
  }
}
```

!!! Poznámka

    Třebaže se mi povedlo podobným způsobem nastavit, aby agent nemusel žádat o svolení při spouštění příkazů jako `uv run ruff` nebo `uv run ty`, pro konkrétní adresáře nebo skripty (např. `"Bash(uv run .claude/skills/:*)"`) se mi to nedaří.

Požádat agenta, aby vygeneroval tagy vyžaduje nějaké psaní a chvíli mu trvá, než si naplánuje potřebné kroky. Asistent v Open WebUI věděl hned, co má dělat. Na druhou stranu, výsledný seznam vypadá o něco kvalitněji (nenechávám agenta, aby vymýšlel nové tagy, což je mentálně jednodužší na kontrolu). Také není třeba nikam nic kopírovat. A hlavně tento skill zapadá do dosavadního workflow, kdy mi agent pomáhá s opravou gramatiky, překlepy nebo překlady. Takže jsem spokojen.

## Další odkazy

* [Agent Skills (Claude Code Docs)](https://code.claude.com/docs/en/skills)
* [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
