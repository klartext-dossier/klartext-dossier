# `xhtml-to-docx` task

The `xhtml-to-docx` task converts an xhtml file to docx.

## Task attributes

| Attribute name       | Default value    | Description                             |
| -------------------- | ---------------- | --------------------------------------- |
| name                 | xhtml-to-docx    | The name of the task used for logging.  |
| base-url             | .                | The base used to resolve relative URLs. |

## Task elements

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| input        | [1..n]       | The file name to include.              |
| output       | [0..1]       | The name of the output file. Optional. |
| template     | [0..1]       | A docx template file to use. Optional. |

Each `input` element can have the following attributes:

| Attribute name | Default value               | Description                                                           |
| -------------- | --------------------------- | --------------------------------------------------------------------- |
| encoding       | utf-8                       | The encoding of the input file.                                       |

Each `output` element can have the following attributes:

| Attribute name | Default value               | Description                      |
| -------------- | --------------------------- | -------------------------------- |
| encoding       | utf-8                       | The encoding of the output file. |

## Task behaviour

The xhtml input will be transformed into a docx file, using the template if provided.

## Example

The pipeline

``` klartext
pipeline:

    load:
        input: "document.xhtml"

    xhtml-to-docx:
        template: "template.docx"
        output: "document.docx"
```

will generate a docx file.

!!! note
    This is work in progress. The detailed mechanism needs to be documented!
