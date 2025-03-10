[Blog](/README.md) ⋅ [Curriculum Vitae](/cv.md) ⋅ [Email](mailto:beranek@duck.com) ⋅ [GitHub](https://github.com/peberanek) ⋅ [X (Twitter)](https://x.com/peberanek)

# Blog

## 2025-03-08

### AI jako akcelerátor toxické kultury

[AI Is About to Make Social Media (Much) More Toxic](https://www.theatlantic.com/technology/archive/2023/05/generative-ai-social-media-integration-dangers-disinformation-addiction/673940/) ([via](https://www.youtube.com/watch?v=tLxfLjebJV8)):
> ... whatever actions AIs may _one day_ take if they develop their own desires, they are already being
used instrumentally by social-media companies, advertisers, foreign agents, and
regular people—and in ways that will deepen many of the pathologies already
inherent in internet culture. On Sydney’s list of things it might try, stealing launch
codes and creating novel viruses are the most terrifying, but making people argue
until they kill one another is something social media is already doing.  

Článek je z května 2023 a některé predikce stále vypadají trochu nadsazené. Na druhou stranu, k velkým škodám ve společnosti není třeba, aby se mezi sebou začali lidi zabíjet. Úplně stačí, když se spolu rozhádáme natolik, že přestaneme spolupracovat, komunikovat a naše společnost se dříve nebo později rozpadne nebo podlehne nátlaku a vlivu zvenčí.

## 2025-03-07

### Open-source AI Sandbox

<img src="/media/open_webui.jpg" alt="AI Sandbox screenshot" width="980" style="max-width: 100%;">

#### Motivace

V roli metodika AI na Univerzitě Karlově mě překvapilo, jak obtížné je i pro takto velkou instituci získat přístup k enterprise verzi chatbotů jako ChatGPT. (Naši uživatelé sice mají k dispozici Microsoft Copilot for Education. Ten je ale v řadě případů nedostačující.) Generativní AI je nová technologie jejíž přínosy (i rizika) teprve objevujeme, takže vidina finančně nákladné investice s nejistým výsledkem není moc lákavá. Zároveň si firmy kladou vysoké požadavky na minimální počet licencí a cenu.

S tím souvisí i riziko neefektivního využívání, jak se přesvědčili např. na Univerzitě Palackého v Olomouci. Pořídili překladač DeepL Pro Advanced for Teams za ~12500 EUR/rok (52 licencí), aby nakonec zjistili, že to byla slepá ulička:

> \- Licencí bylo málo, každý chtěl licenci jen pro sebe  
> \- Mnozí z těch, kdo chtěli licenci, si ji nakonec neaktivovali, zůstali viset v systému  
> \- Ti, kteří licenci dostali, ji pořádně nevyužívají, cca 50 přeložených dokumentů měsíčně  
> \- Ti, kteří ji chtějí využívat intenzivně, jsou omezeni 20 soubory měsíčně  
-- [Nasazení překladače DeepL na UP (příspěvek na konferenci EUNIS-CZ 2024)](https://euniscz.sharepoint.com/:p:/r/sites/vykonny-vybor/Sdilene%20dokumenty/Konference/Hlavn%C3%AD%20konference%20%C5%A0pindler%C5%AFv%20Ml%C3%BDn/2024%20-%2027-29_5/soubory%20na%20web/27.%205.%20pond%C4%9Bl%C3%AD/UPOL%20EUNIS%202024%20DeepL.pptx)

Komplikované bylo i zařídit přihlašování pomocí univerzitního SSO. Vydali se proto cestou vývoje vlastní aplikace využívající DeepL API. Díky tomu mají ke službě přístup všichni zaměstnanci. V rámci finančního modelu pay-as-you-go se (vyjma několika pevných poplatků) platí za počet přeložených znaků. Za uživatele, co aplikaci nevyužívají, se neplatí nic. Uživatelé mají zároveň virtuální peněženku s kreditním limitem, který je motivuje k šetrnému využívání.

S podobným nápadem, ale ve formě _chatbota_, přišli na americkém Harvardu. Na konci roku 2023 řešili situaci, kdy jim firmy jako OpenAI nebyly schopné nebo ochotné nabídnout akceptovatelné smluvní podmínky. Vytvořili si proto vlastní aplikaci s názvem Harvard AI Sandbox (více viz [video prezentace](https://www.youtube.com/watch?v=61zn8Q6lK08)):

> The AI Sandbox provides a secure environment in which to explore Generative AI, mitigating many security and privacy risks and ensuring the data entered will not be used to train any vendor large language models (LLMs). It offers a single interface that enables access to the latest LLMs from OpenAI, Anthropic, Google, and Meta.  
-- [Harvard AI Sandbox](https://www.huit.harvard.edu/ai-sandbox)

Výhodou API bývá i závazek firem, že nebudou využívat vložená data k dalšímu trénování modelů (je třeba vždy ověřit v obchodních podmínkách).

Nutno podotknout, že _výsledný chatbot není náhradou jedna ku jedné za ChatGPT, Claude nebo Gemini_. Tyto produkty budou nejspíš vždy o krok napřed. Na druhou stranu ale _stačí, aby byl dostatečně dobrý pro praktické využití_. AI Sandbox tak může pokrýt základní poptávku nebo sloužit při výuce, a drahé produkty pořídit těm, kdo je skutečně využijí.

#### Implementace

Nevím o tom, že by Harvard zveřejnil zdrojový kód své aplikace. Zároveň mám dlouhodobě dobré zkušenosti s open-source softwarem. Nabízí se tak otázka, zda už náhodou neexistuje dostatečně dobrá alternativa, použitelná přinejmenším jako proof of concept.

Hlavní kritéria výběru:

1. Jedná se o populární projekt s aktivním vývojem. Kód je plně auditovatelný. Ideálně nabízí i enterprise support.
1. Přes API lze využívat pokročilé modely od OpenAI, Anthropic a Google (případně i další).
1. Aplikace je víceuživatelská, s jednoduchou administrací a s rozdělením uživatelů podle rolí a skupin. Ideálně s přihlašováním pomocí SSO.
1. Lze sledovat využívání modelů, a u placených omezit útratu. Ideálně formou již zmíněné peněženky.
1. Lze vkládat soubory (text, obrázky, tabulky).

Doplňková kritéria:

1. Lze využívat lokálně běžící open-source modely.
1. Snadná rozšířitelnost o další funkcionalitu. Ideálně pomocí Pythonu.
1. Podpora různých modalit, nejen text, ale i generování obrázků, hlasového vstupu s výstupu.
1. Možnost nasazení na serveru i na desktopu (pro maximální soukromí).
1. Uživatelské rozhraní je i v češtině.

Postupně jsem prošel a vyzkoušel řadu aplikací (mimo jiné [LibreChat](https://github.com/danny-avila/LibreChat), [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm), [Jan](https://github.com/janhq/jan), [GPT4All](https://github.com/nomic-ai/gpt4all), [Text generation web UI](https://github.com/oobabooga/text-generation-webui)) a výše uvedená kritéria (s výjimkou peněženky) nyní nejlépe splňuje [Open WebUI](https://github.com/open-webui/open-webui). Běh open-source modelů zajišťuje [Ollama](https://github.com/ollama/ollama) (z důvodu jednoduchosti; od kolegy jsem však slyšel, že plánují přejít na [vLLM](https://github.com/vllm-project/vllm)).

Open WebUI podporuje defaultně jen připojení na OpenAI a s ní kompatibilní API. Pro připojení k Anthropic a Google je potřeba využít dodatečné funkce, ať už vlastní, nebo [vytvořené komunitou](https://openwebui.com/functions). Nevýhodou je, že je to kód navíc, který je potřeba zkontrolovat a udržovat. Na druhou stranu to vypadá, že možnosti rozšířitelnosti pomocí [Tools, Functions & Pipelines](https://docs.openwebui.com/features/plugin/) jsou [zajímavé](https://www.reddit.com/r/LocalLLaMA/comments/1h4mq5f/supercharged_openwebui_my_magical_toolkit_for/).

Zkušenosti s nasazením a pilotním provozem plánuji nasdílet v některém z budoucích příspěvků.

#### Jak si AI Sandbox vyzkoušet?

* Projekt [E-infra](https://www.e-infra.cz/) hostuje [testovací instanci Open WebUI](https://chat.ai.e-infra.cz/) s několika open-source modely. K přihlášení mi stačilo mít vytvořený účet v rámci [MetaCentra CESNETu](https://www.metacentrum.cz/cs/VO/metavo/index.html).
* Pro instalaci na vlastním serveru jsem vytvořil jednoduchý [návod](https://github.com/peberanek/ai-sandbox) včetně Docker Compose.

## 2025-03-05

### llm

Dneska jsem vyzkoušel nástroj do příkazové řádky, nazvaný jednoduše [llm](https://llm.datasette.io/en/stable/). Jednou z výhod je, že dokáže volat i lokální modely běžící přes [Ollamu](https://ollama.com/).

> A CLI utility and Python library for interacting with Large Language Models, both via remote APIs and models that can be installed and run on your own machine.
  
```bash
llm "Tell me a joke about LLMs."
```

Nainstaloval jsem přes [uv](https://docs.astral.sh/uv/) ([možno použít i pip](https://llm.datasette.io/en/stable/setup.html#installation)):
```bash
uv tool install llm
```

Mám OpenAI API Key, tak jsem ho hned využil:
```bash
llm keys set openai
```

Vypsat dostupné modely lze následovně:
```bash
llm models default  # defaultni model je gpt-4o-mini
llm models  # vypise vsechny modely
```

Interaktivní chat:
```bash
llm chat
```

Skvělé je, že pomocí [pluginů](https://llm.datasette.io/en/stable/plugins/index.html) lze připojit [řadu dalších modelů](https://llm.datasette.io/en/stable/plugins/directory.html), včetně již zmíněné Ollamy (tu je potřeba mít nainstalovanou, spouštěnou a mít stažený příslušný model):
```bash
llm install llm-ollama
llm "Tell me a joke about LLMs." -m llama3.2
```

## 2025-03-03

### Soubor je víc než aplikace

Před nějakou dobou jsem zkoušel [Obsidian](https://obsidian.md/). I když jsem u něj nakonec nezůstal (kvůli nedostatečné emulaci editoru Vim), tak musím ocenit, že moje poznámky ukládal jako obyčejné textové soubory. Můžu je tak editovat třeba ve VSCode:

> File over app is a philosophy: if you want to create digital artifacts that last, they must be files you can control, in formats that are easy to retrieve and read. Use tools that give you this freedom.
>
>File over app is an appeal to tool makers: accept that all software is ephemeral, and give people ownership over their data.  
>-- [Steph Ango: File over app](https://stephango.com/file-over-app)

K nápadu aplikaci vyzkoušet mě přivedl Andrej Karpathy a jeho [Love letter to Obsidian](https://x.com/karpathy/status/1761467904737067456):

> \- Your notes are simple plain-text markdown files stored locally on your computer. Obsidian is just UI/UX sugar of pretty rendering and editing files.  
> \- Extensive plugins ecosystem and very high composability with any other tools you wish to use because again it's all just plain-text files on your disk. [...]  
> \- There are no attempts to "lock you in", actually as far as I can tell Obsidian is completely free of any user-hostile dark patterns.  

Obdobnou filozofii razí i [Plain Text Accounting (PTA)](https://plaintextaccounting.org/). Konkrétně už řadu let využívám [Beancount](https://plaintextaccounting.org/). Takhle vypadá jednoduchý záznam, resp. transakce:

```
2024-11-12 * "Vstupenka na vyhlidkovou vez"
  Majetek:Banky:CSOB:Bezny-ucet  -140 CZK
  Vydaje:Ostatni
```

Díky tomu, že je vše uložené v obyčejném textovém souboru, mohou nad ním pracovat standardní unixové nástroje jako `git`, `grep` nebo `sed`.

Navíc, Beancount je psaný v Pythonu a dá se s ním řada věcí automatizovat, třeba [import transakcí](https://github.com/beancount/beangulp). Vedle manuálního stahování nabízí některé instituce i API. Dřív jsem si s tím trochu hrál a napsal vlastní nástroj [Beanclerk](https://github.com/peberanek/beanclerk) (zveřejnil jsem k tomu i klienty pro [Fio banku](https://github.com/peberanek/fio-banka) a [Banku Creditas](https://github.com/peberanek/creditas)). Dneska bych to nejspíš udělal jinak, ale nástroje vesele slouží dodnes.

Textové soubory jsou nakonec výhodou i pro velké jazykové modely, třeba ve formě nějakého agenta. Nemusí se jinak zvlášť trénovat nebo data extrahovat, jednoduše si je přečtou.

## 2025-02-26

### Začínám psát blog

> You should start a blog. Having your own little corner of the internet is good for the soul!  
-- [Simon Willison: What to blog about](https://simonwillison.net/2022/Nov/6/what-to-blog-about/)

Říkám si, že by bylo fajn mít místo pro sdílení myšlenek a věcí, co mě zaujaly. Mít nějaký online deník, ke kterému bych se mohl snadno vracet nebo odkazovat. I kdyby měl být jen pro mě. A zároveň, aby to bylo na platformě, kde mi nebude nikdo nic tlačit, nutit, vyžadovat subscription, neustále odvádět mou pozornot někam, kam jsem se původně vydat nechtěl.

[Weblog Simona Willisona](https://simonwillison.net/) mě inspiroval začít. Na první pohled trochu "oldschool", ale líbí se mi to. Píše například co se daný den naučil (Today I Learned; TIL) nebo o svých projektech:

> It’s incredibly tempting to skip the step where you write about a project. But any time you do that you’re leaving a huge amount of uncaptured value from that project on the table.
>
> These days I make myself do it: I tell myself that writing about something is the cost I have to pay for building it. And I always end up feeling that the effort was more than worthwhile.

A nově [píše o věcech, co objevil](https://simonwillison.net/2024/Dec/22/link-blog/).

> ... blogging doesn’t have to be about unique insights. The value is in writing frequently and having something to show for it over time—worthwhile even if you don’t attract much of an audience (or any audience at all).

Díky za tipy!

V průběhu let jsem zjistil, že mi psaní pomáhá uvolnit mentální kapacitu, utřídit si myšlenky a vidět nové souvislosti. Někdy je to jako okno do minulosti ve kterém vidím co jsem dělal nebo psal před x lety a kde jsem dneska. Je fajn vidět progres.

Kolikrát už jsem narazil na nějakou zajímavou věc, hudbu, článek nebo knihovnu, které si zasloužily udělat poznámku, odkaz nebo komentář. Které si zasloužily se k nim třeba v budoucnu vrátit. A jen přidat další záložku v prohlížeči se mi neosvědčilo.

Tak uvidíme, jak se blog osvědčí. Jdeme na to.
