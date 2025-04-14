# `xml-validate` task

The `xml-validate` task validates an XML-file.

## Task attributes

None.

## Task elements

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| input        | [1..n]       | The file name to include.              |
| schema       | [1..n]       | The schema to validate against.        |

Each `input` element can have the following attributes:

| Attribute name | Default value | Description                     |
| -------------- | ------------- | ------------------------------- |
| encoding       | utf-8         | The encoding of the input file. |

## Task behaviour

The xml input will be validated against the given XSD schema files.

## Example

The following pipeline

``` klartext
pipeline:

    file:
        This is __markup__.

    markdown-to-xhtml:

    xml-validate:
        schema: "htmlbook.xsd"
```

will run successfully, as the generated xhtml file is valid HTMLBook.
