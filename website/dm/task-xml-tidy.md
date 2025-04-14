# `xml-tidy` task

The `xml-tidy` task pretty-prints an XML-file.

## Task attributes

None.

## Task elements

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| input        | [1..n]       | The file name to include.              |
| output       | [0..1]       | The name of the output file. Optional. |
| option       | [0..n]       | Additional options. Optional.          |

Each `input` element can have the following attributes:

| Attribute name | Default value | Description                     |
| -------------- | ------------- | ------------------------------- |
| encoding       | utf-8         | The encoding of the input file. |

Each `output` element can have the following attributes:

| Attribute name | Default value | Description                      |
| -------------- | ------------- | -------------------------------- |
| encoding       | utf-8         | The encoding of the output file. |

Each `option` element can have the following attributes:

| Attribute name | Default value | Description                      |
| -------------- | ------------- | -------------------------------- |
| name           | none          | The name of the option.          |
| value          | none          | The value of the option.         |

See the [tidylib documentation](https://pythonhosted.org/pytidylib/#configuration-options) for possible options.

## Task behaviour

The xml input will be transformed to a pretty-printed XML-file.

## Example

The following input

=== "Pipeline"

    ``` klartext
    pipeline:

        load:
            input: "ugly.xml"

        xml-tidy:
            option: name="indent" value="true"
            option: name="add-xml-decl" value="true"
            output: "pretty.xml"
    ```

=== "Input"

    ``` xml
    <html xmlns="http://www.w3.org/1999/xhtml"><head><title>A document</title><link rel="stylesheet" type="text/css" href="htmlbook.css" /></head><body data-type="book"><section data-type="titlepage"><h1>A document</h1></section><section data-type="chapter"><h1>Introduction</h1><p>This is a <strong>markdown</strong> document.</p></section></body></html>
    ```

will create a pretty-printed XML file:

``` xml
<?xml version="1.0"?>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>A document</title>
    <link href="htmlbook.css" rel="stylesheet" type="text/css" />
  </head>
  <body data-type="book">
    <section data-type="titlepage">
      <h1>A document</h1>
    </section>
    <section data-type="chapter">
      <h1>Introduction</h1>
      <p>This is a 
      <strong>markdown</strong>document.</p>
    </section>
  </body>
</html>
```
