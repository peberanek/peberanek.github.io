---
date: 2026-04-18
tags:
  - blogging
  - open-source
  - software-development
---

# Zensical jako nástupce Material for MkDocs

[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) je populární framework pro generování statických webových stránek, resp. dokumentace, postavený na [MkDocs](https://www.mkdocs.org/). Sám ho používám pro [tvorbu tohoto webu](../posts/upgrade-blogu.md) a s ergonomií i výsledkem jsem velmi spokojen. Překvapilo mě proto zjištění, že **tým okolo Material for MkDocs se rozhodl v dalším vývoji nepokračovat** a vytvořit zcela nový nástroj nazvaný [Zensical](https://squidfunk.github.io/mkdocs-material/blog/2025/11/05/zensical/). Ze série jejich článků (viz předchozí odkaz) se však zdá, že se jedná o dlouhodobě plánované a odůvodněné rozhodnutí.

Narazili např. na technické limity knihovny pro vyhledávání na straně klienta Lunr.js, která je navíc dlouhodobě nepodporovaná. K tomu se jim nepodařilo najít dostatečně dobrou alternativu, takže se rozhodli postavit vlastní vyhledávací engine. Dále je zmíněno potenciálně [pomalé sestavení dokumentace s MkDocs (klidně 8 i 20 minut)](https://github.com/mkdocs/mkdocs/issues/3695#issuecomment-2093299518) v případě rozsáhlých projektů (což se mě naštěstí netýká).

Daleko větším problémem je však **situace okolo samotného projektu MkDocs** jakožto klíčové závislosti: **projekt se stal dlouhodobě neudržovaný**, komunikace ohledně jeho správy byla poněkud nejasná a nová verze MkDocs 2 navíc nemá v plánu podporovat pluginy, které jsou pro fungování Material for MkDocs klíčové. Tým tento projekt proto vyhodnotil jako "supply chain risk".

Nakonec se rozhodli od MkDocs oprostit a vytvořit výše zmíněný Zensical. Ten je napsaný z většiny v Rustu, nicméně je dostupný na pypi.org a dá se [nainstalovat třeba pomocí `uv`](https://zensical.org/docs/get-started/#install-with-uv):

```sh
uv init
uv add --dev zensical
uv run zensical
```

Mimochodem, přepis funkcionality do Rustu následuje aktuální trend, který reprezentují projekty jako [Ruff](https://github.com/astral-sh/ruff), již zmíněný [uv](https://github.com/astral-sh/uv) nebo částečně [Pydantic](https://github.com/pydantic/pydantic).

Těší mě, že by měla být (z většiny) zajištěna **zpětná [kompatibilita](https://zensical.org/compatibility/)**:

> Compatibility with Material for MkDocs is our top priority. We understand that switching to a new static site generator can be challenging, especially for large projects with many customizations. Therefore, we've put significant effort into ensuring that Zensical understands `mkdocs.yml` configuration files, so that you can build your projects with minimal changes.  
> -- [Zensical – A modern static site generator](https://squidfunk.github.io/mkdocs-material/blog/2025/11/05/zensical/#maximum-compatibility)

Více viz [detailní **Feature Parity**](https://zensical.org/compatibility/features/)

Material for MkDocs by měl dostávat **podporu přibližně do listopadu 2026**:

> We're aware that transitioning takes time, which is why we commit to supporting Material for MkDocs for at least the next 12 months, fixing critical bugs and security vulnerabilities as needed.  
> -- [Zensical – A modern static site generator](https://squidfunk.github.io/mkdocs-material/blog/2025/11/05/zensical/#looking-ahead)

Zensical je k dispozici pod permisivní MIT licencí (stejně jako Material for MkDocs). Zajímavou změnou je **odklon od sponsorware modelu** (kde některé funkce byly jen pro sponsory) k nabídce pro profesionální použití pomocí Zensical Spark.

Vývoj plánuji dále sledovat a rozhodně jim přeju, ať se tenhle model osvědčí.
