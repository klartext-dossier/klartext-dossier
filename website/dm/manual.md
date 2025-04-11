# User Manual

This `dm` user manual explains the use of the tool and how to configure a processing pipeline.

## Command Line Parameters

## Pipeline Definition

## Structure of a Task

Each task can have a number of parts: a tag, a list of attributes, a number of (child-)elements and a text content:

``` klartext title="Structure of a task definition"
tagname: attribute1="v1" attribute2="v2" 
    element1: attribute="v3" "value"

    Text content.
```

## Tasks

The following table provides an overview over the tasks that are available to build processing pipelines:

| Task/Tag name                                    | Description                                                    |
| ------------------------------------------------ | -------------------------------------------------------------- |
| [`code-highlight`](task-code-highlight.md)       | adds syntax highlighting to `<code>` tags                      |
| [`copy`](task-copy.md)                           | copies the content of a file                                   |
| [`diagram-to-svg`](task-diagram-to-svg.md)       | transforms a diagram to an SVG element                         |
| [`dump`](task-dump.md)                           | displays the output on the console                             |
| [`embed-svg`](task-embed-svg.md)                 | transforms an element to an embedded PNG image                 |
| [`file`](task-file.md)                           | creates an input document from within a pipeline               |
| [`if`](task-if.md)                               | conditionally executes tasks                                   |
| [`include`](task-include.md)                     | combines several input files                                   |
| [`klartext-to-xml`](task-klartext-to-xml.md)     | converts klartext to XML                                       |
| [`load`](task-load.md)                           | loads a single input file                                      |
| [`markdown-include`](task-markdown-include.md)   | processes a markdown include file                              |
| [`markdown-to-xhtml`](task-markdown-to-xhtml.md) | converts markdown to xhtml                                     |
| [`pdf-to-png`](task-pdf-to-png.md)               | converts a PDF file to a set of images                         |
| [`pngs-to-pptx`](task-pngs-to-pptx.md)           | converts a set of images to a pptx file                        |
| [`save`](task-save.md)                           | saves the output to a file                                     |
| [`sequence`](task-sequence.md)                   | executes child tasks                                           |
| [`xhtml-to-docx`](task-xhtml-to-docx.md)         | converts an xhtml file to docx                                 |
| [`xhtml-to-pdf`](task-xhtml-to-pdf.md)           | converts an xhtml file to PDF with a stylesheet transformation |
| [`xml-tidy`](task-xml-tidy.md)                   | pretty-prints an XML-file                                      |
| [`xml-transform`](task-xml-transform.md)         | transforms an XML document with an XSLT transformation         |
| [`xml-validate`](task-xml-validate.md)           | validates an XML-file                                          |
