---
date: 2026-06-27
tags:
  - ai
  - agentic-ai
  - knowledge-management
  - file-over-app
  - open-source
  - mental-health
---

# Zkušenosti s tvorbou osobní znalostní báze

V následujícím textu sdílím svou motivaci a zkušenosti s tvorbou osobní znalostní báze ([Personal Knowledge Base](https://en.wikipedia.org/wiki/Personal_knowledge_base)) s využitím různých open source nástrojů. Přestože je projekt relativně čerstvý (věnuji se mu pár měsíců), už nyní v něm nacházím velkou přidanou hodnotu.

## Od tužky a papíru k Markdownu

Posledních 7 let si dělám ručně psané poznámky do sešitu. Jsou rychlé, snadné, přirozené. Člověk není omezován klávesnicí, obrazovkou, stávkujícím softwarem, otravnými notifikacemi a podobně. Psaní mi pomáhá ujasnit si myšlenky, priority, uvolnit mentální kapacitu. Poznačit si, co bych jinak určitě zapomněl. A někdy i odreagovat emoce.

Ručně psané poznámky mají pochopitelně řadu nevýhod. Pokud škrábete tak strašně, jako jsem psal donedávna i já, může být později těžké to vůbec přečíst. (Mimochodem, přechodem na [Comenia Script](https://www.comenia-script.com/) se čitelnost mého psaní _dramaticky zlepšila_. A přeučení nebylo těžké ani zdlouhavé - za pár dnů tréninku bylo hotovo.) Dále, pokud chce člověk něco opravit nebo změnit, u fyzického psaní a kreslení to jde jen těžko. V poznámkách se taky špatně hledá, staré sešity nejsou po ruce, ztrácí se a podobně.

Zkoušel jsem proto využít různý software: poznámky ve Wordu nebo obyčejných textových souborech, později i specializované nástroje jako [Joplin](https://joplinapp.org/) nebo [Obsidian](https://obsidian.md/). Nic z toho se ale neuchytilo. Myslím, že největší překážky byly následující:

1. Můj mentální model poznámek byl příliš složitý: složité hierarchie, snaha zachytit příliš mnoho.
1. Nástroje byly buď nevhodné (Word), nebo nepohodlné (Joplin, Obsidian). Učit se pracovat s novým uživatelských rozhraním je kognitivně náročné, a navíc jsem si dost zvykl na rychlé psaní v editoru Vim (tj. bez nutnosti používat myš). (Mimochodem, [Fish shell](https://fishshell.com/docs/current/cmds/fish_vi_key_bindings.html) umí emulovat Vim i v terminálu!) Obsidian sice nějakou minimální emulaci Vimu nabízel, ale mým potřebám nestačila.
1. Chyběl mi jednoduchý způsob jak k poznámkám přistupovat z různých zařízení (smartphone, PC, laptop) bez nutnosti vytvářet si někde účet a posílat data do cloudu. Z toho důvodu mě nelákaly aplikace jako Notion nebo Evernote, kde zároveň nemusí být snadné svá data později exportovat.

> Simplicity changes behavior.  
> -- [BJ Fogg: Fogg Behavior Model](https://www.behaviormodel.org/videos)

<!-- more -->

Nejvíc se mi nakonec osvědčily obyčejné textové soubory v Markdownu, protože _snadno zapadly do existujícího workflow_. Mohl jsem je psát v editoru VS Code, na který jsem zvyklý z programování. VS Code má navíc dobrý [emulátor Vimu](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim) a zároveň dokáže Markdown i vykreslit pomocí zkratky CTRL+Shift+V.

Digitalizaci jsem začal příležitostným psaním deníku _když jsem cítil potřebu_ si něco poznačit nebo zpracovat. Líbila se mi možnost přidávat odkazy a obrázky, včetně rychlejšího vyhledávání. To fungovalo, bylo to užitečné, bez tlaku teď něco dělat jinak nebo hromadně přepisovat. Jeden soubor v Markdownu. Sice nebyl přístupný na dalších zařízeních, ale tahle _jednoduchost a nenárokovost_ byla tím prvním krokem, co jsem potřeboval. Sešit na rychlé poznámky mi zůstal, deník se stal příležitostným digitálním doplňkem.

## Motivace pro znalostní bázi

V posledních letech jsem opakovaně cítil potřebu soustředit svoje poznámky a související artefakty (typicky obrázky) na jedno místo. Hledat věci po různých adresářích nebo v sešitě začalo být dost otravné. Taky jsem měl chuť se občas nad něčím víc zamyslet a případně to nasdílet i veřejně. Před rokem a čtvrt mě proto [Simon Willison inspiroval začít psát blog](../posts/zacinam-psat-blog.md).

Přemýšlel jsem, jak na to jít jednoduše, a kombinace GitHub Pages + Markdown zafungovala výborně. Ze začátku mi stačilo jen `README.md`. Jak se ale blog, resp. web rozšiřoval, přešel jsem na [sestavení pomocí Material for MkDocs](../posts/upgrade-blogu.md). Nástroj je napsaný v Pythonu, zdrojové soubory webu se píší v Markdownu. Opět to zapadlo.

Řada poznámek zůstala nicméně rozesetá na různých místech, plus mě napadala spousta věcí, které byly čistě interní, nebo potřebovaly ještě uzrát. Zkusil jsem si proto udělat gitovský repozitář "notes" pro deník a pár dalších poznámek, ale stále to nebylo ono.

## Experiment s "LLM Wiki"

Začátkem dubna [Andrej Karpathy zveřejnil svůj příspěvek o LLM Knowledge Bases](https://x.com/karpathy/status/2040470801506541998), který mě zaujal. Pointou je, že znalostní bázi tvoří a udržuje AI agent. Primární rolí uživatele je vybírat datové zdroje.

Předhodil jsem tedy [LLM Wiki idea file](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (z Karpathyho příspěvku výše) agentům Claude Code a Codex. Jako datové zdroje jsem jim dal repozitář svého blogu, resp. webu a pár dalších souborů s poznámkami.

A musím říct, že výsledky byly zajímavé. Agenti dokázali v textu najít řadu souvislostí, které mě nenapadly. Bylo to jako když se na ty stejné informace _podívá někdo další, jinýma očima_.

Zároveň jsem ale brzy narazil na potíže, např.:

- Jak zajistit, že odkazy, které agent generuje (tzn. prolinkování dokumentů), skutečně existují a že se nějakou změnou nerozbily? Jistě by šlo najít, příp. napsat nějaký custom software, co to vyřeší, ale byla to komplexita navíc, která mě v tu chvíli spíš odrazovala.
- Jak snížit riziko, že agent vytváří nepravdivé informace a závěry? Nelíbí se mi představa nechat běžet agenta na svém počítači pod svým uživatelským účtem v plně autonomním módu (zejména kvůli rizikům jako Prompt Injection nebo Supply Chain útokům; způsoby izolace teprve zkoumám). Každý nový dokument nebo změnu jsem tedy poctivě zkontroloval a v tom množství to byla dost únavná práce. Moc mě to nebavilo.
- Nelíbilo se mi, jak začíná narůstat spotřeba tokenů a s tím i cena za práci. Modely volám přes [OpenRouter API](https://openrouter.ai/) (měsíční předplatné ChatGPT nebo Claude se mi nevyplácí). Oproti běžnému "kódění" s Claude Code začala spotřeba citelně stoupat. Jistě, dá se argumentovat, že závisí na ceně modelu, reasoning effort, import velkého množství dokumentů nebude příliš častý, a tak dále. Přesto jsem začal mít otazník u škálování z pohledu ceny.

Přišlo mi, že komplexita začala pomalu stoupat, namísto, aby klesala. Koncept LLM Wiki pro mě v danou chvíli nebyl dostatečně jednoduchý a pohodlný na realizaci. Rozhodl jsem se proto zkusit jiný přístup: Začít budovat znalostní bázi od nuly, manuálně, a __přidat práci agenta jen tam, kde má největší smysl__, kde bude agent komplexitu snižovat.

## Projekt "Knowledge"

Vytvořil jsem proto nový repozitář "knowledge". Rozdíl oproti předchozím pokusům nebyl až tak v obsahu, jako spíš v mém přístupu. Namísto statického odkladiště informací jsem chtěl živou, aktivně udržovanou bázi, která bude užitečná pro to, co právě řeším. Minimalistický praktický obsah, který může v budoucnu využít i nějaký "osobní AI asistent".

Chvíli jsem si s tím hrál a experimentoval, nicméně k zásadnímu mi pomohly 2 nástroje:

1. (Opět) _Material for MkDocs_: Sestavit poznámky do podoby přehledného a oku lahodícího webu byl citelný upgrade. S pěkným webem jsem dostal i větší chuť se mu věnovat. Vyřešil se tím i problém s validací interních odkazů: když MkDocs narazí na neplatný odkaz, vypíše warning, příp. jde vynutit i error (pomocí `mkdocs build --strict`). Skvělou vlastností je [funkce vyhledávání](https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-search/).
1. _Tailscale_: Díky [Tailscale jsem si vytvořil soukromou VPN](../posts/soukroma-vpn-s-tailscale.md), na které jde vytvořený web rovnou nasdílet (pomocí funkce Tailscale Serve). Znalostní bázi mám tak přístupnou na všech zařízeních, neustále po ruce.

Vznikl mi tak **soukromý bezpečný digitální prostor**, kde mě neotravují žádné notifikace ani reklamy, nikdo mi nic netlačí a nepodsouvá. Mám prostor, kde se můžu soustředit na to, co je _důležité pro mě_. Prostor, kde můžu mít přehledně sepsané a utříděné priority, snadno si je připomínat, aktualizovat a rozvíjet.

Je jasné, že každý z nás potřebuje něco trochu jiného. Mě osobně teď třeba pomáhají přehledy a vizualizace. Viz příklad níže:

Co mě nabíjí:

!!! tip "Trávit čas mezi aktivními lidmi"

!!! tip "Procházky, výlety do přírody, variabilita, změna prostředí"

!!! tip "Pracovat na něčem, co přináší mi skutečnou hodnotu"

Co mě vyčerpává:

!!! danger "Trávení času u počítače"

!!! danger "Někoho o něčem přesvědčovat"

!!! danger "Chaos, mikromanagement, nesplněné sliby"

_Vytvořeno pomocí [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)_

Hlavní strana báze je pro mě takový rychlý rozcestník, ke kterému se každý den vracím. Dělám si poznámky do deníku, občas k nějaké technologii, se kterou zrovna experimentuji. Je to úzce svázané se snahou budovat a posilovat zdravou pravidelnost, mentální regeneraci a podobně. O to třeba v nějakém dalším článku.

## Použité technologie

Pro přehled přidávám stručný seznam použitých technologií s komentáři:

- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/): Nástroj pro vytvoření webové podoby znalostní báze. Dokumenty se píši v Markdownu. Vyhovuje mi snadné použití, moderní vzhled, řada užitečných pluginů jako vyhledávání na straně klienta. V dohledné době plánuji [nahradit nástupnickým nástrojem Zensical](../posts/zensical-jako-nastupce-material-for-mkdocs.md).
- Textový editor, v mém případě VS Code: Pointou je, aby tvorba znalostní báze co nejsnáze zapadla do existujícího workflow. Vyhovují mi vlastnosti jako již zmíněná emulace Vimu, vestavěný terminál nebo otevření okna webového prohlížeče přímo v editoru.
- Git: Jsem zvyklý projekty verzovat. Git se zároveň hodí jako nástroj pro sdílení a práci na různých zařízeních (PC, laptop). Sdílení probíhá prostřednictvím bare repozitáře na vlastním serveru, kde se web i [automaticky sestaví a nasadí pomocí `post-receive` hooku](../posts/git-post-receive-hook.md).
- [Tailscale](https://tailscale.com/): Proprietární technologie VPN, která staví na protokolu [WireGuard](https://www.wireguard.com/). Pomocí [Tailscale Serve](https://tailscale.com/docs/features/tailscale-serve) sdílím webové stránky a lokální služby v rámci VPN.
- Google Docs: Editovat znalostní bázi (Git repo) na smartphonu by nejspíš šlo, ale ne moc pohodlně. Pro rychlé poznámky a odkazy využívám Google Docs, které jsou dostupné na všech zařízeních. Jednou za čas poznámky přepíšu. Je to trochu opruz, ale dá se to zvládnout.

## Otevřené otázky

- _Bezpečné využívání AI agentních systémů_. Velké jazykové modely a AI agentní systémy přináší řadu rizik, které je třeba brát v potaz. Viz [OWASP Top 10 Risk & Mitigations for LLMs and Gen AI Apps](https://genai.owasp.org/llm-top-10/):
    - Při tvorbě znalostní báze, např. při psaní deníku, se nechci nijak cenzurovat. Objevují se zde tedy dost osobní informace, a to nejen o mě, ale potenciálně i o lidech, které znám. Říkám si tedy jak eliminovat, nebo alespoň snížit riziko úniku těchto dat.
        - Ideální by bylo využívat jen modely běžící na mém vlastním hardware. Existuje dostatečně "malý" a zároveň výkonný model, zejména s ohledem na češtinu?
        - Služba OpenRouter nabízí vynucení politiky [Zero Data Retention](https://openrouter.ai/docs/guides/features/zdr), případně [Guardrails](https://openrouter.ai/docs/guides/features/guardrails/overview). Samozřejmě nezbývá, než poskytovatelům věřit. Je to akceptovatelné řešení?
    - Kontrolovat a schvalovat příkazy a změny, které AI agent provádí, je kognitivně vyčerpávající. Rád bych měl proto možnost spustit agenta v plně autonomním režimu. Následující dvě řešení mě zaujaly, nicméně bude potřeba ověřit si technické detaily a praktičnost:
        - [Ubuntu Workshop](https://ubuntu.com/workshop/docs/): neprivilegované systémové kontejnery vytvářené pomocí LXD.
        - [Docker Sandboxes](https://docs.docker.com/ai/sandboxes/): virtuální stroje vytvářené pomocí microVM.

Výše zmíněné otázky jsou předmětem mého dalšího průzkumu.
