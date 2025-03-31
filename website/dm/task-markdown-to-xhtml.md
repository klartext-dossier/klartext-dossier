# `markdown-to-xhtml` task

The `markdown-to-xhtml` task Converts markdown input to an xhtml according to the HTMLBook specification.

## Task attributes

| Attribute name | Default value    | Description                            |
| -------------- | ---------------- | -------------------------------------- |
| name           | markdown-to-xhtml| The name of the task used for logging. |

## Task elements

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| input        | [1..n]       | The file name to include.              |
| output       | [0..1]       | The name of the output file. Optional. |

Each `input` element can have the following attributes:

| Attribute name | Default value               | Description                                                           |
| -------------- | --------------------------- | --------------------------------------------------------------------- |
| encoding       | utf-8                       | The encoding of the input file.                                       |

Each `output` element can have the following attributes:

| Attribute name | Default value               | Description                      |
| -------------- | --------------------------- | -------------------------------- |
| encoding       | utf-8                       | The encoding of the output file. |

## Task behaviour

The input s will be read, parsed, and converted to xhtml.

## Example
=== "Pipeline"
    ``` klartext
    pipeline:

        markdown-to-xhtml:
            input: "markdown.md"
    ```

=== "markdown.md"
    ``` markdown
    # A document

    ## Introduction

    This is a **markdown** document.    
    ```

will result in the following XML file:

``` html
<?xml version="1.0" encoding="UTF-8" ?>

<html xmlns="http://www.w3.org/1999/xhtml">

    <head>
        <title>A document</title>
        <link rel="stylesheet" type="text/css" href="htmlbook.css" />
    </head>

    <body data-type="book">
        <section data-type="titlepage">
            <h1>A document</h1>
        </section>
        <section data-type="chapter">
            <h1>Introduction</h1>
            <p>This is a <strong>markdown</strong> document.</p>
        </section>
    </body>

</html>
```
