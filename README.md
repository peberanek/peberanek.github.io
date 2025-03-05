[Blog](/README.md) ⋅ [Curriculum Vitae](/cv.md) ⋅ [Email](mailto:beranek@duck.com) ⋅ [GitHub](https://github.com/peberanek) ⋅ [X (Twitter)](https://x.com/peberanek)

# Blog

## 2025-03-05

### llm

Dneska jsem vyzkoušel nástroj do příkazové řádky, nazvaný jednoduše [llm](https://llm.datasette.io/en/stable/) (jeho autorem je Simon Willison, který, mimo jiné, píše [zajímavý blog](https://simonwillison.net/)). `llm` dokáže volat i modely běžící přes [Ollamu](https://ollama.com/).

> A CLI utility and Python library for interacting with Large Language Models, both via remote APIs and models that can be installed and run on your own machine.
  
```bash
llm "Tell me a joke about LLMs."
```

Nainstaloval jsem přes [uv](https://docs.astral.sh/uv/) (samozřejmě je [možné použít i pip](https://llm.datasette.io/en/stable/setup.html#installation)):
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

### Soubor je důležitější než aplikace

Před nějakou dobou jsem zkoušel [Obsidian](https://obsidian.md/). I když jsem u něj nakonec nezůstal (kvůli nedostatečné emulaci editoru Vim), tak musím ocenit, že moje poznámky ukládá jako obyčejné textové soubory. Můžu je tak editovat třeba ve VSCode:

> File over app is a philosophy: if you want to create digital artifacts that last, they must be files you can control, in formats that are easy to retrieve and read. Use tools that give you this freedom.
>
>File over app is an appeal to tool makers: accept that all software is ephemeral, and give people ownership over their data.  
>-- [Steph Ango](https://stephango.com/file-over-app) (Obsidian CEO)

Nebo slovy [Andreje Karpathyho](https://x.com/karpathy/status/1761467904737067456):

> \- Your notes are simple plain-text markdown files stored locally on your computer. Obsidian is just UI/UX sugar of pretty rendering and editing files.  
> \- Extensive plugins ecosystem and very high composability with any other tools you wish to use because again it's all just plain-text files on your disk. [...]  
> \- There are no attempts to "lock you in", actually as far as I can tell Obsidian is completely free of any user-hostile dark patterns.  

Obdobnou filozofii razí i [Plain Text Accounting (PTA)](https://plaintextaccounting.org/). Konkrétně už řadu let využívám [Beancount](https://plaintextaccounting.org/):

```
2024-11-12 * "Vstupenka na vyhlidkovou vez"
  Majetek:Banky:CSOB:Bezny-ucet  -140 CZK
  Vydaje:Ostatni
```

Díky tomu, že jsou to obyčejné textové soubory, mohou nad nimi snadno pracovat nástroje jako `git`, `grep`, `sed` a další.

Navíc, Beancount je psaný v Pythonu a dá se s ním řada věcí automatizovat, třeba [import transakcí](https://github.com/beancount/beangulp). Vedle manuálního stažení textových souborů nabízí některé instituce i API. Dřív jsem si s tím trochu hrál a napsal vlastní nástroj [Beanclerk](https://github.com/peberanek/beanclerk) (zveřejnil jsem k tomu i klienty pro [Fio banku](https://github.com/peberanek/fio-banka) a [Banku Creditas](https://github.com/peberanek/creditas)). Dneska bych to nejspíš udělal o dost jinak, ale nástroje vesele slouží dodnes.

Řadu těch nástrojů třeba jednoho dne nahradí nějaký velký jazykový model, protože jsou to všechno jen obyčejné textové soubory. Uvidíme.

## 2025-02-26

### Začínám psát blog

> You should start a blog. Having your own little corner of the internet is good for the soul!  
-- [Simon Willison](https://simonwillison.net/2022/Nov/6/what-to-blog-about/)

Už nějakou dobu si říkám, že by bylo fajn mít místo pro sdílení myšlenek a věcí, co mě něčím zaujaly. Mít nějaký online deník, ke kterému se můžu snadno vracet. I kdyby měl být jen pro mě. A zároveň, aby to bylo na platformě, kde mi nebude nikdo nic tlačit, nutit, vyžadovat subscription, neustále odvádět mou pozornot někam, kam jsem vůbec jít nechtěl.

Simon Willison mě svým Weblogem inspiroval začít. Na první pohled trochu "oldschool", ale mě se to líbí. Píše například co se daný den naučil (Today I Learned; TIL) nebo o svých projektech:

> It’s incredibly tempting to skip the step where you write about a project. But any time you do that you’re leaving a huge amount of uncaptured value from that project on the table.
>
> These days I make myself do it: I tell myself that writing about something is the cost I have to pay for building it. And I always end up feeling that the effort was more than worthwhile.

A nově píše o [věcech, co objevil](https://simonwillison.net/2024/Dec/22/link-blog/).

> ... blogging doesn’t have to be about unique insights. The value is in writing frequently and having something to show for it over time—worthwhile even if you don’t attract much of an audience (or any audience at all).

Díky za tipy!

V průběhu let jsem zjistil, že mi psaní pomáhá uvolnit mentální kapacitu, utřídit si myšlenky a třeba i vidět nové souvislosti. Někdy je to takové okno do minulosti ve kterém vidím co jsem dělal nebo psal před x lety a kde jsem dneska. Je fajn vidět progres.

Kolikrát jsem narazil na nějakou zajímavou věc, hudbu, knihovnu, které si zasloužily udělat poznámku, odkaz nebo komentář. Které si zasloužily se k nim třeba v budoucnu vrátit. A jen hromadit záložky v prohlížeči se mi moc neosvědčilo.

Tak uvidíme, jak se osvědčí blog. Jdeme na to.
