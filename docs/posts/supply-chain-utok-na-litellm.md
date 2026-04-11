---
date: 2026-03-27
draft: true  # TODO: remove
tags:
  - TODO
---

# Supply chain útok na LiteLLM

> TLDR;
> 
> * The compromised PyPI packages were litellm==1.82.7 and litellm==1.82.8. Those packages have now been removed from PyPI.
> * We believe that the compromise originated from the Trivy dependency used in our CI/CD security scanning workflow.
> * Customers running the official LiteLLM Proxy Docker image were not impacted. That deployment path pins dependencies in requirements.txt and does not rely on the compromised PyPI packages.
> * We are pausing new LiteLLM releases until we complete a broader supply-chain review and confirm the release path is safe.  
> -- [Security Update: Suspected Supply Chain Incident (LiteLLM Blog)](https://docs.litellm.ai/blog/security-update-march-2026)

* napadeny byl pouze balicek na pypi.org, zdrojovy kod na githubu ne. https://docs.litellm.ai/blog/security-update-march-2026#who-is-affected
* Zajimave je, ze githubovy ucet autora LiteLLM neni dostupny (smazan, deaktivovan?): https://github.com/krrishdholakia
* trivy popis utoku (https://www.aquasec.com/blog/trivy-supply-chain-attack-what-you-need-to-know/) ukazuje sofistikovany utok na CI/CD a masivni sber credentials