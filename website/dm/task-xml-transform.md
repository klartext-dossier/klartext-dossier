# `xml-transform` task

The `xml-transform` task converts an xhtml file to PDF with a less/css stylesheet transformation.

## Task attributes

| Attribute name       | Default value    | Description                             |
| -------------------- | ---------------- | --------------------------------------- |
| name                 | xml-transform    | The name of the task used for logging.  |

## Task elements

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| input        | [1..n]       | The file name to include.              |
| output       | [0..1]       | The name of the output file. Optional. |
| stylesheet   | [0..n]       | A XSLT stylesheet to apply.            |

Each `input` element can have the following attributes:

| Attribute name | Default value | Description                     |
| -------------- | ------------- | ------------------------------- |
| encoding       | utf-8         | The encoding of the input file. |

Each `output` element can have the following attributes:

| Attribute name | Default value | Description                      |
| -------------- | ------------- | -------------------------------- |
| encoding       | utf-8         | The encoding of the output file. |

## Task behaviour

The xml input will be transformed into xml output by applying a number of XSLT transformations.

## Example

The pipeline

``` klartext
pipeline:

    load:
        input: "document.xhtml"

    xml-transform:
        stylesheet: "htmlbook-to-docx.xslt"
```

will apply the common transformation to prepare a HTMLBook file for word generation.
