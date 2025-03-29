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

The following tables provides an oveview over the tasks that are available to build processing pipelines:

| Task name                                      | Description                                      |
| ---------------------------------------------- | ------------------------------------------------ |
| [`file`](task-file.md)                         | creates an input document from within a pipeline |
| [`include`](task-include.md)                   | combines several input files                     |
| [`load`](task-load.md)                         | loads a single input file                        |
| [`markdown-include`](task-markdown-include.md) | processes a markdown include file                |

<!-- ## Conversion Tasks

### `code-highlight` task

### `copy` task

### `diagram-to-svg` task

### `embed-svg` task

### `klartext-to-xml` task

### `markdown-to-xhtml` task

### `pdf-to-png` task

### `pngs-to-pptx` task

### `xhtml-to-docx` task

### `xhtml-to-pdf` task

### `xml-transform` task

## Output Tasks

### `save` task

## Other Tasks

### `dump` task

### `if` task

### `sequence` task

### `xml-tidy` task

### `xml-validate` task -->
