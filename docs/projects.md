# Projects

## AI Sandbox

_Charles University_ (2024 - present)

The goal of this project is to provide users with access:

1. to an **advanced chat interface**, similar to ChatGPT, with the ability to chat with various models (GPT, Claude, Gemini), including open-weights models hosted on-premise.
2. to a **unified API** interface for researchers and developers.

The main arguments for such a solution are **cost-effectiveness** compared to bulk subscription purchases, reducing users' motivation to use **unapproved tools**, and **flexibility and control** over the platform and its functionality. The project has been inspired by [Harvard AI Sandbox](https://www.huit.harvard.edu/ai-sandbox), [Stanford AI Playground](https://uit.stanford.edu/aiplayground), and [Chat AI (e-INFRA CZ)](https://docs.cerit.io/en/docs/ai-as-a-service/chat-ai).

![Open WebUI](assets/images/open_webui.png)
/// caption
[Open WebUI](https://github.com/open-webui/open-webui) serves as the advanced chat interface
///

![LiteLLM](assets/images/litellm.png)
/// caption
[LiteLLM](https://github.com/BerriAI/litellm) provides the unified API, metrics, cost limiting and more
///

More information can be found at the links below:

* [Project architecture and demos](https://github.com/peberanek/ai-sandbox)
* [Documentation for users at Charles University](https://ai.cuni.cz/AI-75.html)

## Internal Testing Framework for LVM

_Red Hat_ (2019 - 2021)

This project started as an initiative to develop a new testing framework for LVM (Logical Volume Manager) integration tests, extending to High Availability Cluster testing.

The main motivation was to modernize our test suite - the **existing Perl-based tests had become difficult to maintain** due to their complexity and monolithic structure. Additionally, strong Perl skills were becoming increasingly rare among engineers. Since the rest of the team was already writing tests in Python and it had become a requirement for new quality engineers, moving to a Python-based framework was a natural choice. Eventually, it was decided to **build on [pytest](https://github.com/pytest-dev/pytest/)** due to its maturity and flexible plugin system.

Building a framework is not easy, and we learned a lot along the way. Surprisingly, **the technical problems** like integrating with existing infrastructure and tooling sometimes **proved less difficult than the non-technical ones** - explaining the long-term benefits of Python over Perl, or shifting from object-oriented to functional programming. One key observation was that these challenges needed to be addressed incrementally through small, practical use cases that clearly demonstrated the benefits. Making the framework as accessible as possible for newcomers was essential.

## Personal Finance

_personal project_ (2015 - present)

This long-term project helps me keep track of my money and stay financially organized. It is built on [Beancount](https://github.com/beancount/beancount) (double-entry accounting from text files), enhanced with automated transaction and data imports via various APIs ([Beanclerk](https://github.com/peberanek/beanclerk), [Fio Banka API](https://github.com/peberanek/fio-banka), [Creditas OpenAPI Client](https://github.com/peberanek/creditas)) - typically the most tedious part of personal accounting.

![Fava screenshot](assets/images/fava-2.png)
/// caption
Example Balance Sheet in [Fava](https://beancount.github.io/fava/)
///

You can find more about the motivation and real-world benefits of this approach in my article [Osobní účetnictví: Má to smysl?](posts/osobni-ucetnictvi.md)
