---
date: 2026-05-17
tags:
  - automation
  - git
  - home-lab
  - open-source
---

# Automatické nasazení dokumentace s git `post-receive` hookem

Jak už jsem [psal dříve](../posts/upgrade-blogu.md), tento web je vytvořený s Material for MkDocs a nasazení probíhá automaticky pomocí [příslušné Github action](https://github.com/peberanek/peberanek.github.io/blob/24842d96bbf5ccd519564a1f720f1f0923cbc799/.github/workflows/building.yml). Je to velmi pohodlné, nemusím se o nic starat.

Zároveň už si nějakou dobu tvořím osobní znalostní bázi, také formou dokumentace pomocí Material for MkDocs (o tom třeba někdy v budoucnu). Pointa byla tvořit jí jednoduše v textových souborech (v Markdownu), a přitom ji mít dostupnou na všech zařízeních. Píšu si tam i dost soukromé věci, takže ji nechci mít vystavenou veřejně na internetu jako tenhle web. Logickou volbou bylo tedy zkusit ji nasadit v rámci nového [home labu](../posts/soukroma-vpn-s-tailscale.md).

Přemýšlel jsem, jak provádět nasazení automaticky a jednoduše. Claude mi navrh využít [git `post-receive` hook](https://git-scm.com/docs/githooks#post-receive) (který mimochodem nemá svůj `.sample` file v `.git/hooks`, což mě trochu překvapilo). Návrh se mi zalíbil. Jedná se o jeden shellový script, který dokumentaci sestaví potom co udělám `git push` do daného repozitáře (zmíněná znalostní báze je zároveň git repo). Výsledný web je přístupný přes VPN pomocí `tailscale serve`.

Níže je příklad zmíněného git hooku. (Znalostní bázi jsem pojmenoval jednoduše `knowledge`.)

```sh
#!/bin/bash
#
# Build and deploy MkDocs documentation when main branch is pushed.
#

# The usual Bash safety net
set -o errexit
set -o nounset
set -o noglob
set -o pipefail

clone_dir="${HOME}/build/knowledge"
web_dir="${HOME}/web/knowledge"

unset GIT_DIR  # The envvar confuses git when cd into a different dir

while read -r oldsha newsha refname; do
    if [[ "${refname}" == "refs/heads/main" ]]; then
        echo "Push to main detected, building docs..."
        cd "${clone_dir}"

        # The repo is meant as pull-only, local changes are overridden.
        git fetch origin
        git reset --hard origin/main

        /home/petr/.local/bin/uv run mkdocs build --clean
        rm -rf "${web_dir}"
        cp -r site/ "${web_dir}"
        echo "Done. Docs deployed to ${web_dir}"
    fi
done
```

Zprovoznit daný skript byla trochu fuška, protože shellové prostředí git hooku je omezené (proto je tam např. ta absolutní cesta k `uv`). Ale povedlo se. Zdá se, že to funguje dobře, a už jsem tenhle pattern použil i v jiném projektu.
