# `xhtml-to-pdf` task

The `xhtml-to-pdf` task converts an xhtml file to PDF with a less/css stylesheet transformation.

## Task attributes

| Attribute name       | Default value    | Description                             |
| -------------------- | ---------------- | --------------------------------------- |
| presentational-hints | true             | Follow HTML presentational hints.       |
| base-url             | .                | The base used to resolve relative URLs. |

## Task elements

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| input        | [1..n]       | The file name to include.              |
| output       | [0..1]       | The name of the output file. Optional. |
| stylesheet   | [0..n]       | A less/css stylesheet to apply.        |

Each `input` element can have the following attributes:

| Attribute name | Default value               | Description                                                           |
| -------------- | --------------------------- | --------------------------------------------------------------------- |
| encoding       | utf-8                       | The encoding of the input file.                                       |

Each `output` element can have the following attributes:

| Attribute name | Default value               | Description                      |
| -------------- | --------------------------- | -------------------------------- |
| encoding       | utf-8                       | The encoding of the output file. |

Each `stylesheet` element can have the following attributes:

| Attribute name | Default value | Description                                                |
| -------------- | ------------- | ---------------------------------------------------------- |
| test           | n/a           | Expression that decides whether the stylesheet is applied. |

When a `stylesheet` element refers to a `less` stylesheet, than the `stylesheet` element can have any number of additional attributes. These attributes will be passed to the `less` compiler as variables.

## Task behaviour

The xhtml input will be transformed into a PDF by applying the stylesheets.

## Example

The pipeline

``` klartext
pipeline:

    load:
        input: "document.xhtml"

    xhtml-to-pdf: presentational-hints="false"
        stylesheet: font-size="12pt" "htmlbook.less"
        stylesheet: test="debug" "htmlbook-debug.css"
        stylesheet: "additional.css"
        output: "document.pdf"
```

will generate a PDF by applying three consecutive stylesheets:

1. the common htmlbook stylesheet, with a base font size of 12pt
2. if the `debug` flag is passed on the command line, the `htmlbook-debug` stylesheet is appoied (which will mark certain errors in red)
3. finally, an additional local stylesheet is applied
