---
description: Finalize blog post for publication
agent: build
model: openrouter/openai/gpt-5.6-terra
---

1. Proofread the blog post at $1.

1. Generate tags for $1:
    1. Generate existing tags by running:
    ```sh
    uv run python list-tags.py
    ```

    Use existing tags to update `tags` in the post frontmatter. The final list may look like this:
    ```yaml
    tags:
    - ai
    - ai-agents
    - open-source
    ```

    When the post is about AI, always include tag `ai`.

4. Remove `draft: true` from $1 frontmatter, if present.

5. Fix date to current date, if it is a new article, or add `updated` date, if it is an update, e.g.:
    ```yaml
    date:
      created: 2026-05-04
      updated: 2026-05-08
    ```
