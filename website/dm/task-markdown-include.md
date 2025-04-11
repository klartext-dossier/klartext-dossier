# `markdown-include` task

The `markdown-include` task processes a markdown include file (`.mdpp`).

## Task attributes

| Attribute name | Default value    | Description                            |
| -------------- | ---------------- | -------------------------------------- |
| name           | markdown-include | The name of the task used for logging. |

## Task elements

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| input        | [1..n]       | The file name/pattern to include.      |
| output       | [0..1]       | The name of the output file. Optional. |

Each `input` element can have the following attributes:

| Attribute name | Default value               | Description                     |
| -------------- | --------------------------- | ------------------------------- |
| encoding       | utf-8                       | The encoding of the input file. |

Each `output` element can have the following attributes:

| Attribute name | Default value               | Description                      |
| -------------- | --------------------------- | -------------------------------- |
| encoding       | utf-8                       | The encoding of the output file. |

## Task behaviour

The specified markdown include file will be process and the resulting file passed to the next task.

## Example

``` klartext
pipeline:

    markdown-include:
        input: "document.mdpp"
```

will read and process the `document.mdpp` file.
