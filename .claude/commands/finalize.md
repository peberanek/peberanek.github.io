---
description: Finalize blog post for publication
argument-hint: [blog-post-path]
allowed-tools: Bash(uv run python list-tags.py)
---

1. Read the blog post at 1$. Point out its weaknesses like speculation or incorrect claims. I may or may not want to resolve them.

2. Proofread the blog post at $1.

3. Generate tags for $1 using skill `generate-tags`.
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
