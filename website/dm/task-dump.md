# `dump` task

The `dump` task allows displaying the content of a document.

## Task attributes

| Attribute name | Default value | Description                            |
| -------------- | ------------- | -------------------------------------- |
| name           | dump          | The name of the task used for logging. |

## Task elements

| Element name | Multiplicity | Description                        |
| ------------ | ------------ | ---------------------------------- |
| input        | [1..1]       | The name of the input.             |

Each `input` element can have the following attributes:

| Attribute name | Default value               | Description                     |
| -------------- | --------------------------- | ------------------------------- |
| encoding       | utf-8                       | The encoding of the input file. |

## Task behaviour

The input file will be written to the console / standard output.

## Example

``` klartext
pipeline:

    file:
        This is a sample text.

    dump:
```

will print the text `This is a sample text.` on the standard output.
