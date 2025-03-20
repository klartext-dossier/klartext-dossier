# Klartext/Dossier

This is the main repository of the klartext/dossier toolset for modern document generation.

The toolset consists of a number of elements:

klartext
:   *klartext* is a markup language that combines the power of XML and Markdown in a Pythonic way. This repository contains a parser library for that language.

htmlbook
:   [HTMLBook](https://oreillymedia.github.io/HTMLBook/) is a specified subset of XHTML used for typesetting books. This repository contains an extensible less/css stylesheet for [HTMLBook](https://oreillymedia.github.io/HTMLBook).

dossier-mdx
:   *dossier-mdx* provides a number of [Python Markdown](https://python-markdown.github.io) extensions for converting Markdown into [HTMLBook](https://oreillymedia.github.io/HTMLBook/) compliant XHTML.

dm
:   *dm* (dossier manager) is a tool that allows to define document generation pipelines for all kinds of generation scenarios. For example, it allows to convert klartext sources into proper PDF documents.

