---
date: 2025-03-03
tags:
  - beancount
  - open-source
  - andrej-karpathy
  - software-development
---

# Soubor je víc než aplikace

Před nějakou dobou jsem zkoušel [Obsidian](https://obsidian.md/). I když jsem u něj nakonec nezůstal (kvůli nedostatečné emulaci editoru Vim), tak musím ocenit, že moje poznámky ukládal jako obyčejné textové soubory. Můžu je tak editovat třeba ve VSCode:

> File over app is a philosophy: if you want to create digital artifacts that last, they must be files you can control, in formats that are easy to retrieve and read. Use tools that give you this freedom.
>
>File over app is an appeal to tool makers: accept that all software is ephemeral, and give people ownership over their data.  
>-- [Steph Ango: File over app](https://stephango.com/file-over-app)

<!-- more -->

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
