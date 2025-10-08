---
date:
  created: 2025-04-20
  updated: 2025-06-08
tags:
  - ai
  - generative-ai
  - chatbots
  - open-webui
  - open-source
---

# Open WebUI jako rozšíření pro Rancher Desktop

V článku o [AI Sandboxu](../posts/open-source-ai-sandbox.md) jsem zmínil Open WebUI jakožto flexibilní rozhraní (chatbota) pro komunikaci s různými modely generativní AI. Nyní jsem zjistil, že je k dispozici i formou [rozšírení pro Rancher Desktop](https://www.suse.com/c/rancher_blog/rancher-desktop-1-17-with-open-webui-extension-and-more/) (a dokonce je součástí platformy [SUSE AI](https://documentation.suse.com/suse-ai/1.0/html/AI-deployment-intro/index.html)).

Musím říct, že instalace rozšíření nebyla úplně přímočará. Nainstaloval jsem Rancher Desktop a kliknul na instalaci rozšíření. Ta ale nedoběhla a zůstala tzv. viset, což je trochu nešťastná první zkušenost. Po restartu celé aplikace už ale instalace doběhla v pořádku. Líbí se mi, že Open WebUI běží přímo v okně Rancher Desktopu, takže se není potřeba nikam přepínat. Není ani potřeba vytvářet nového uživatele, vytvoří se defaultní uživatel `User`. Propojení s existující instancí Ollama proběhlo automaticky, což je taky fajn. Nevýhodou může být starší verze Open WebUI (0.5.20) oproti upstreamu (0.6.5).

_Update_: Vypnout autentizaci pro lokálního uživatele lze pomocí proměnné prostředí `WEBUI_AUTH`, nicméně to lze pouze v případě, že ještě nebyl vytvořen žádný uživatel. Více viz [dokumentace](https://docs.openwebui.com/getting-started/env-configuration#webui_auth).
