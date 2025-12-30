---
date: 2025-12-30
tags:
  - creativity
  - linux
---

# Trnitá cesta k vyzkoušení MetaHuman pro Unreal Engine 5

Občas si hraju s digitální kresbou a kvůli proporcím si pomáhám 3D modely v populárním open source editoru Blender. Nejtěžší jsou pro mě proporce lidské postavy, a tak jsem vyzkoušel různá rozšíření jako [MakeHuman](https://static.makehumancommunity.org/) nebo [Human Generator](https://humgen3d.com/). Na rychlé pokusy postačí, ale dříve nebo později se projeví jejich limity v detailech a přizpůsobitelnosti modelů.

Nedávno jsem zjistil, že existuje - k mému údivu bezplatně - pokročilý framework [MetaHuman](https://www.metahuman.com/) pro Unreal Engine. Výsledné modely vypadají velmi dobře, Unreal Engine má instalátor i pro Linux, takže mi to nedalo a pustil jsem se do instalace. Dosti trnité. Aneb jak by řekl klasik - byla to zkoušenost.

## MetaHuman na Linuxu? Ano i ne

Unreal Engine 5 je sice "zdarma" pro jednotlivce i společnosti [s ročními výnosy do 1 milionu USD](https://www.unrealengine.com/en-US/license), ale pro stažení je nutné přihlášení přes účet u Epic Games. OK, "zdarma" tedy bude pravděpodobně znamenat cílenou reklamu, neboli výrobce si to zkusí vybrat jinde. S tím jsem v rámci testování schopen žít. Horší už je to s doporučenými požadavky na operační systém - _Ubuntu 22.04_. To má sice stále oficiální podporu, ale dnes už je to přecejen starší vydání. Na mém stroji momentálně běží _Ubuntu 25.10_, takže nezbývalo, než to prostě vyzkoušet a připravit se na potenciální problémy.

<!-- more -->

Po stažení zazipovaného balíčku (30 GB) se bohužel problémy objevily - verze 5.7 byla v podstatě nepoužitelná a často padala. Zkusil jsem tedy verzi 5.6, která už fungovala slušně nepadala tak často. V ní ale nefunguje MetaHuman (resp. možnost vytvářet postavy, dostupná na Linuxu až [od verze 5.7](https://www.metahuman.com/en-US/releases/metahuman-5-7-is-now-available)). Existuje sice návod jak [rozjet verzi 5.7 v kontejneru](https://dev.epicgames.com/community/learning/tutorials/KWvY/metahuman-the-easiest-way-to-run-unreal-engine-5-7-natively-on-any-linux-distro), ale bez podpory GPU. Než se trápit s nastavováním nebo pokusy s virtuálními stroji, dal jsem ještě šanci svému staršímu laptopu s Windows 11. Má sice jen 8 GB RAM a slabší Nvidii (2 GB VRAM), ale naivně jsem doufal, že na něm třeba MetaHuman nějak poběží, a vyzkouším alespoň nějaké základní funkce.

Instalace Unreal Engine byla sice přímočará a aplikace se rozjela, ale pracovat s ní prakticky nešlo. Tahle možnost tedy taky padla, nicméně zvědavost mi nedala to vzdát.

## Instalace Windows 11

Než se trápit s Linuxem, nastal čas nainstalovat Windows. Zvažoval jsem zmenšit stávající linuxový oddíl a udělat dual boot. Nakonec jsem si ale vzpomněl na jeden volný SSD disk, díky kterému by odpadla nutnost zasahovat do stávajícího systému. Obratem jsem ho zapojil a šel vytvářet instalační flashku s Windows 11.

Příprava a instalace byly přímočaré přesně do chvíle, než mi instalátor Windows ohlásil, že mému stroji chybí Secure Boot a TPM 2.0. Jak jsem zjistil později, obojí by šlo nejspíš zapnout, nicméně při hledání řešení mě zaujal program [Rufus](https://github.com/pbatard/rufus). Ten umí v instalačním obrazu vypnout nejen tyto požadavky, ale např. i nutnost přihlášení přes účet Microsoft, nebo automaticky vytvořit lokálního uživatele. Zajímavé a praktické.

Rufus tedy problém se Secure Bootem a TPM vyřešil. O krok později si však instalátor nedokázal poradit s tím, že na SSDčku byla vytvořená partition s NTFS filesystémem. Partition neuměl ani smazat. V tu chvíli jsem si říkal, že to už není možný - past vedle pasti. Naštěstí po rebootu do Linuxu a odebrání partition pomocí Gnome Disks mohla instalace pokračovat. Uf.

V rámci tvorby obrazu jsem v souladu nastavením svého stroje vybral _Partition Scheme_ jako _MBR_. A to byla chyba. Při instalaci (po restartu) se totiž ukázálo, že z nějakého záhadného důvodu systém nenabootuje. Zkusil jsem tedy vypnout podporu pro BIOS a vytvořit nový instalační obraz s _Partition Scheme_ jako _GPT_... A instalace konečně doběhla. Zázrak.

Po několika hodinách boje jsem konečně nainstaloval i Unreal Engine 7 a zprovoznil MetaHuman framework. Musím říct, že modely v MetaHuman vypadají velmi dobře, ale to už je na jiný článek.
