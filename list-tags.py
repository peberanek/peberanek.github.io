"""
List all unique tags from blog posts.

Scans all markdown files in docs/posts/ and extracts tags from their
YAML frontmatter, then outputs a sorted, deduplicated list.
"""

from typing import cast

import frontmatter
from pathlib import Path


def main() -> None:
    """Main function to list all tags."""
    posts_dir = Path("docs/posts")
    all_tags: set[str] = set()

    for md_file in posts_dir.glob("*.md"):
        post = frontmatter.load(str(md_file))
        if "tags" in post.metadata:
            tags = post.metadata["tags"]
            if isinstance(tags, list):
                all_tags.update(cast(list[str], tags))

    print(sorted(all_tags))


if __name__ == "__main__":
    main()
