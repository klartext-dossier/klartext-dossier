# `klartext-to-xml` task

The `klartext-to-xml` task converts klartext input to XML.

## Task attributes

| Attribute name | Default value   | Description                            |
| -------------- | --------------- | -------------------------------------- |
| name           | klartext-to-xml | The name of the task used for logging. |

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

The input s will be read, parsed, and converted to an XML structure.

## Example
=== "Pipeline"
    ``` klartext
    pipeline:

        klartext-to-xml:
            input: "klartext.kt"
    ```

=== "klartext.kt"
    ``` html
    article: title="About Klartext"

        author: "F. Bar"

        `klartext` is a modern {markup language}.    
    ```

will result in the following XML file:

``` xml
<article title="About Klartext">
    <author>F. Bar</author>
    <p xmlns="http://www.w3.org/1999/xhtml">
        <code>klartext</code> is a modern <a data-type="xref" data-xrefstyle="glossary" href="#markup_language">markup language</a>.
    </p>
</article>
```
