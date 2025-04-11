# `include` task

The `include` task executes all child tasks when a condition flag is set.

## Task attributes

| Attribute name | Default value | Description                            |
| -------------- | ------------- | -------------------------------------- |
| name           | if            | The name of the task used for logging. |
| root           | test          | The condition to evaluate.             |

## Task elements

None.

## Task behaviour

The child tasks will be executed when the test condition is true.

## Example

``` klartext
pipeline:

    [ ... ]

    if: test="debug"
        dump:
```

will dump the current document when the `debug` flag is set, e.g., when executing the pipeline like this:

``` bash
dm run --set debug -p pipeline.dm
```