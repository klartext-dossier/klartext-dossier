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

Each `output` element can have the following attributes:

| Attribute name | Default value               | Description                      |
| -------------- | --------------------------- | -------------------------------- |
| encoding       | utf-8                       | The encoding of the output file. |

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

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| input        | [1..n]       | The file name/pattern to include.      |
| output       | [0..1]       | The name of the output file. Optional. |

Note that you can use Unix-style file name globbing to include several files with one pattern.

Each `input` element can have the following attributes:

| Attribute name | Default value               | Description                                                           |
| -------------- | --------------------------- | --------------------------------------------------------------------- |
| tag            | content                     | The name of the tag under which included markdow content will be put. |
| format         | _extension of the filename_ | The format of the include file. One of ['kt', 'md'].                  |
| encoding       | utf-8                       | The encoding of the input file.                                       |

Each `output` element can have the following attributes:

| Attribute name | Default value               | Description                      |
| -------------- | --------------------------- | -------------------------------- |
| encoding       | utf-8                       | The encoding of the output file. |

#### Task behaviour

The specified include files will be read, parsed, and combined to one XML structure.

#### Example

``` klartext
pipeline:

    include: root="top"
        input: tag="sub" "document.md"
        input: "**/*.kt"
```

will result in an XML structure like

``` xml
<top>
    <sub>
        <!-- content of docment.md, converted into xhtml -->
    </sub>
    <!-- content of the matching .kt files, converted into xhtml -->
</top>
```

### `load` task

The `load` task will load a single input file.

#### Task attributes

| Attribute name | Default value | Description                            |
| -------------- | ------------- | -------------------------------------- |
| name           | include       | The name of the task used for logging. |

#### Task elements

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| input        | [1..n]       | The file name/pattern to include.      |

Each `input` element can have the following attributes:

| Attribute name | Default value               | Description                     |
| -------------- | --------------------------- | ------------------------------- |
| encoding       | utf-8                       | The encoding of the input file. |

#### Task behaviour

The specified file will be read in and passed on to the next task.

#### Example

``` klartext
pipeline:

    load:
        input: "filename.ext"
```

This will load the `filename.ext` without any kind of processing.

### `markdown-include` task

The `markdown-include` task processes a markdown include file (`.mdpp`).

#### Task attributes

| Attribute name | Default value | Description                            |
| -------------- | ------------- | -------------------------------------- |
| name           | include       | The name of the task used for logging. |

#### Task elements

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| input        | [1..n]       | The file name/pattern to include.      |
| output       | [0..1]       | The name of the output file. Optional. |

Each `input` element can have the following attributes:

| Attribute name | Default value               | Description                     |
| -------------- | --------------------------- | ------------------------------- |
| encoding       | utf-8                       | The encoding of the input file. |

Each `output` element can have the following attributes:

| Attribute name | Default value               | Description                      |
| -------------- | --------------------------- | -------------------------------- |
| encoding       | utf-8                       | The encoding of the output file. |

#### Task behaviour

The specified markdown include file will be process and the resulting file passed to the next task.

#### Example

``` klartext
pipeline:

    markdown-include:
        input: "document.mdpp"
```

will read and process the `document.mdpp` file.

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
