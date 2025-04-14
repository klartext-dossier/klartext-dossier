# `file` task

The `file` task allows to create an input document from within a pipeline.

!!! note
    This is very useful for testing a pipeline, as you do not need to provide an additional input file.

## Task attributes

None.

## Task elements

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| output       | [0..1]       | The name of the output file. Optional. |

Each `output` element can have the following attributes:

| Attribute name | Default value               | Description                      |
| -------------- | --------------------------- | -------------------------------- |
| encoding       | utf-8                       | The encoding of the output file. |

## Task behaviour

The text content of the `file` task (with the leading indentation removed) is used as input and passed to the next task.

If an `output` element is given, the text content will be saved to a file with the given name.

## Example

``` klartext
pipeline:

    file:
        This is some content.

        That will be passed on to the next task.
```