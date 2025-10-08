---
date: 2025-06-29
tags:
  - ai
  - generative-ai
  - software-development
  - jon-gjengset
  - intelligence-augmentation
---

# Limity programování s asistencí AI

Nedávno jsem psal o tom, jak se díky nástupu jazykových modelů postupně [mění role vývojáře](../posts/menici-se-role-vyvojare.md). Jon Gjengset, autor knihy [Rust for Rustaceans](https://rust-for-rustaceans.com/), nabízí pohled na jeden z limitů, na které umělá intelince, resp. algoritmy strojového učení, naráží (viz jeho [lednové Q&A](https://rust-for-rustaceans.com/) (zvýraznění níže je moje)):

> I think in particular **where [machine learning] works really well is when you have either pattern matching or pattern recognition, where you have a lot of data to source those patterns from.** So I don’t generally think of machine learning as being smart. I think of it as being really good at spotting patterns that people have seen before, or replicating patterns that have been seen before. And that could include combining patterns in—let’s call them—novel ways, but at least combining them in some way that might appear novel.
> 
> I think there are a number of maybe surprising areas where this works really well. One of them is code generation. **I don’t use it a lot for my coding, and there are a couple of reasons for that, but one that I’ve touched on in the past is that the code I tend to write now, and the code I was writing at AWS, and the code I was writing during my PhD, was not very standard,** for lack of a better word. Like, most of the code—it is unclear if anyone had written quite that code before. That’s not the case for a lot of software development.

<!-- more -->

> So for a lot of software development, if you’re building—I don’t know—a website, being the canonical example, but if you’re building anything that interfaces with AWS services, or you’re just, like, interfacing with the Discord API, like things where there’s a bunch of code that does something kind of similar, there’s a lot more of the pattern that you want to do represented in the data that the machine learning models have already seen, and so they’re better at replicating that well.
> 
> Whereas, if I asked it to, I don’t know, implement partially stateful incremental view materialization, even if I did it function by function, I think it would struggle, because there’s not really anything else for it to base it on. **There’s no pattern it can repeat; there's not even really a combination of patterns it can repeat. It’s not to say it could never be good at it—it’s just I haven’t found it particularly compelling for that.**
> 
> [...]
>
> So, overall, I think machine learning has some really good applications, but I do not think that it is a thing to rely on for everything, because I think the moment you move away from well-established patterns, it doesn’t work very well at all. But where you can find those patterns, it works extremely well.  
