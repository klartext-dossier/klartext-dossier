# `save` task

The `save` task allows saving the output document to a file.

## Task attributes

None.

## Task elements

| Element name | Multiplicity | Description                        |
| ------------ | ------------ | ---------------------------------- |
| output       | [1..1]       | The name of the output file. onal. |

Each `output` element can have the following attributes:

| Attribute name | Default value               | Description                      |
| -------------- | --------------------------- | -------------------------------- |
| encoding       | utf-8                       | The encoding of the output file. |

## Task behaviour

The output document will be saved to a file.

## Example

``` klartext
pipeline:

    file:
        This is a sample text.

    save:
        output: encoding="utf16le" "output.txt"
```

will save the output to a file `output.txt` using the UTF-16LE enconding.
