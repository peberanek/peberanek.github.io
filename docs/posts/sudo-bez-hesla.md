---
date: 2025-03-20
---

# `sudo` bez hesla

Požádal jsem Clauda 3.7 Sonnet aby mi poradil s následující situací: mám shellový skript a některé příkazy vyžadují `sudo`, resp. spouštět příkaz s právy roota. Skript se spouští docela často a začíná být nepraktické pokaždé zadávat heslo. Claude přišel s návrhem povolit dané příkazy pomocí pluginu sudoers ("default sudo security policy plugin"; více viz `man sudoers`), který jsem do té doby neznal. Rovnou mi vypsal, co a jak mám nastavit:

``` sh
sudo visudo -f /etc/sudoers.d/update
```

A do souboru přidat např. následující:
```
myuser ALL=(root) NOPASSWD: /usr/bin/apt update, /usr/bin/apt upgrade -y, /usr/bin/snap refresh
```

Uživatel `myuser` může spouštět `/usr/bin/apt update`, `/usr/bin/apt upgrade -y`, a `/usr/bin/snap refresh` jako `root` bez nutnosti se autentizovat. Příkazy musí být zadány i včetně všech uvedených parametrů (tj. `apt upgrade -y`, cestu není třeba zadávat), jinak je heslo vyžadováno.

Vzhledem k rostoucím schopnostem a znalostem současných modelů začíná být pocitově jednodužší (i zábavnější) jako první konzultovat problém s chatbotem, než "jít hledat na internetu". A to nejen v situacích, kdy jsou související informace s velkou pravděpodobností hojně zastoupené v trénikových datasetech. "I blbej nápad je dobrej nápad. Ne sám o sobě, ale tím, že nás může mentálně odblokovat a nasměrovat k použitelnému řešení."
