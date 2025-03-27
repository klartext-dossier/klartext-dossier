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

The following sections describe the attributes, elements and contents of each task.

## Input Tasks

### `file` task

The `file` task allows to create an input document from within a pipeline.

!!! note
    This is very useful for testing a pipeline, as you do not need to provide an additional input file.

#### Task attributes

| Attribute name | Default value | Description                            |
| -------------- | ------------- | -------------------------------------- |
| name           | file          | The name of the task used for logging. |

#### Task elements

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| output       | [0..1]       | The name of the output file. Optional. |

#### Task behaviour

The text content of the `file` task (with the leading indentation removed) is used as input and passed to the next task.

If an `output` element is given, the text content will be saved to a file with the given name.

#### Example

``` klartext
pipeline:

    file:
        This is some content.

        That will be passed on to the next task.
```

### `include` task

The `include` task allows to combine several input files into an interal XML structure.

#### Task attributes

| Attribute name | Default value | Description                            |
| -------------- | ------------- | -------------------------------------- |
| name           | include       | The name of the task used for logging. |
| root           | root          | The root tag of the XML structure.     |

#### Task elements

| Element name | Multiplicity | Description                        |
| ------------ | ------------ | ---------------------------------- |
| input        | [1..n]       | The root tag of the XML structure. |

#### Task behaviour

The text content of the `file` task (with the leading indentation removed) is used as input and passed to the next task.

#### Example

``` klartext
pipeline:

    file:
        This is some content.

        That will be passed on to the next task.
```

### `load` task

### `markdown-include` task

## Conversion Tasks

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

### `xml-validate` task
