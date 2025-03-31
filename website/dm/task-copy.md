# `copy` task

The `copy` task allows copying the content of a file, potentially performing an encoding conversion.

## Task attributes

| Attribute name | Default value | Description                            |
| -------------- | ------------- | -------------------------------------- |
| name           | copy          | The name of the task used for logging. |

## Task elements

| Element name | Multiplicity | Description                        |
| ------------ | ------------ | ---------------------------------- |
| input        | [1..1]       | The name of the input.             |
| output       | [1..1]       | The name of the output file. onal. |

Each `input` element can have the following attributes:

| Attribute name | Default value               | Description                     |
| -------------- | --------------------------- | ------------------------------- |
| encoding       | utf-8                       | The encoding of the input file. |

Each `output` element can have the following attributes:

| Attribute name | Default value               | Description                      |
| -------------- | --------------------------- | -------------------------------- |
| encoding       | utf-8                       | The encoding of the output file. |

## Task behaviour

The input file will be written to the output file.

## Example

``` klartext
pipeline:

    copy:
        input: encoding="utf8" "document.md"
        output: encoding="utf16le" "copy.md
```

will copy the file `document.md` to the file `copy.md` while converting the file format from UTF-8 to UTF-16 LE.
