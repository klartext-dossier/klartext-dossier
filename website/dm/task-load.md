# `load` task

The `load` task will load a single input file.

## Task attributes

None.

## Task elements

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| input        | [1..n]       | The file name/pattern to include.      |

Each `input` element can have the following attributes:

| Attribute name | Default value               | Description                     |
| -------------- | --------------------------- | ------------------------------- |
| encoding       | utf-8                       | The encoding of the input file. |

## Task behaviour

The specified file will be read in and passed on to the next task.

## Example

``` klartext
pipeline:

    load:
        input: "filename.ext"
```

This will load the `filename.ext` without any kind of processing.
