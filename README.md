[Blog](/README.md) ⋅ [Curriculum Vitae](/cv.md) ⋅ [Email](mailto:beranek@duck.com) ⋅ [GitHub](https://github.com/peberanek) ⋅ [X (Twitter)](https://x.com/peberanek)

# Blog

## 2025-05-02

### Mark Zuckerberg (nejen) o Chatbot Aréně

> You also mentioned the whole Chatbot Arena thing, which I think is interesting and points to the challenge around how you do benchmarking. How do you know what models are good for which things?
>
> One of the things we've generally tried to do over the last year is anchor more of our models in our Meta AI product north star use cases. The issue with open source benchmarks, and any given thing like the LM Arena stuff, is that they’re often skewed toward a very specific set of uses cases, which are often not actually  what any normal person does in your product. [...]
>
> So we're trying to anchor our north star on the product value that people report to us, what they say that they want, and what their revealed preferences are, and using the experiences that we have. Sometimes these benchmarks just don't quite line up. I think a lot of them are quite easily gameable.
>
> On the Arena you'll see stuff like Sonnet 3.7, which is a great model, and it's not near the top. It was relatively easy for our team to tune a version of Llama 4 Maverick that could be way at the top. But the version we released, the pure model, actually has no tuning for that at all, so it's further down. So you just need to be careful with some of these benchmarks. We're going to index primarily on the products.  
-- [Mark Zuckerberg: Meta's AGI Plan](https://www.dwarkesh.com/p/mark-zuckerberg-2) ([via](https://simonwillison.net/2025/May/1/mark-zuckerberg/))

## 2025-04-20

### Open WebUI jako rozšíření pro Rancher Desktop

V článku o [AI Sandboxu](https://peberanek.github.io/#open-source-ai-sandbox) jsem zmínil Open WebUI jakožto flexibilní rozhraní (chatbota) pro komunikaci s různými modely generativní AI. Nyní jsem zjistil, že je k dispozici i formou [rozšírení pro Rancher Desktop](https://www.suse.com/c/rancher_blog/rancher-desktop-1-17-with-open-webui-extension-and-more/) (a dokonce je součástí platformy [SUSE AI](https://documentation.suse.com/suse-ai/1.0/html/AI-deployment-intro/index.html)).

Musím říct, že instalace rozšíření nebyla úplně přímočará. Nainstaloval jsem Rancher Desktop a kliknul na instalaci rozšíření. Ta ale nedoběhla a zůstala tzv. viset, což je trochu nešťastná první zkušenost. Po restartu celé aplikace už ale instalace doběhla v pořádku. Líbí se mi, že Open WebUI běží přímo v okně Rancher Desktopu, takže se není potřeba nikam přepínat. Není ani potřeba vytvářet nového uživatele, vytvoří se defaultní uživatel `User`. Propojení s existující instancí Ollama proběhlo automaticky, což je taky fajn. Nevýhodou může být starší verze Open WebUI (0.5.20) oproti upstreamu (0.6.5).

## 2025-04-15

### OpenAI GPT-4.1

[OpenAI vydala novou sérii modelů GPT-4.1](https://openai.com/index/gpt-4-1/) ([via](https://buttondown.com/ainews/archive/ainews-gpt-41-the-new-openai-workhorse/)) (číslování je trochu matoucí vzhledem k nedávno vydanému GPT-4.5 research preview). Z příspěvku je zřejmé, že modely jsou cílené primárně na oblast programování a programovacích asistentů/agentů, kde dlouho vládl Claude 3.5 (resp. 3.7) Sonnet, a nově vstoupila Gemini 2.5 Pro. OpenAI inzeruje také zlepšené výsledky v následování instrukcí (oproti GPT-4o), a výrazně větší kontext - až 1 milion tokenů (což by mělo např. pojmout - 8x - celý zdrojový kód Reactu).

Zároveň není v plánu zpřístupnit nové modely v ChatGPT:

> Note that GPT-4.1 will only be available via the API. In ChatGPT, many of the improvements in instruction following, coding, and intelligence have been gradually incorporated into the latest version of GPT-4o, and we will continue to incorporate more with future releases.

Zajímavá je i cena generovaných (output) tokenů: GPT-4.1 je oproti Claude 3.7 Sonnet a Gemini 2.5 Pro zhruba o polovinu levnější ($8 oproti $15 za 1 milion tokenů). Výrazně lépe vychází oproti o1 ($60), nemluvě o o1-pro ($600). Poměr vůči o3 ($4.40) nedokážu odhadnout vzhledem k nutnosti generovat reasoning tokeny.

Dlouhý kontext:

> Thomson Reuters tested GPT‑4.1 with CoCounsel, their professional grade AI assistant for legal work. Compared to GPT‑4o, they were able to improve multi-document review accuracy by 17% when using GPT‑4.1 across internal long-context benchmarks—an essential measure of CoCounsel’s ability to handle complex legal workflows involving multiple, lengthy documents. In particular, they found the model to be highly reliable at maintaining context across sources and accurately identifying nuanced relationships between documents, such as conflicting clauses or additional supplementary context—tasks critical to legal analysis and decision-making.

> In our initial testing, latency to first token for GPT‑4.1 was approximately fifteen seconds with 128,000 tokens of context, and a minute for a million tokens of context. GPT‑4.1 mini and nano are faster, e.g., GPT‑4.1 nano most often returns the first token in less than five seconds for queries with 128,000 input tokens.

Další poznámky:
* Ve zpracování obrazu vychází GPT-4.1 a GPT-4.1-mini téměř stejně (viz článek), přičemž mini stojí pouze 1/5 ceny.
* V oblasti 'Academic knowledge' vychází GPT-4.1 (i GPT-4.1-mini!) stejně nebo dokonce lépe než stávající ChatGPT-4o.

## 2025-04-14

### AI jako spolupracovník

> Can AI take over some of [my] tasks? The answer is yes, and frankly, there are tasks that I wouldn't mind offloading to AI, like administrative paperwork. But does that mean my job will vanish? Not really. Getting rid of some tasks doesn't mean the job disappears. In the same way, power tools didn't eliminate carpenters but made them more efficient, and spreadsheets let accountants work faster but did not eliminate accountants. AI has the potential to automate mundane tasks, freeing us for work that requires uniquely human traits such as creativity and critical thinking–or, possibly, managing and curating the AI's creative output[.]
> 
> However, this isn't the end of the story. The systems within which we operate play a crucial role in shaping our jobs as well. [...] Let's say an AI can deliver a lecture better than I can. Would students be willing to outsource their learning to AI? [...] Would the deans of the university feel comfortable using AI in this way? Would the magazines and sites that rank schools punish us for doing so? My job is connected to many other jobs, customers and stakeholders. Even if AI automates my job, the systems in which it works are less obvious.  
-- [Ethan Mollick: "Co-Intelligence: Living and Working with AI", p. 125-126](https://www.moreusefulthings.com/book)

## 2025-04-09

### Na něco se těšit

Známý chirung [profesor Pavel Pafko říká, že je důležité se pořád na něco těšit](https://strednicechy.rozhlas.cz/jsme-zhyckani-ano-prospelo-nam-slapat-do-kopce-odpovida-profesor-pavel-pafko-9448286):

> "Lidem říkám, že člověk, kterej se ráno vzbudí musí mít nějaký plán na ten den, který bude následovat. Často ten plán nesplníme, protože nám do toho přijdou situace neplánované, které nám ten plán rozbourají. Ale těšit se ráno jenom na to, že ten den vydržím, pak se navečeřím a pak půjdu spát, tak ten den neměl být takový."

Otázka "Na co se dneska můžu těšit?" může být někdy dost těžká. A přesto, dá se jí upravit třeba na "Jak to zařídit, abych se dneska vůbec mohl na něco těšit?", nebo "Jakou malou radost si dneska můžu dopřát?".

## 2025-04-08

### Ohýbání LM Arena Leaderboardu

Andrej Karpathy [vyjádřil jistou nedůvěru](https://youtu.be/7xTGNNLPyMI?t=11815) k výsledkům na [LM Arena Leaderboard](https://lmarena.ai/?leaderboard) v posledních měsících. Příkladem je třeba oblíbený Claude 3.7 Sonnet, v žebříčku až okolo 15. místa. A hle, Meta nám tak trochu podvádí, resp. jejich model (na 2. místě) je jiný než modely, které reálně vydali:

> Meta’s interpretation of our policy did not match what we expect from model providers. Meta should have made it clearer that “Llama-4-Maverick-03-26-Experimental” was a customized model to optimize for human preference. As a result of that we are updating our leaderboard policies to reinforce our commitment to fair, reproducible evaluations so this confusion doesn’t occur in the future.  
-- [lmarena.ai](https://x.com/lmarena_ai/status/1909397817434816562) ([via](https://buttondown.com/ainews/archive/ainews-llama-4s-controversial-weekend-release/))

Pokud se jedná o upravený model, který není normálně k dispozici, říkám si proč nebyl z žebříčku odebrán.

_Update(2025-04-12)_: Zdá se, že Llama-4-Maverick-03-26-Experimental už byla z žebříčku odebrána, a [Llama-4-Maverick-17B-128E-Instruct](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) si nevede nijak oslnivě. Dnes okolo 32. místa.

## 2025-04-05

### Nové jazykové modely a panika (nejen) na trzích

#### 25.3.2025

Google vydal [Gemini 2.5 Pro Experimental](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/). Nyní #1 na [LM Arena Leaderboard](https://lmarena.ai/?leaderboard).

#### 31.3.2025

> TL;DR: we are excited to release a powerful new open-weight language model with reasoning in the coming months, and we want to talk to devs about how to make it maximally useful: https://openai.com/open-model-feedback/
>
> we are excited to make this a very, very good model!  
-- [Sam Altman](https://x.com/sama/status/1906793591944646898) ([via](https://simonwillison.net/2025/Apr/1/brad-lightcap/))

#### 4.4.2025

<img src="/media/spx_20250405.png" alt="TradingView screenshot (SPX 500)" style="max-width: 100%;">

_Screenshot z aplikace TradingView zachycují propad indexu S&P 500 (denní graf za poslední rok; propad za poslední 2 dny o -10,5%)._

#### 5.4.2025

Dnes (v sobotu!) vydala Meta dvojici open-weight modelů [Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/). Nyní #2 na LM Arena Leaderboard.

OpenAI:

> change of plans: we are going to release o3 and o4-mini after all, probably in a couple of weeks, and then do GPT-5 in a few months.  
-- [Sam Altman](https://x.com/sama/status/1908167621624856998) ([via](https://simonwillison.net/2025/Apr/4/sam-altman/))

### O smyslu psaní blogů

> Blogging is small-p political again, today. It’s come back round. It’s a statement to put your words in a place where they are not subject to someone else’s algorithm telling you what success looks like; when you blog, your words are not a vote for the values of someone else’s platform.
>
> [...]
>
> I don’t make any money out of [my blog], not directly. But it’s so, so worth it. I don’t how how to put a figure on the value of friends, work, ideas, opportunities and enjoyment I’ve got out of simply “thinking out loud” over the years.  
-- [Matt Webb: People and Blogs](https://manuelmoreale.com/pb-matt-webb) ([via](https://simonwillison.net/2025/Apr/5/matt-webb/))

### Různí chatboti v jedné aplikaci

Už pár let používám open-source aplikaci [Ferdium](https://ferdium.org/). Díky ní můžu mít různé služby, např. Gmail, Google Kalendář nebo Discord v jednom rozhraní bez nutnosti používat běžný prohlížeč. Zároveň můžu být přihlášený k pracovnímu i soukromému účtu zároveň aniž bych se musel odhlašovat a přepínat. Jednu službu lze přidat vícekrát, pokaždé s jiným účtem, protože každá běží izolovaně. Díky Ferdiu se mi tak nemýchají dohromady věci jako čtení emailů, chatování a prohlížení internetu. Mohu se i lépe soustředit - notifikace zůstávají ve Ferdiu a dají se případně vypnout.

Stejný princip jde uplatnit i pro různé chatboty a další AI nástroje. Namísto lovení záložek v prohlížeči mohou být přehledně ve Ferdiu, viz níže. (Ferdium je postavené na technologii [Electron](https://www.electronjs.org/) - jedná se tedy v principu o webové stránky běžící v Chromiu. Služby tudíž nejsou plnohodnotné desktopové aplikace.)

<img src="/media/ferdium.png" alt="Ferdium screenshot" style="max-width: 100%;">

_Screenshot aplikace Ferdium. Vytvořeno s pomocí [Screely](https://screely.com/) a [GIMP](https://www.gimp.org/)._

Jak je vidět v levém panelu, ikona Anthropic (Claude) je tam 2x - jednou jako soukromý a jednou jako pracovní účet.

Zhruba před rokem jsem zkoušel přidat službu ChatGPT, ale nešlo se mi přihlásit. Nyní to vypadá, že problém byl odstraněn. Některé služby (ChatGPT, Claude, Perplexity) jsou dostupné v katalogu služeb, jiné (Google AI Studio, NotebookLM, Open WebUI) je potřeba přidat manuálně, resp. doplnit URL. Co se týče Open WebUI, měl jsem trochu obavu, jestli se Ferdium dokáže připojit i na lokálně běžící server, konkrétně `http://0.0.0.0:8080/`, a ano, zvládne to.

Užitečnou funkcionalitou jsou 'workspaces', díky které mám AI nástroje v samostatném pracovním prostoru (viz obrázek výše), ve kterém mě nerozptylují ikony Gmalu nebo Discordu.

## 2025-04-04

### AI jako nástroj (ne)komunikace

[Po odstávce elektřiny mají lidé na Trutnovsku zničené spotřebiče](https://ct24.ceskatelevize.cz/clanek/regiony/po-odstavce-elektriny-maji-lide-na-trutnovsku-znicene-spotrebice-359706):

> Například v domě obyvatelky Stanovic Jany Hadincové ani ve čtvrtek nevařili kávu. Nechladila lednička, neohřívali vodu, nefungoval sporák a vypadla síť wi-fi. Přístroje jsou zničené. Odhad škody je sto padesát tisíc korun. „Nejhorší je ta bezmoc, když někam voláte, všude umělá inteligence, nikdo s vámi nechce mluvit,“ popsala.

Párkrát už jsem zažil situaci, kdy jsem potřeboval něco řešit a jeden z mála komunikačních nástrojů byl poněkud nespolupracující chatbot. Velmi frustrující. Nasadit AI operátora tam kde levně nahradí několik lidí bude jistě pro řadu firem velmi lákavé. Na druhou stranu výsledkem může být také čím dál více odlidštěná (ne)komunikace.

## 2025-04-02

### Model Context Protocol (MCP)

> The Model Context Protocol aims to provide a standard interface for LLMs to interact with other applications, allowing applications to expose tools, resources (contant that you might want to dump into your context) and parameterized prompts that can be used by the models.  
-- [Simon Willison](https://simonwillison.net/2024/Nov/25/model-context-protocol/)

> MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools.  
-- [modelcontextprotocol.io](https://modelcontextprotocol.io/introduction)

Poslední dobou narážím na čím dál víc zmínek o MCP (např. na [AI News](https://buttondown.com/ainews/archive/ainews-ghibli-memes/), nově v [Open WebUI v0.6.0](https://github.com/open-webui/open-webui/releases/tag/v0.6.0) (resp. [mcpo](https://github.com/open-webui/mcpo)), a dokonce už i v [Beancount Google Group](https://groups.google.com/g/beancount/c/VC91-6yLBE4/m/ihCVGU6BBwAJ)). Úvodní kapitoly videa [Building Agents with Model Context Protocol - Full Workshop with Mahesh Murag of Anthropic](https://www.youtube.com/watch?v=kQmXtrmQ5Zg) nabízí pěkný srozumitelný přehled.

## 2025-03-30

### AI jako nástroj hledání nových řešení

Andrej Karpathy ve svém videu [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) (konkrétně v části o Reinforcement Learning) zmiňuje film [Alphago (2017)](https://www.youtube.com/watch?v=WXuK6gekU1Y). Vřele doporučuji. Film pojednává o stejnojmenném programu, který jako první dokázal porazit Lee Sedola - jednoho z nejlepších hráčů hry Go, považované za výrazně komplexnější než třeba šachy. Ve filmu mě zaujala mimo jiné úvodní scéna zmiňující jinou hru - Breakout:

> Virtual environments and games, we think they're the perfect platform for developing and testing AI algorithms. Games are very convenient, in that a lot of them have scores, so it's very easy to measure incremental progress. [...]
>
> So let's start off with Breakout. So here you control the bat and ball, and you're trying to break through this rainbow-colored wall. The agent system has to learn everything for itself,
just from the raw pixels. It doesn't know what it's controlling. It doesn't even know what the object of the game is. Now, at the beginning, after 100 games, you can see the agent is not very good. It's missing the ball most of the time. But it's starting to get the hang of the idea that the bat should go towards the ball.

<img src="/media/breakout_1.png" alt="Breakout game screenshot" width="650" style="max-width: 100%;">

> Now, after 300 games, it's about as good as any human can play this, and pretty much gets the ball back every time. We thought, "Well, that's pretty cool." But we left the system playing for another 200 games, and it did this amazing thing. It found the optimal strategy was to dig a tunnel around the side, and put the ball round the back of the wall.

<img src="/media/breakout_2.png" alt="Breakout game screenshot" width="650" style="max-width: 100%;">

> **The researchers** working on this, the amazing AI developers, well, they're not so good at Breakout, and they **didn't know about that strategy. So, they learned something from their own system, which is, uh, you know, pretty funny and quite instructive**, I think, about the potential for general AI.

## 2025-03-20

### `sudo` bez hesla

Požádal jsem Clauda 3.7 Sonnet aby mi poradil s následující situací: mám shellový skript a některé příkazy vyžadují `sudo`, resp. spouštět příkaz s právy roota. Skript se spouští docela často a začíná být nepraktické pokaždé zadávat heslo. Claude přišel s návrhem povolit dané příkazy pomocí pluginu sudoers ("default sudo security policy plugin"; více viz `man sudoers`), který jsem do té doby neznal. Rovnou mi vypsal, co a jak mám nastavit:

```bash
sudo visudo -f /etc/sudoers.d/update
```

A do souboru přidat např. následující:
```
# Allow running commands without password
myuser ALL=(root) NOPASSWD: /usr/bin/apt update, /usr/bin/apt upgrade -y, /usr/bin/snap refresh
```

Uživatel `myuser` může spouštět `/usr/bin/apt update`, `/usr/bin/apt upgrade -y`, a `/usr/bin/snap refresh` jako `root` bez nutnosti se autentizovat. Příkazy musí být zadány i včetně všech uvedených parametrů (tj. `apt upgrade -y`, cestu není třeba zadávat), jinak je heslo vyžadováno.

Vzhledem k rostoucím schopnostem a znalostem současných modelů začíná být pocitově jednodužší (i zábavnější) jako první konzultovat problém s chatbotem, než "jít hledat na internetu". A to nejen v situacích, kdy jsou související informace s velkou pravděpodobností hojně zastoupené v trénikových datasetech. Ono totiž, jak říká jeden můj bohatý příbuzný, "I blbej nápad je dobrej nápad. Ne sám o sobě, ale tím, že nás může mentálně odblokovat a nasměrovat k použitelnému řešení."

## 2025-03-19

### Ventolin

<img src="https://www.fleda.cz//data/files/Ventolin-Krezek1654.jpg" alt="Ventolin na pódiu v klubu Fléda" style="max-width: 100%;">

_Foto výše: Ventolin na pódiu [v brněnském klubu Fléda](https://www.fleda.cz/photo/default/291/)_

Český hudebník David Doubek alias [Ventolin](https://www.ventolin.cz/). Hudební texty na rozhraní experimentu, absurdity, ale taky skrytého významu a vtipu. To vše ruku v ruce s kvalitní elektronickou hudbou. Nejvíc mě zaujaly skladby:

* [Sovy](https://www.youtube.com/watch?v=Rz-GbKTt81c)
* [Disco Science](https://www.youtube.com/watch?v=jjTOYerHRVo)
* [Totem](https://www.youtube.com/watch?v=ZdZZ0cgawJg)
* [Supersonik](https://www.youtube.com/watch?v=nFl24aJnLZ4)
* [Vyšší inteligence](https://www.youtube.com/watch?v=DxuyO0_RopY)
* [Když jedu z hub](https://www.youtube.com/watch?v=jGiAXU-8Vn8)

Dnes jsem náhodou zjistil, že o něm dokonce vznikl [krátký dokument](https://www.youtube.com/watch?v=E6h6ZFLB1dE).

## 2025-03-09

### Amarův zákon

> We tend to overestimate the effect of a technology in the short run and underestimate the effect in the long run.  
-- [Roy Amara](https://en.wikipedia.org/wiki/Roy_Amara)

Tímto díky [Martinu Richterovi](https://cz.linkedin.com/in/mr-martin-richter) za zmínku.

## 2025-03-08

### AI jako akcelerátor toxické kultury

[AI Is About to Make Social Media (Much) More Toxic](https://www.theatlantic.com/technology/archive/2023/05/generative-ai-social-media-integration-dangers-disinformation-addiction/673940/) ([via](https://www.youtube.com/watch?v=tLxfLjebJV8)):
> ... whatever actions AIs may _one day_ take if they develop their own desires, they are already being
used instrumentally by social-media companies, advertisers, foreign agents, and
regular people—and in ways that will deepen many of the pathologies already
inherent in internet culture. On Sydney’s list of things it might try, stealing launch
codes and creating novel viruses are the most terrifying, but making people argue
until they kill one another is something social media is already doing.  

## 2025-03-07

### Open-source AI Sandbox

<img src="/media/open_webui.png" alt="Open WebUI screenshot" style="max-width: 100%;">

_Screenshot aplikace Open WebUI. Vytvořeno s pomocí [Screely](https://screely.com/) a [GIMP](https://www.gimp.org/)._

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

* Open WebUI [lze nainstalovat na vlastním počítači různými způsoby](https://docs.openwebui.com/getting-started/quick-start/). Za mě nejjednodužší je použít [uv](https://docs.astral.sh/uv/):
  ```
  uvx --python 3.11 open-webui@latest serve
  ```
* Projekt [E-infra](https://www.e-infra.cz/) hostuje [testovací instanci Open WebUI](https://docs.cerit.io/en/docs/web-apps/chat-ai) s několika open-source modely.
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
