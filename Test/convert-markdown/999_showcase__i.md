---
author:   Matthias Hölzer-Klüpfel
template: formal
company:  The Company, Inc.
doc_type: EXPL
doc_id:   1230
status:   Draft
keywords: a, b, c
language: en
subject:  A demonstration
version:  2019-06-11
---

# Dossier Markdown Showcase

[TOC]

## About Dossier Markdown

The “Dossier” documentation system uses a variant of the widely used “Markdown” markup language.

The markup language is specified in the [CommonMark Specification][CommonMarkSpec].

This showcase explains the use of the most prominent features of the markup language used by “Dossier”, and how they are rendered in the different output formats.

## Writing Documents

The following sections demonstrate how to write documents in the “Dossier” markup language.

### Writing simple text

Writing simple text is as simple as it can be: just type away the text. For example, the following markup

```md
This is a simple paragraph containing normal text.

This is another simple paragraph containing normal text.
```

will be rendered as

> This is a simple paragraph containing normal text.
>
> This is another simple paragraph containing normal text.

### Decorating text

Decorating text, e.g. to put emphasis on some terms, is not much more difficult. Those are the options:

```md
This paragraph has _italic_ text.

This one has **bold** text.
```

will be rendered as

> This paragraph has _italic_ text.
>
> This one has **bold** text.

### Lists and enumerations

There are two basic types of lists: ordered lists, aka enumerations, and unordered lists. Both are easy to write:

```md
Unordered list:

* first item
* second item
* third item
```

will be rendered as

> Unordered list:
>
> * first item
> * second item
> * third item

```md
Ordered list:

1. first item
2. second item
3. third item
```

will be rendered as

> Ordered list:
>
> 1. first item
> 2. second item
> 3. third item

Both types of lists can be nested:

```md
1. first item
2. second item
    * first subitem
    * second subitem
    * third subitem
3. third item
```

will be rendered as

> 1. first item
> 2. second item
>     * first subitem
>     * second subitem
>     * third subitem
> 3. third item

### Definition lists

Definition lists can be used, for example, to define terms:

```md
Foobar
: This is a Foobar

Killroy
: This is a Killroy
```

will be rendered as

> Foobar
> : This is a Foobar
>
> Killroy
> : This is a Killroy

### Checklists

Checklists can be added like this:

```md
* [ ] do something
* [ ] save the world
* [x] read a book
* [ ] do something else
```

will be rendered as

* [ ] do something
* [ ] save the world
* [x] read a book
* [ ] do something else

### Adding structure

Structure can be added to a document by using section headers:

```md
### Second level heading

### Another second level heading

#### And a third level
```

### Quoting text

There are several options available to quote text. First the simple inline quotes:

```md
This is a paragraph containing a <q>html quote</q>.

This is a paragraph containing a 'straight single quote'.

This is a paragraph containing a "straight double quote".

This is a paragraph containing a ‘typographic single quote’.

This is a paragraph containing a “typographic double quote”.
```

will be rendered as

> This is a paragraph containing a 'straight single quote'.
>
> This is a paragraph containing a "straight double quote".
>
> This is a paragraph containing a ‘typographic single quote’.
>
> This is a paragraph containing a “typographic double quote”.

Alternatively, sections of text can be quoted using a blockquote:

```md
> This is a quoted section of text.
```

will be rendered as

> > This is a quoted section of text.

### Quoting code

For quoting code or code sections, there are again two options:

1. inline code
2. code sections

```md
Inline `code` has `back-ticks around` it.
```

will be rendered as

Inline `code` has `back-ticks around` it.

```bash
git checkout -b featureA
```

will be rendered as

```bash
git checkout -b featureA
```

<!--- References --->

[CommonMarkSpec]: https://spec.commonmark.org/current
