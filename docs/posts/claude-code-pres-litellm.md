---
date: 2025-10-03
tags:
  - ai
  - ai-agents
  - claude-code
  - litellm
  - fish-shell
---

# Claude Code přes LiteLLM

Nedávno jsme s pomocí kolegů z e-INFRA CZ rozjeli univerzitní instanci LiteLLM ve funkci AI API Gateway. Dají se tak poskytovat různé modely generativní AI přes API. Návod [v dokumentaci LiteLLM](https://docs.litellm.ai/docs/tutorials/claude_responses_api) je vcelku přímočary, nicméně jsem narazil na pár detailů.

Aby bylo možné používat Claude Code bez předplatného, je potřeba nastavit následující proměnné prostředí:

``` bash
export ANTHROPIC_AUTH_TOKEN="<GATEWAY-API-KEY>"
export ANTHROPIC_BASE_URL="<GATEWAY-URL>"
```

Vytvořil jsem si virtuální API klíč, který může volat všechny modely od Anthropic jako `anthropic/*`, což je jednodužší, než každý model přidávat manuálně. Jednotlivé modely je pak nutné volat např. jako `anthropic/claude-sonnet-4-5-20250929`. Nestačí jen `claude-sonnet-4-5-20250929`, což je defaultní chování Claude Code a vrátí se tím pádem error, že model nebyl na gateway nalezen. Vyřešit se to dá buď explicitním nastavením modelu přes přepínač:

``` bash
claude --model anthropic/claude-sonnet-4-5-20250929l
```

Nebo pohodlně přes příslušnou proměnnou prostředí. Model pak není třeba uvádět.

``` bash
export ANTHROPIC_MODEL="anthropic/claude-sonnet-4-5-20250929"
```

!!! Poznámka

    Nově používám Fish shell, a nastavení těchto proměnných persistentním způsobem (obdobou záznamu v `.bashrc`) mi dalo trochu zabrat. Fish je velmi ergonomický, nicméně některé věci jsou oproti Bashi celkem nezvyk. Pomohl mi opět Claude:

    ``` sh
    set -Ux ANTHROPIC_AUTH_TOKEN <GATEWAY-API-KEY>
    set -Ux ANTHROPIC_BASE_URL <GATEWAY-URL>
    set -Ux ANTHROPIC_MODEL anthropic/claude-sonnet-4-5-20250929
    ```

    Hotnoty proměných se uloží a následně exportují ze souboru `.config/fish/fish_variables`.
