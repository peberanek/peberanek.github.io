---
date: 2025-10-04
draft: true
---

# AI Sandbox: zkušenosti z pilotního provozu

_Už dříve jsem psal [o motivaci pro vytvoření open source AI Sandboxu](../posts/open-source-ai-sandbox.md). Cílem tohoto článku je záměr zpřesnit a doplnit o dosavadní zkušenosti z implementace v univerzitním prostředí._

S popularitou aplikace ChatGPT vzrostl zájem členů akademické obce Univerzity Karlovy o využívání generativní umělé inteligence ve výuce a výzkumu, při studiu a v práci. Spolu s tím se však objevily následující problémy:

* Řada uživatelů vyjádřila **oprávněné obavy z úniku citlivých osobních, provozních či výzkumných dat**, zejména v souvislosti s používáním veřejně dostupných verzí populárních chatbotů. Jejich poskytovatelé totiž často využívají vkládaná data k dalšímu tréninku a nepříliš jasnému "zlepšování svých produktů". Nedávno také Národní úřad pro kybernetickou bezpečnost vydal [varování před některými produkty společnosti DeepSeek](https://nukib.gov.cz/cs/infoservis/aktuality/2279-nukib-vydal-varovani-pred-nekterymi-produkty-spolecnosti-deepseek/), jejichž využívání bylo na UK obratem zakázáno.
* V praxi se ukazuje, že **reálné využívání nakoupených předplatných bývá nízké**. Jen část uživatelů je skutečně aktivní, a někteří si svůj účet ani neaktivují. Pokročilí uživatelé pak dříve či později narazí na limity. Navíc v případě, kdy je předplatných pořízen jen omezený počet, lze očekávat vlnu nevole, že někdo přístup dostal a jiný ne.
* **Uzavření akceptovatelných smluv na Enterprise (příp. Edu) verze chatbotů není snadné**. Někteří významní poskytovatelé s českými univerzitami buď nekomunikují, nebo vyžadují vysoké počty nakoupených předplatných za nepříliš lákavou cenu.

Logickým krokem, kterým se řada organizací vydává, je prozkoumat existující open-source řešení hostovaná na vlastním hardware. Navíc, poskytovatelé jako OpenAI, Anthropic nebo Google umožňují volat své služby prostřednictvím API v režimu _pay-as-you-go_. Tím pádem se platí jen za reálnou spotřebu, nikoliv paušálně za jednotlivé uživatele, a otevírá se tak cesta k možnému snížení nákladů.

<!-- more -->

## Inspirace v zahraničí i v tuzemsku

Výše uvedené problémy [řešili také na Harvard University](https://www.youtube.com/watch?v=61zn8Q6lK08). Na základě informací z univerzitních komisí zjistili, že mají velkou poptávku po využívání AI nástrojů při výuce, a proto se rozhodli vytvořit vlastní řešení. Výsledkem je [služba **Harvard AI Sandbox**](https://www.huit.harvard.edu/ai-sandbox):

> The AI Sandbox provides a secure environment in which to explore Generative AI, mitigating many security and privacy risks and ensuring the data entered will not be used to train any vendor large language models (LLMs). It offers a single interface that enables access to the latest LLMs from OpenAI, Anthropic, Google, and Meta.

Z pohledu běžného uživatele se jedná o webové chatovací rozhraní podobné ChatGPT, postavené na open source aplikaci [LibreChat](https://www.librechat.ai/). Pracovat lze s modely od různých poskytovatelů (viz výše), přičemž uživatelé mají povoleno vkládat jen [data do úrovně rizika 3](https://www.huit.harvard.edu/ai/tools) (_"Moderate impact on university operations, research, reputation, or finances"_). Více viz [University Risk Classifications](https://privsec.harvard.edu/classify-risk).

Podobný přístup zaujali i na Stanford University. Pro svou akademickou obec vytvořili platformu [**AI Playground**](https://uit.stanford.edu/service/aiplayground), která vedle [chatovacího rozhraní](https://uit.stanford.edu/aiplayground) (také LibreChat) nabízí i centrálně spravovaný přístup k modelům přes API. Nazvali jej [**AI API Gateway**](https://uit.stanford.edu/service/ai-api-gateway) a stojí na open source aplikaci [LiteLLM](https://www.litellm.ai/). Podporu tak mají nejen běžní uživatelé, ale také výzkumníci a vývojáři, kteří potřebují volat modely programaticky nebo ve vysokých objemech vkládaných a generovaných dat.

Inspirací z tuzemska nám jsou aktivity národní výpočetní infrastruktury [e-INFRA CZ](https://www.e-infra.cz/), konkrétně centra [CERIT SC](https://www.cerit-sc.cz/). Jednou z nich je zpřístupnění [různých AI nástrojů](https://blog.e-infra.cz/blog/chat-ai/), mezi nimi i [chatovacího rozhraní **Chat AI**](https://docs.cerit.io/en/docs/web-apps/chat-ai), postaveného na open source aplikaci [Open WebUI](https://docs.openwebui.com/). Uživatelé mohou chatovat s různými open weights modely běžícími na infrastruktuře e-INFRA CZ, případně i s některými modely placenými. Tato aplikace zároveň umožňuje volat modely i přes API. Pro přístup stačí mít platný účet [v MetaCentru CESNETu](https://metavo.metacentrum.cz/cs/) (více viz [přihláška](https://metavo.metacentrum.cz/cs/application/index.html)).

![Open WebUI](../assets/images/open_webui.png)
/// caption
Chatovací rozhraní aplikace Open WebUI
///

Zde bych rád zmínil, že i chatovací rozhraní AI Sandboxu je hostováno na infrastruktuře e-INFRA CZ, a to jako samostatný klon Open WebUI. Díky tomu můžeme využívat jejich výkonné open weights modely. Zároveň platí, že do naší instance mají přístup jen uživatelé Univerzity Karlovy, a to prostřednictvím Centrální autentizační služby UK (CAS). Za nasazení a pomoc se správou kolegům z e-INFRA CZ, resp. CERIT SC, velmi děkujeme. Pro zájemce o bližší informace o tom, co obnáší hostování velkých jazykových modelů na vlastní infrastruktuře vřele doporučuji jejich článek [Silicon Vampires: How Do We Run LLMs](https://blog.e-infra.cz/blog/run-llm/).

## Očekávání a skutečnost

Samozřejmě platí, že open source neznamená dokonalé řešení. Některé projekty jsou vysloveně špatné, řada zůstává nedotažena, a jen některé jsou skutečně kvalitní a s dobrou - zejména dlouhodobou - podporou. Proto jsme zhruba před rokem po delším výběru a zkoušení nasadili malou testovací instanci s Open WebUI + [Ollama](https://ollama.com/). Výhodou je, že se obojí dá relativně jednoduše nainstalovat na osobním počítači, vyzkoušet a až poté nasadit jako webovou aplikaci na serveru. (LibreChat jsem na počátku také zkoušel, ale vzhledem k tomu, že v něm tehdy byla správa uživatelů dosti složitá, zvítězilo populárnější Open WebUI.)


Výběr projektů - proč Open WebUI, LiteLLM, Ollama, vLLM

Překvapilo mě

* malá podpora vedení - slovní ano, ale personální a finanční jen minimální, snad pomůže tým RSE
* malá snaha se aktivně zapojit - všichni čekají, až to někdo jiný zařídí

Propast mezi pilotem a ostrým provozem je velká.

## TODO

Díky překvapivým obtížím s pořízením Edu verze ChatGPT (a dalších pokročilých chatbotů) jsme se před rokem a půl rozhodli prozkoumat open source řešení. Na základě podobných projektů zahraničních univerzit jsme nasadili chatovací platformu nazvanou AI Sandbox. Jaká byla naše očekávání a jaká je realita? V čem se platforma osvědčila a co nás brzdí? Jak složité (nebo jednoduché) by bylo nasadit ji i u vás? Přijďte se dozvědět víc a sdílet zkušenosti.

Kategorizace dat: https://openscience.cuni.cz/OSCI-95.html

* Design - tech popis
* Zkušenosti a zůžení scope
* Co nás brzdí, road map
