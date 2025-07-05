---
date: 2025-07-05
draft: true
---

TODO: 'Čisté-jmění' místo 'Kapital'

# Osobní účetnictví: Má to smysl?

Následující text je zamyšlením nad posledními 10 lety, kdy jsem si začal vést osobní účetnictví, tj. kompletní přehled majetku a závazků, příjmů a výdajů. Od úplných začátků s tužkou a papírem až po automatizované zpracování pomocí open-source aplikací. V článku popisuji důvody, které mě k tomu vedly a sdílím své zkušenosti.

## Proč jsem s osobním účetnictvím začal

V roce 2015 jsem padnul na finanční dno a k tomu skončil na dva měsíce v nemocnici. Celkem drsná životní lekce. Na druhou stranu, na chvíli jsem nemusel řešit účtenky, penále, a především nesplnitelné požadavky lidí v mém okolí, a to mi dalo příležitost se vzpamatovat a zvednout. Shodou okolností se mi v té době dostala do ruky kniha _Bohatý táta, chudý táta_ od Roberta Kiyosakiho a Sharon Lechter. Třebaže se jedná o poněkud kontroverzního autora (Kiyosaki), jeho historka o bohatém tátovi mě motivovala si udělat v penězích pořádek.

<!-- more -->

Jednou z oblastí, kterou Kiyosaki uvádí jako klíčovou pro budování bohatství, je znalost účetnictví. Nemá tím na mysli stát se expertem (ty je lepší si najmout), ale porozumět principům a umět je využít ve svůj prospěch. Základy účetnictví jsem měl na střední škole (jeden z těch předmětů, co si říkáte, že nikdy nevyužijete), a tak mě napadlo zkusit si vytvořit funkční model rozvahy, výsledovky a jednotlivých účtů, vše zjednodušené pro osobní potřebu.

Kdo někdy finančně zápasil, asi mi dá za pravdu, že přemýšlet a mluvit v tom stavu o penězích je bolest. Velká bolest. A taky strach, možná i pocit selhání. Člověk by nejraději dělal, že jeho finanční problémy neexistují, vytěsnil je, zapomněl. A tím se vše ještě zhorší. Ono to na první pohled vypadá logicky: protože máme finanční problémy, nechceme o nich mluvit. Já si ale dovolím tvrdit, že je tomu naopak: _protože jsme naučení o naší finanční realitě nemluvit, tabuizovat ji, nepřemýšlet nad ní, tak právě proto máme menší či větší finanční problémy_. A osobní účetnictví se mi osvědčilo jako nástroj, jak si toto přemýšlení ulehčit a dát mu systém.

Zajímavé je, že jakmile jsem začal sepisovat svůj majetek, začaly se objevovat další a další zapomenuté peníze. A dluhy, poctivě vyčíslené, přestaly vypadat tak strašidelně. Dodnes vnímám jako velkou výhodu to, že už nemusím vše držet v hlavě. Možnost mít čísla a data vizualizovaná před sebou mi dává větší klid a mentální kapacitu pro hledání nových řešení. Ať už se jednalo o strategii placení dluhů, osekávání zbytečných výdajů nebo dnes třeba o investice.

## Od tužky a papíru k automatizaci

### Excel/Calc

Na střední jsme účtovali ručně, takže jsem přirozeně začal s tužkou, papírem a opakováním _Učebnice účetnictví_ z roku 2006. Počítat vše manuálně nebo s kalkulačkou se však omrzí dost rychle, takže dalším logickým krokem byl Excel, resp. LibreOffice Calc (v principu je to totéž). Calc je fajn v tom, že dává značnou flexibilitu ve výpočtech a vizualizacích, aniž by musel člověk programovat. Dodnes ho využívám na některé přehledy. S množstvím dat ale začala narůstat i komplexita a s ní i nároky na údržbu a detekci chyb, takže jsem se zhruba po roce vydal hledat robustnější řešení.

### Pokus o vlastní databázi

S úsměvem nyní vzpomínám na epizodku, kdy jsem v rámci kurzu Úvodu do databází dostal nápad, že bych přece mohl udělat PostgreSQL databázi s nějakým jednoduchým front-endem. Jako studijní projekt to bylo fajn, ale člověk nakonec zjistí, že jednodužší je použít něco už hotového.

### Komerční aplikace

Jednou z možností bylo jít cestou aplikací jako [YNAB (You Need a Budget)](https://www.ynab.com/) nebo [Mint](https://mint.intuit.com/). Nicméně kombinace předplatného a nutnosti svěřovat své kompletní finanční informace nějaké společnosti mě nelákala. Zároveň může být později složité svá data získat zpět nebo převést jinam. Např. výše zmíněný Mint byl v roce 2023 ukončen, resp. začleněn pod [Credit Karma](https://en.wikipedia.org/wiki/Credit_Karma). Mimochodem, věděli jste, že existovala aplikace [Microsoft Money](https://en.wikipedia.org/wiki/Microsoft_Money)? Její podpora byla ukončena v roce 2011, prý pro nedostatečnou poptávku.

### Open-source a GnuCash

Ve vodách open-source jsem narazil na [HomeBank](https://www.gethomebank.org/), [ledger](https://ledger-cli.org/) a [GnuCash](https://gnucash.org/), přičemž nejvíc mě tehdy oslovila poslední z nich, a to kombinací podvojného účetnictví a GUI (které ledger, tuším, tehdy neměl). Na specifika grafického rozhraní jsem si zvyknul, a na nějakou dobu mi nevadilo ani manuální zadávání. GnuCash sice umí importovat data ze souboru, ale z důvodu osobní pohodlnosti jsem tuto funkci zatvrzele ignoroval. Například kvůli chybějícím ID transakcí, což by v praxi znamenalo vždy vše překontrolovat a opravovat případné duplicity.

Postupem času i GnuCash začalo ukazovat své limity. Základní automatizace pomocí Pythonu se nakonec dala zvládnout (motivovalo mě zjištění, že [Fio banka API](https://www.fio.cz/bankovni-sluzby/api-bankovnictvi) vrací ID transakcí i aktuální zůstatek). Vedle oficiálních [Python bindings](https://wiki.gnucash.org/wiki/Python_Bindings) existuje i slušně zdokumentovaný balíček [piecash](https://github.com/sdementen/piecash) (kredit autorovi), se kterým šla řada věcí udělat. Při hrátkách s kryptoměnami jsem ale narazil. GnuCash podporuje maximálně 6 desetinných míst a např. Bitcoin potřebuje 8 (jiné kryptoměny i více). Hackování tedy bylo dost a nastal čas hledat něco flexibilnějšího.

!!! Poznámka

    Pro detailně rozepsané výhody a nevýhody některých aplikací doporučuji [tento přehled](https://beancount.github.io/docs/command_line_accounting_in_context.html#why-not-just-use-a-spreadsheet).

## Beancount aneb Plain Text Accounting v praxi

> I believe that the method of double-entry counting should be taught to everyone at the high school level everywhere as it is a tremendously useful organizational skill, and I hope that this text can help spread its knowledge beyond professional circles.  
-- [Martin Blais (z dokumentace k aplikaci Beancount)](https://beancount.github.io/docs/the_double_entry_counting_method.html#introduction)

V rámci průzkumu jsem objevil [Plain Text Accounting (PTA)](https://plaintextaccounting.org/), což znamená vedení účetních záznamů v textových souborech. Vedle již zmíněné aplikace _ledger_ (nebo [hledger](https://hledger.org/)) tento přístup implementuje i [Beancount](https://github.com/beancount/beancount/), který je napsaný primárně v Pythonu (a částečně v C). Holt k některým věcem jsem potřeboval dospět, resp. být komfortní s prací v textovém editoru a v příkazové řádce.

Není mojí ambicí v tomto článku poskytnout úvod do Beancountu (viz [dokumentace](https://beancount.github.io/docs/index.html)) ani do podvojného účetnictví (viz např. [tento detailní průvodce](https://beancount.github.io/docs/command_line_accounting_in_context.html)). Níže uvedu alespoň pár příkladů a ukázek jako malou ochutnávku.

V případě zájmu je možné najít všechny příklady v následujícím repozitáři:

``` sh
git clone https://github.com/peberanek/beancount-examples.git
```

Pro instalaci balíčků je použit moderní rychlý správce závislostí [uv](https://docs.astral.sh/uv/):

``` sh
cd beancount-examples/
uv sync
```

### Ukázková účetní kniha

Níže následuje komentovaný příklad velmi jednoduché účetní knihy (anglicky _ledger_):

<div class="annotate" markdown>

``` beancount title="ledger.beancount"
; Options (1)
option "name_assets" "Majetek" (12)
option "name_liabilities" "Zavazky" (13)
option "name_equity" "Kapital" (14)
option "name_income" "Prijmy"
option "name_expenses" "Vydaje"
option "operating_currency" "CZK" (11)

; Ucty (2)
2025-01-01 open Majetek:Banky:Easy-Bank:BU     CZK (3)
2025-01-01 open Majetek:Banky:Easy-Bank:BU-EUR EUR (4)
2025-01-01 open Majetek:Hotovost:Penezenka     CZK
2025-01-01 open Kapital:Pocatecni-stav         CZK, EUR (5)
2025-01-01 open Prijmy:Zamestnani:ABConsult    CZK
2025-01-01 open Vydaje:Zakladni-potreby        CZK
  note: "jidlo, zakladni spotrebni zbozi a sluzby" (6)

; Transakce (7)
2025-01-01 * "Pocatecni stav"
  Majetek:Banky:Easy-Bank:BU      50000 CZK
  Majetek:Banky:Easy-Bank:BU-EUR   2000 EUR
  Majetek:Hotovost:Penezenka        510 CZK
  Kapital:Pocatecni-stav (8)

2025-01-02 * "Restaurace Koruna" "Obed" (9)
  transaction_id: "123456789" (10)
  Majetek:Banky:Easy-Bank:BU       -200 CZK
  Vydaje:Zakladni-potreby

2025-01-15 * "ABConsult" "Vyplata mzdy"
  transaction_id: "123456790"
  Majetek:Banky:Easy-Bank:BU      50000 CZK
  Prijmy:Zamestnani:ABConsult

2025-01-20 * "Easy Bank" "Vyber z bankomatu"
  transaction_id: "123456791"
  Majetek:Banky:Easy-Bank:BU     -10000 CZK
  Majetek:Hotovost:Penezenka

2025-01-31 * "Souhrn utraty za jidlo"
  Majetek:Hotovost:Penezenka      -6000 CZK
  Vydaje:Zakladni-potreby
```

</div>

1.  `;` uvozuje komentáře. Nastavení níže umožňují používat vlastní názvy kategorií účtů místo anglických Assets, Liabilities atd. Více viz [Options](https://beancount.github.io/docs/beancount_language_syntax.html#options) a [Beancount Options Reference](https://beancount.github.io/docs/beancount_options_reference.html).
2.  Více viz [Accounts](https://beancount.github.io/docs/beancount_language_syntax.html#accounts)
3.  BU je zkratka pro "běžný účet"
4.  BU v Eurech. Koncovka `-EUR` je jen moje konvence pro vytváření unikátních názvů účtů.
5.  Je možné mít více měn na jednom účtu. V praxi to ale nedoporučuji (až na výjimky, jako je tato), protože při větším množství transakcí se ztrácí přehlednost.
6.  Volitelná metadata. Každá direktiva (řádek začínající datumem) může mít neomezené množství metadat. Více viz [Metadata](https://beancount.github.io/docs/beancount_language_syntax.html#metadata_1).
7.  Transakce je nejčastější direktivou, nicméně existují i další typy direktiv. Více viz [Directives](https://beancount.github.io/docs/beancount_design_doc.html#directives)
8.  Částka se dopočítá se automaticky, pokud to kontext dovoluje. Více viz [Elision of Amounts](https://beancount.github.io/docs/beancount_design_doc.html#elision-of-amounts)
9.  Transakce má nejen popis `"Obed"`, ale i protistranu (_Payee_) `"Restaurace Koruna"`. `*` je příznak (_Flag_) a znamená, že transakce je v pořádku. Pomocí příznaku `!` lze označit transakce, co potřebují další kontrolu. Technicky existují i další příznaky, viz [Flags](https://github.com/beancount/beancount/blob/master/beancount/core/flags.py).
10. Možnost přidávat volitelná metadata, v tomto případě ID transakce, je velmi praktická. Např. pro pozdější kontrolu při importu, zda už daná transakce v knize a na daném účtu existuje. Podobná metadata bývají dostupná při volání přes bankovní nebo burzovní API.
11. Měna preferovaná pro reporty. Vyžadováno nástrojem Fava. Viz další kapitola.
12. Majetek, tedy to co vlastním.
13. Závazky, tedy to co dlužím.
14. Vlastní kapitál neboli čisté jmění. Automaticky vypočtený rozdíl mezi majetkem a závazky.

!!! Poznámka

    Třebaže Beancount plně podporuje diakritiku, v praxi se mi osvědčilo ji nepoužívat. Píšu bez ní rychleji. Samozřejmě záleži na vkusu, resp. rozložení klávesnice.

### Grafické uživatelské rozhraní Fava

Výše uvedenou knihu lze prohlížet a editovat pomocí grafického uživatelského rozhraní [Fava](https://beancount.github.io/fava/).

``` sh
uv run fava ledger.beancount
```

Aplikace běží jako server dostupný na adrese `http://127.0.0.1:5000` (adresa serveru by se měla objevit ve výstupu příkazu).

Níže přidávám několik komentovaných screenshotů:

![Fava screenshot](../assets/images/fava-1.png)
/// caption
Přehled příjmů a výdajů
///

Obrázek výše: Kvůli zachování účetních principů vychází kladné příjmy jako záporné číslo, což je ze začátku dost neintuitivní. Jednou z možných pomůcek je představa, že to jsou peníze, které někomu jinému ubyly.

![Fava screenshot](../assets/images/fava-2.png)
/// caption
Rozvaha
///

Obrázek výše: Namísto anglických označení Assets, Liabilities a Equity používám raději Majetek, Závazky a Kapitál (automaticky vypočítané čisté jmění, tj. rozdíl mezi majetkem a závazky; princip záporného znaménka je stejný jako v případě příjmů - viz výše).

![Fava screenshot](../assets/images/fava-5.png)
/// caption
Transakční žurnál
///

Obrázek výše: Všechny transakce, resp. direktivy, jsou přehledně uvedeny v žurnálu. V žurnálu se dá filtrovat, ať už se jedná o typ direktivy, časové období, účet, tag nebo třeba protistranu (Payee).

![Fava screenshot](../assets/images/fava-3.png)
/// caption
Přehled transakcí na běžném účtu
///

Obrázek výše: Po klikutí na název účtu se zobrazí transakce spojené s daným účtem. V horní části obrázku můžeme vidět i jednoduchou vizualizaci přírůstku a úbytku prostředků na účtu.

![Fava screenshot](../assets/images/fava-4.png)
/// caption
Vestavěný editor transakcí
///

Obrázek výše: Po kliknutí na datum transakce je možné transakci editovat.

!!! Poznámka

    Pro zájemce vytvořili správci aplikace Fava i [interaktivní demo](https://fava.pythonanywhere.com) s komplexní účetní knihou.

### Volání z Pythonu

Jedním z benefitů Beancountu je, že ho jde volat i jako knihovnu. Např. takto:

``` py title="read_transaction.py"
"""Read first transaction in `./ledger.beancount` and print it as a Python object."""

from beancount.core.data import filter_txns
from beancount.loader import load_file
from rich import print as rprint

entries, errors, options_map = load_file("ledger.beancount")
transaction = next(filter_txns(entries))

rprint(transaction)
```

Provést instrukce v souboru výše jde např. takto:

``` sh
uv run python3 read_transaction.py
```

Výstup je následující:

``` py
Transaction(
    meta={
        'filename': '/home/petr/tmp/beancount-examples/ledger.beancount',
        'lineno': 19,
        '__tolerances__': {}
    },
    date=datetime.date(2025, 1, 1),
    flag='*',
    payee=None,
    narration='Pocatecni stav',
    tags=frozenset(),
    links=frozenset(),
    postings=[
        Posting(
            account='Majetek:Banky:Easy-Bank:BU',
            units=50000 CZK,
            cost=None,
            price=None,
            flag=None,
            meta={'filename': '/home/petr/tmp/beancount-examples/ledger.beancount', 'lineno': 20}
        ),
        Posting(
            account='Majetek:Hotovost:Penezenka',
            units=510 CZK,
            cost=None,
            price=None,
            flag=None,
            meta={'filename': '/home/petr/tmp/beancount-examples/ledger.beancount', 'lineno': 22}
        ),
        Posting(
            account='Kapital:Pocatecni-stav',
            units=-50510 CZK,
            cost=None,
            price=None,
            flag=None,
            meta={
                'filename': '/home/petr/tmp/beancount-examples/ledger.beancount',
                'lineno': 23,
                '__automatic__': True
            }
        ),
        Posting(
            account='Majetek:Banky:Easy-Bank:BU-EUR',
            units=2000 EUR,
            cost=None,
            price=None,
            flag=None,
            meta={'filename': '/home/petr/tmp/beancount-examples/ledger.beancount', 'lineno': 21}
        ),
        Posting(
            account='Kapital:Pocatecni-stav',
            units=-2000 EUR,
            cost=None,
            price=None,
            flag=None,
            meta={
                'filename': '/home/petr/tmp/beancount-examples/ledger.beancount',
                'lineno': 23,
                '__automatic__': True
            }
        )
    ]
)
```

Transakce jde i zapisovat:

``` py title="write_transaction.py"
"""Write a Beancount Transaction to stdout."""

from beancount.core.data import Transaction, Posting, EMPTY_SET, Amount
from beancount.core.flags import FLAG_OKAY
from beancount.parser.printer import print_entry
import datetime
from decimal import Decimal

transaction = Transaction(
    meta={"transaction_id": "123456789"},
    date=datetime.date(2025, 1, 1),
    flag=FLAG_OKAY,
    payee="Easy Bank",
    narration="Vyber hotovosti",
    tags=EMPTY_SET,
    links=EMPTY_SET,
    postings=[
        Posting(
            account="Majetek:Banky:Easy-Bank:BU",
            units=Amount(Decimal(-1000), "CZK"),
            cost=None,
            price=None,
            flag=None,
            meta={},
        ),
        Posting(
            account="Majetek:Hotovost:Penezenka",
            units=Amount(Decimal(1000), "CZK"),
            cost=None,
            price=None,
            flag=None,
            meta={},
        ),
    ],
)

print_entry(transaction)

```

Po provedení instrukcí v souboru získáme výstup ve formě transakce ve formátu Beancount.

``` sh
uv run python3 write_transaction.py
```

``` beancount
2025-01-01 * "Easy Bank" "Vyber hotovosti"
  transaction_id: "123456789"
  Majetek:Banky:Easy-Bank:BU  -1000 CZK
  Majetek:Hotovost:Penezenka   1000 CZK
```

Transakce nemusí být nutně validní. To je výhoda v případě, že potřebuji vytvořit transakci, pro kterou nemám kompletní informace a budu ji manuálně doplňovat. Případně lze transakci označit pomocí `FLAG_WARNING` namísto `FLAG_OK` v případech, kdy je transakce validní, ale stejně bude potřebovat další kontrolu.

Svého času jsem se rozhodl napsat [Beanclerk](https://github.com/peberanek/beanclerk) (framework pro import transakcí prostřednictvím API). Řadu věcí by určitě šlo udělat lépe, nicméně funkci spolehlivě plní, takže ho uvádím jako studijní příklad.

### Výhody a nevýhody

Zásadní výhodou Beancountu je pro mě flexibilita:

* jde používat s dalšími příkazy jako `git`, `grep` nebo `sed`,
* vedle vestavěných příkazů jako `bean-check` (validace účetní knihy) jde doinstalovat další pomocné aplikace jako již zmíněná Fava, [beangulp](https://github.com/beancount/beangulp) (framework pro importování transakcí) nebo [pricehist](https://gitlab.com/chrisberkhout/pricehist) (importování směnných kurzů a cen aktiv).
* díky podpoře pro prakticky jakékoliv aktivum (cizí měny, kryptoměny, akcie apod.) a možnosti zaznamenávat nákupní ceny (Cost basis) jde použít pro obchodování a daňové účely,
* funkcionalitu jde libovolně rozšiřovat pomocí [systému pluginů](https://beancount.github.io/docs/beancount_scripting_plugins.html) nebo voláním Beancountu jako knihovny Pythonu (viz [API reference](https://beancount.github.io/docs/api_reference/index.html)),
* už dříve jsem psal, že [soubor, resp. data jsou důležitější než aplikace](../posts/soubor-je-vic-nez-aplikace.md), a Beancount tuto filozofii naplňuje,
* vzhledem k tomu, že účetní kniha je textový dokument, nabízí se zde zpracování pomocí velkých jazykových modelů (ideálně lokálně běžících - pro větší soukromí). Jak známo, jazykové modely nebývají přesné ve výpočtech, ale zároveň mohou volat nástroje (např. udělat dotaz pomocí [Beanquery MCP](https://github.com/vanto/beanquery-mcp)). V praxi jsem zatím neměl potřebu to využít, takže uvidíme.

Dále oceňuji praktická rozšíření pro různé textové editory (např. pro [VSCode](https://marketplace.visualstudio.com/items?itemName=Lencerf.beancount)) a komunitní podporu formou [mailing listu (Google group)](https://groups.google.com/g/beancount).

Co se týče dokumentace, ta je na jednu stranu velmi propracovaná, ale zároveň nepříliš udržovaná. Problém je v tom, že většina informací platí pro starší verzi Beancountu (v2), která má oproti nejnovější verzi (v3) několik podstatných rozdílů, což bývá pro začátečníky matoucí.

Tím se dostávám i ke dvěma hlavním nevýhodám:

* autor Beancountu - Martin Blais - nemá v posledních letech na vývoj a udržování moc času, takže opravy a nové funkce přicházejí spíše sporadicky,
* při velkém množství záznamů může být zpracování citelně pomalé. Ve staré účetní knize jsem měl okolo 8 tisíc transakcí, řadu z nich s nákupní cenou aktiva, a výpočty trvaly i několik vteřin, což začalo zpomalovat kontrolu v rozšíření pro VSCode (viz výše). Před rokem a půl jsem proto založil novou účetní knihu (od 1.1.2024, k dnešnímu dni cca 1400 transakcí) a rychlost je opět velmi svižná.

## Faktory udržitelnosti

Vedení osobního účetnictví není snadné a vyžaduje čas a úsilí. Navíc, naše finanční realita a některé účetní technikálie mohou být frustrující. Ze začátku jsem se na to i několikrát vykašlal, abych se ke svému "finančnímu přehledu" zase dříve či později vrátil. Protože mít přehled se mi v průběhu času vyplácí víc, než ho nemít. Níže uvádím 3 faktory, které vnímám jako zásadní pro dlouhodobou udržitelnost celé téhle aktivity:

### Jednoduchost

> Simplicity changes behavior.  
-- [BJ Fogg](https://www.bjfogg.com/)

Samotné udržování účetních záznamů je nuda a proto jím chci trávit co nejméně času. Dříve jsem měl tendenci zaznamenávat přiliš mnoho detailů, což bylo často zbytečné. Např. každou provedenou transakci, rozepisovat některé položky:

- souhrn Zakladni potřeby
- jidlo v hotovosti - jednou za cas souhrn
- drazsi veci si poznacim, kvuli zarucni dobe - uz se hodilo - je jednoduzsi vyhledat v ucetni knize nez hledat uctenku

Začít se dá třeba jen s tužkou, papírem a otázkou "Jak to, že mi každý měsíc zbyde jen tolik a tolik? (Pokud vůbec něco)", "Kolik můžu a chci investovat?" nebo "Kam vlastně moje peníze tečou?". Člověk postupně začne zjišťovat, kolik peněz utrácí úplně zbytečně, a přirozeně se začnou rodit nápady na optimalizaci. Na nějakou dobu nejspíš vystačí jen Excel, resp. Calc.

Porozumět účetním pojmům jako aktiva, pasiva, náklady a výnosy může být složité. Mentálně jednodužší mi přijde používat označení jako majetek (to co mám), závazky (to co dlužím), kapitál (nebo též _čisté jmění_; rozdíl mezi majetkem a závazky), příjmy a výdaje.

Také se mi v praxi osvědčilo účtovat jen to podstatné a neztrácet čas příliš velkými detaily. Např. výdaje za jídlo (většinou) platím v hotovosti, jednou za čas spočítám rozdíl a ten zaúčtuji. Překvapivě tak zůstane velmi málo transakcí, které je potřeba zaúčtovat ručně, zvlášť v kombinaci s automatickým importem dat z banky. (Doporučení od autora Beancountu. Díky!)

### Pravidelnost

Když se nám daří udržovat věci jednoduché, máme pak větší kapacitu dělat je pravidelně. Ze začátku mi hodně psychicky pomáhalo držet své peníze pod kontrolou, takže jsem si zapisoval transakce každý den ráno. Byl to takový rituál. Dnes už mi díky automatizaci stačí udělat si sezení jednou za týden. V tomhle jsem asi stále trochu extrém. Obecně mi přijde, že lidem stačí sezení jednou za měsíc.

Pravidelnost je pro mě zdrojem klidu. Co nesnese odklad (máloco), to vyřeším hned a zbytek můžu pustit z hlavy. Buď mě na to upozorní notifikace (custom skript pro Beancount), nebo se k tomu dostanu při příštím sezení. Oproti finančnímu stresu před pádem na dno to je velká úleva.

### Automatizace
* Automatizace může být jednoduchá (Excel) i sofistikovaná (Beancount, Beangulp, stahování přes API, Beangrow apod.).
* snizuje casove a mentalni naklady na udrzbu - podporuje jednoduchost a pravidelnost
* automatizace usetri hodne mentalni namahy a predchazi chybam - klicova pro udrzitelnost

## shrnuti, ma to smysl? benefity pro me, co jsem se naucil
* mam prehled, vetsi sebejistotu, financni rozhodnuti jsou planovana (prirozene)
* pravidelnost, stabilni zaklady a navyky pro financni investovani
* budovani rezervy - pravidelnost dela divy, pozitivni zkusenost -> zkusenost pro investovani?
* data pro vypocet dani
* Co je osobni ucetnictvi?
    * prehled majetku a zavazku, prijmu a vydaju
    * pravidelna aktivita - byt v kontaktu a vsimavy ke svemu financnimu zivotu. Uvedomeni si svych financnich navyku. Odvaha nenechat se dal ojebavat.
    * rozhodovani na zaklade informaci, nikoliv emoci
