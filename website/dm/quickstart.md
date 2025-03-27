# Quickstart

## A simple document processing pipeline

The following example shows a simple document processing pipeline that will convert a markdown document into a PDF:

``` klartext title="processing.dm"
pipeline:

    markdown-to-xhtml::
        input: "document.md"

    xhtml-to-pdf:
        stylesheet: "htmlbook.less"
        output: "document.pdf"    
```

!!! note
    A pipeline definition file (usually ending with '.dm') is itself a `klartext` file.

## Tasks in the pipeline

The example pipeline consists of only two tasks:

`markdown-to-xhtml`
:   This task converts the ^markdown input document to an xhtml structure

`xhtml-to-pdf`
:   This task applies a less stylesheet to the xhtml structure and renders it to a PDF document

## Executing the pipeline

To execute the processing pipeline, you run the `dm` tool on the command line:

``` bash
$ dm --log=info run -p processing.dm 

2025-03-26 12:36:40,457 | I | Execute conversion pipeline "/workspaces/dossier/website/dm/examples/processing.dm"
2025-03-26 12:36:40,459 | I | markdown-to-xhtml - loading document.md
2025-03-26 12:36:40,478 | I | xhtml-to-pdf - converting "/workspaces/dossier/dossier/dm/Tools/less/htmlbook.less" to "/tmp/tmpbg_v816m.css"
2025-03-26 12:36:40,880 | I | xhtml-to-pdf - applying stylesheet "/tmp/tmpbg_v816m.css"
2025-03-26 12:36:41,246 | I | xhtml-to-pdf - saving document.pdf, encoding="None"
```

This will generate the file `document.pdf` that contains a properly formatted document with the content from the `document.md` file.