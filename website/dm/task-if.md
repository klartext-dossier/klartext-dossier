# `include` task

The `include` task executes all child tasks when a condition flag is set.

## Task attributes

| Attribute name | Default value | Description                          |
| -------------- | ------------- | ------------------------------------ |
| test           | _none_        | The condition to evaluate. Required. |

## Task elements

Tasks to run conditionally.

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