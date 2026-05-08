---
date: 2026-05-09
tags:
  - home-lab
  - linux
  - open-source
  - open-webui
  - simon-willison
---

# Soukromá VPN s Tailscale

Po [drobném zádrhelu](../posts/jak-vypnout-intel-rst.md) při přeměně starého laptopu na domácí server nastal čas se k němu připojit. Chtěl jsem při tom vyzkoušet službu [Tailscale](https://tailscale.com/), na kterou mě [přivedl Simon Willison](https://simonwillison.net/2025/Nov/7/codex-tailscale-spark/). A musím říct, že jsem velmi příjemně překvapen.

Tailscale se prezentuje jako platforma pro vytvoření bezpečné virtuální sítě postavená na moderním open source protokolu [WireGuard](https://www.wireguard.com/). Třebaže se jedná o komerční službu, platforma nabízí [velmi štědrý free tier pro osobní použití](https://tailscale.com/pricing), který pro můj domácí lab stačí.

## Instalace

Instalace byla přímočará. Lze použít [custom instalační script](https://tailscale.com/download) nebo [přidat příslušný repozitář manuálně](https://pkgs.tailscale.com/stable/) a nainstalovat prostřednictvím správce balíčků. (Ocenit musím pěkně zpracovanou [dokumentaci](https://tailscale.com/docs/how-to/quickstart) a přehledová videa.)

```sh
sudo apt install tailscale
```

Pak už jen stačí Tailscale spustit a přes odkaz na web přidat stroj do sítě.

```sh
sudo tailscale up
```

Tím se vytvoří persistentní služba `tailscaled` a stroj se pak připojuje do sítě automaticky.

Platforma funguje pro řadu operačních systémů, takže lze snadno přidat třeba zařízení s Androidem. Můžu se tak připojovat k běžícím službám (jako např. Open WebUI) i z telefonu, což je přesně use case, který jsem potřeboval vyřešit.

## Poznámky

* [Tailscale SSH](https://tailscale.com/docs/features/tailscale-ssh): Užitečná funkcionalita, díky které jsem nemusel vůbec řešit nastavování OpenSSH nebo SSH keys. Autentizace probíhá přes webové rozhraní Tailscale. Zdá se, že je defaultně zapnutý "check mode", kdy je nutné se po 12 hodinách znovu autentizovat. Zatím jsem neměl potřebu to měnit nebo vypnout.
* [Use ufw to lock down an Ubuntu server](https://tailscale.com/docs/how-to/secure-ubuntu-server-with-ufw): Návod jak nastavit Tailscale s UFW firewallem. Radost mi trochu kazí fakt, že např. Docker pravidla definovaná UFW zcela ignoruje, nicméně i to je řešitelné.
* Práci mi ušetřila funkcionalita [Tailscale Serve](https://tailscale.com/docs/features/tailscale-serve), díky které jsem zpřístupnil výše zmíněné Open WebUI na soukromé síti, aniž bych musel řešit věci jako HTTPS (které je v některých případech nutné).
```sh
sudo tailscale serve --bg http://localhost:8080
```
(Přepínač `--bg` způsobí, že se služba spustí na pozadí v perzistentním režimu, takže se i po restartu stroje znovu nastartuje.)
