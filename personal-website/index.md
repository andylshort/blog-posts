---
publicationDate: 2023-09-08
published: false
subtitle: The Complexity of Simplicity
tags:
- project
- web
title: How I Made My Personal Website
---

This website is simple. That's all it needs to be. I'm a firm believer that most everything shouldn't overstep their bounds: they should do one thing, and do that one thing well. Websites. Software. Pens. Toilet roll. You name it. Usually, if something aims to do multiple different things, as opposed to one, I find it will do all of them incompletely and poorly. However, this is a whole topic of conversation I'd like to save for another time. To skip past my justification and head straight to the implementation details, [click here](#implementation). Otherwise, read on!

## Motivation

I'm not in the business of web design, so naturally this website doesn't need bloated JavaScript libraries for client-side rendering and the likes. Nor am I in the business of stealing your personal data, hence the lack of advertisements, tracker scripts, and analytics. All I want is a few simple, static landing pages and a set of blog posts that is straightforward to add to. Simple, right?

Inspiration: (<https://sequoia.makes.software/lets-code-it-static-site-generator/>)

In no particular order, my requirements were as follows:

* Parsing of Markdown files to HTML for simple blog posts
* CSS that I can inline to reduce HTTP requests
* Some way of templating pages for modularity's sake
* An automatic way to link pages together, such as having a list of blog posts on the index page
* Static pages - no dynamism, client-side rendering, potential for security issues

Ironically, achieving this simplicity involved unnecessary complexity. WordPress was out as I didn't want an entire system to maintain, keep up-to-date with security patches, nor did I want, or even need, every feature that it has. Being computer savvy, I didn't mind rolling my own system. I wanted to steer clear of nodejs as setting up a whole chain of dependencies and workflows using things like gulp or webpack is overkill, annoying to setup, [prone to breaking through no fault of your own](https://news.ycombinator.com/item?id=22979245). For someone not in the know, it's impenetrable.

Client-side rendering frameworks (just JavaScript or CSS frameworks in general) are out too due to inclusion of unnecessary and unused features, increased file size or dependence on requests to CDNs, and just general need to learn proprietary details specific to each. Which frameworks would you even pick? The new flavour-of-the-month pick with no documentation? Vue or React or Preact or...? There are nascent technologies bubbling up to the surface of Hacker News and GitHub daily and it feels like I'd be building on an ever-shifting foundation of sand. No thanks.

The landscape seems to be the same with static site generators. The breadth of options [is impressive](https://www.staticgen.com/). I had brief success with Hugo, with a simple website being a simple `brew install hugo` and `hugo new site ...` away. What it floundered on was its verbosity and subpar documentation. A lot of its templating syntax, as well as its need for subfolders, lots of small files and constituent parts, was verbose and cumbersome. There were few examples either from first- or third-party sources that helped. I found I needed to install or build an entire theme as well in order to style the website competently. Why an *entire theme*? Even changing the url of blogs to `post/yyyy/mm/dd/title` wasn't intuitive. Nothing _just worked_.

Then, one day, I stumbled upon [this article](https://k1ss.org/blog/20191004a) from the creator of KISS Linux, Dylan Araps. In his post, he detailed the lengths he'd gone to build and optimise the KISS Linux website for simplicity. Not only did it inspire me with ideas and techniques that I could incorporate into my website, but it also reassured me that my pursuit of bare simplicity is not a solitary one.

## Implementation
<a id="implementation"></a>

All of the blog posts (this one included) are generated with [Pandoc](https://pandoc.org). It has a simple templating syntax, ability to pass in HTML snippets, variables as command-line parameters, as well as having enhancements such as syntax highlighting and Markdown footnotes! I can just throw a Markdown file at it and out comes nice, static HTML. (As an aside, Pandoc can translate from Markdown to LaTeX. This will come in handy when I'm looking to draft papers during the course of my PhD!)

These fruits were not as low-hanging as first suspected. Pandoc generates each page in isolation, links between pages need to be scripted. Using a Python script, I globbed all of the blog posts to extract the front matter from them, append additional information, and stored these both in a YAML file, that gets passed to the home page to make the list of recent posts, and a Python object that I can iterate over to build each post page, passing in each piece of metadata on the command line[^1].

[^1]: A syntax or parameter to pass in an array of variables would help with scripting, I feel.

The blog posts follow one template, the index page has its own. The `<head>` element, `<header>`, `<nav>`, and `<footer>` elements are common to every page, so are abstracted out into their own files and composed together at build time. Finally, the CSS is inlined in the `<head>` element for speed and to not require another HTTP request. Apart from the syntax highlighting code (which is also inlined), the CSS is hand-crafted (some might even say _artisanal_) to give a good reading experience. I work with computers and screens for a living hence value text in a readable font, that at large enough to read easily, serif fonts that are clear, not cramped, and can breathe.  To tie things together, there is an inlined, base64-encoded favicon to save another HTTP request, code blocks are styled using Pandoc's syntax highlighting, footnotes and all that good stuff is generated automatically by [Pandoc's enhanced markdown markup](https://pandoc.org/MANUAL.html#pandocs-markdown), and maths is handled by Pandoc itself with the `--mathjax` parameter.

## Conclusion

Surely, on the face of it, this seems more complicated than just typing `hugo` and leaving the details to something else? Not to me. I see it as only being a few lines of Python (minimal overhead, using minimal files) and a great markup translation tool to get the **exactly** how I want. The results are minimal, simple, clean, functional. Every aspect I want anything I make to embody.

There will always be further optimisations, performance improvements, code reduction to be made, tinkered with. For the time being, I'm content. The source code is available [on GitHub](https://github.com/andylshort/andyls.co.uk). My goal in the immediate future is to generate an RSS feed and tag pages for my blog. Being able to share and categorise my writing would be a nice thing to achieve.