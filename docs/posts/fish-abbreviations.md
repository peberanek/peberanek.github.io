---
date: 2026-01-30
tags:
  - fish-shell
  - linux
---

# Fish Abbreviations

Při snaze ušetřit si psaní dlouhého příkazu (resp. hledání v historii) jsem narazil na zajímavou vlastnost Fish shellu, a to na [zkratky (Abbreviations)](https://fishshell.com/docs/current/cmds/abbr.html).

Zkratku jde vytvořit např. takto:
```sh
abbr --add webui 'WEBUI_AUTH=False open-webui serve'
```

!!! Poznámka

    Aby byla zkratka perzistentní, je potřeba ji přidat do [`config.fish`](https://fishshell.com/docs/current/language.html#configuration). Dokumentace doporučuje zkratku nejprve vypsat:
    ```sh
    > abbr
    abbr -a -- webui 'WEBUI_AUTH=False open-webui serve'
    ```

    A tento příkaz (tj. `abbr -a -- webui 'WEBUI_AUTH=False open-webui serve'`) pak uložit do konfiguračního souboru.

Výhodou oproti tradičním aliasům je, že po zadání zkratky `webui` se zkratka dá expandovat (typicky pomocí mezeníku nebo Enteru). Je tak zřejmé, jaký příkaz se bude spouštět a případně ho lze upravit.
