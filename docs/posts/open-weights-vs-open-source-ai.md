---
date: 2025-06-07
---

# Open Weights vs Open Source AI

Deep Dive audio overview (vygenerováno z článku odkazovaného níže pomocí NotebookLM):

<audio controls>
  <source src="../../assets/audio/deep_dive_open_weights.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>
<br>

[Open Weights: not quite what you’ve been told](https://opensource.org/ai/open-weights): Článek ukazuje, že "open-source" a Open Weights modely nejsou jedno a totéž. _Open Weights_ znamená přístup k finálním parametrům daného modelu, nikoliv však ke kódu použitému k vytvoření tréninkového datasetu, ani k datasetu samotnému, nebo alespoň k jeho detailnímu popisu pokud není možné z právních důvodů dataset zveřejnit. Open Weights modely je tak velmi těžné, né-li nemožné replikovat, auditovat, porozumět procesu jejich tréninku a tím pádem i všem aspektům jejich chování (např. skrytý bias).

<!-- more -->

Tato neprůhlednost může být problém jak pro regulátory (jak se na Open Weights dívá AI Act?), tak pro spolupráci na dalším vývoji. (Co se týče regulace, jeden z problémů vidím i v neporozumění základním pojmům, jako rozdíl mezi chatbotem a samotným modelem, kdy chatbot může sbírat citlivé údaje, ale samotný model nikoliv. Už jsem se v praxi setkal s tím, že toto neporozumění může vést ke snaze plošně odrazovat od používání čínských modelů, třebaže běží na vlastním hardware a používají je edukovaní uživatelé.)

> To better understand why Open Weights and Open Source AI differ so drastically, consider the following comparison:
>
> | **Feature** | **Open Weights** | **Open Source AI** |
> |-------------|------------------|-------------------|
> | **Weights & Biases** | Released | Released |
> | **Training Code** | Not Shared | Fully Shared |
> | **Intermediate Checkpoints** | Withheld | Nice to have |
> | **Training dataset** | Not Shared/Not disclosed | Released* |
> | **Training Data Composition** | Partially/Not Disclosed | Fully Disclosed |
>
> Clearly, Open Weights mark a notable advancement over fully proprietary solutions by offering the final model parameters. However, Open Source AI goes further by unlocking the entire development process. This holistic openness enables complete reproducibility, thorough bias audits, and robust community-driven improvements.
> 
> \* When legally allowed. [...]
