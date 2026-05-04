---
date: 2026-05-04
tags:
  - linux
  - claude
---

# Jak vypnout Intel RST na laptopu Acer Aspire 3

V rámci testování aplikace, na které nyní pracuji, jsem si rozhodl vytvořit domácí server ze starého laptopu Acer Aspire 3. Při instalaci Ubuntu serveru jsem nicméně narazil na problém, kdy mi instalátor ohlásil, že nejsou k dispozici žádné disky pro instalaci systému, což mě překvapilo. Předinstalované Windowsy běžely bez problémů.

Zkusil jsem tedy rozjet Live session Ubuntu desktopu s tím, že disky zkusím zformátovat a mohlo by to pomoct. Instalátor Ubuntu desktopu mi také nahlásil problém s disky, konkrétně problém s aktivní Intel RST (Rapid Storage Technology), která neumožňovala v instalaci pokračovat. RST bylo třeba vypnout.

Třebaže jsem zkusil věc vyřešit s pomocí Claude Sonnet 4.6, nakonec mi to dalo celkem zabrat (viz shrnutí níže). Pointa byla vypnout RST v BIOSu. _Přepínač je defaultně skrytý_ a pro zobrazení je [nutné stisknout CTRL+s v příslušném menu v BIOSu](https://community.acer.com/en/discussion/comment/895185?tab=all&utm_source=community-share#Comment_895185).

<!-- more -->

Níže následuje shrnutí chatu s Claudem. Mimochodem mi takovéto shrnutí přijde jako zajímavý pattern pro uložení užitečných informací z chatu např. do osobní znalostní báze.

> # Ubuntu Server Installation on Acer Aspire 3 (N19C2) - RST Issue
>
> ## Problem
> Ubuntu Server installer could not find any drives due to Intel RST
> (Rapid Storage Technology) being enabled in firmware.
> 
> ## System Info
> - **Model:** Acer Aspire 3, N19C2
> - **BIOS:** Insyde Corp v1.11 (2020)
> - **Goal:** Clean Ubuntu Server installation (no dual boot)
> 
> ## Failed Approaches
> - No storage/SATA options visible in BIOS
> - Windows registry values (`iaStorV` and `storahci`) already set to 0
> - BIOS update (same version 1.11, newer date Oct 2020) — no change
> - F6 in BIOS only changes values, doesn't reveal hidden menus
> 
> ## Solution
> Hidden BIOS option revealed via **Ctrl+S** on the main BIOS tab:
> - Switched SATA operation mode from **RST** to **AHCI**
> - Option is hidden by default on Acer Aspire 3
> 
> ## References
> - [Ubuntu docs - Intel RST during Ubuntu installation][1]
> - [Acer Community Forum - disabling RST][2]
> 
> [1]: https://documentation.ubuntu.com/desktop/en/latest/reference/intel-rst-during-ubuntu-installation/
> [2]: https://community.acer.com/en/discussion/comment/895185?tab=all&utm_source=community-share#Comment_895185 

## Lessons Learned

* Finální informaci (CTRL+s v Biosu pro zobrazení skrytého přepínače pro SATA) mi model neporadil (model byl blízko, radil klávesu F6, která je ale rezervovaná pro změnu hodnot). Používal jsem Claude Sonnet 4.6 _bez přístupu k internetu_. Příště bude užitečnější zvolit model s online přístupem.
