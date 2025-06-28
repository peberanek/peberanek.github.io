---
date: 2025-06-28
---

# Upgrade webu pomocí Material for MkDocs

Jak už jsem psal dříve, [Simon Willison mě inspiroval začít psát blog](../posts/zacinam-psat-blog.md). Jelikož jsem si nebyl jistý, jestli u toho dlouhodobě vydržím, snažil jsem se celou akci maximálně zjednodušit. Pro hosting jsem využil [GitHub Pages](https://pages.github.com/), protože jsou zdarma, a dokáží pěkně vyrendrovat obyčejný Markdown. Není tedy třeba psát žádný HTML kód, řešit šablony apod. Člověk se může hned soustředit na psaní a na celý blog ve finále stačí jen jedno dlouhé `README.md`.

Zároveň jsem v té době řešil problém se svým CVčkem: měl jsem ho pěkně sice vysázené pomocí [Scribusu](https://www.scribus.net/) (open-source obdoba Adobe InDesign), ale upravovat ho byla docela pruda. Hodil by se mi nějaký formát - obyčejný texťák, který by šel snadno verzovat pomocí Gitu, a zároveň by vypadal slušně při tisku. Zde se opět osvědčil Markdown, který je navíc v souladu s filozofií, že [soubor je víc než aplikace](../posts/soubor-je-vic-nez-aplikace.md). Do hlavičky blogu mi tedy přibyl odkaz na `cv.md`, které šlo v rozhraní webového prohlížeče snadno převést do PDF i vytisknout. Skvělé.

Jak se ale blog začal rozrůstat, bylo na čase začít řešit jednotný vzhled všech stránek, prolinkování článků, tvorbu náhledů, tagování apod. Při hraní si s knihovnou [Textual](https://www.textualize.io/) (tvorba sofistikovaných TUI) jsem narazil na jejich [blog](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/), který využívá [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

<!-- more -->

Věděl jsem, že se používá na tvorbu dokumentace (např. [FastAPI](https://fastapi.tiangolo.com/) nebo [pydantic](https://docs.pydantic.dev/latest/)), nicméně blog pro mě byla novinka. Vizuálně vypadal dobře, a když jsem zjistil, že stránky se píší v Markdown, šel jsem to hned vyzkoušet.

## Instalace

Jedná se balíček programovacího jazyka Python, takže instalace pomocí [uv](https://docs.astral.sh/uv/) je přímočará. V existujícím adresáři `peberanek.github.io` jsem spustil:
``` sh
uv init --bare . # (1)!
uv add mkdocs-material
uv run mkdocs new .
```

1.  uv vytvoří pouze `pyproject.toml`.

Tím se vytvoří virtuální prostředí (`.venv/`) s balíčkem `mkdocs`, jeho konfigurací a základní strukturou v adresáři `docs/`.

```
.
├── docs
│   └── index.md
├── mkdocs.yml
├── pyproject.toml
├── uv.lock
└── .venv/
```

!!! Poznámka

    Zkoušel jsem `mkdocs-material` instalovat i jako tool. V tom případě je potřeba použít tento příkaz:
    ``` sh
    uv tool install mkdocs --with mkdocs-material
    ```

## Poznámky

Výsledný zdrojový kód blogu (včetně nastavení a obsahu) si můžete prohlédnout [v repozitáři peberanek.github.io](https://github.com/peberanek/peberanek.github.io). Níže uvedu pár věcí, na které jsem během upgradu narazil:

* Opět z důvodu jednoduchosti jsem chtěl mít blog jako první stranu webu. Toho lze docílit pomocí nastavení `blog_dir`. Viz [konfigurace jako Blog only](https://squidfunk.github.io/mkdocs-material/setup/setting-up-a-blog/#blog-only). Skvělé je, že i přesto se dají přidávat další stránky, jako např. zmíněné [CV](https://peberanek.github.io/cv/).
* Odkazování na jiný článek je potřeba udělat pomocí relativní cesty (např. `../posts/clanek-xyz.md`). Při odkazování pomocí `links` je ale třeba uvádět `posts/clanek-xyz.md`, což je trochu matoucí. Odkazy ve vloženém HTML kódu (např. audio) nefungují spolehlivě ze všech míst (buď fungují na hlavní straně, nebo ve článku), viz [Open Weights vs Open Source AI](../posts/open-weights-vs-open-source-ai.md). V tomto případě by bylo asi lepší hostovat audio soubory samostatně.
* By default, v odkazech na články zůstává diakritika, což se mi nelíbí (nechci řešit chyby spojené s enkódováním). Funkce, která se o tvorbu odkazů stará, lze naštěstí přenastavit:

    ``` yaml title="mkdocs.yml"
    plugins:
      - blog:
          post_slugify: !!python/object/apply:pymdownx.slugs.slugify
            kwds:
              case: lower
              percent_encode: false
              normalize: 'NFD'
    ```

* Musím ocenit možnost automatického nastavení světlého nebo tmavého tématu, viz [Automatic light / dark mode](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/?h=automatic#automatic-light-dark-mode).
