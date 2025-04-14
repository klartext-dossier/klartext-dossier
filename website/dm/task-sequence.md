# `sequence` task

The `sequence` task executes all child tasks in sequence.

## Task attributes

None.

## Task elements

None.

## Task behaviour

The child tasks will be executed in sequence.

!!! note
    This is the normal behaviour of a `pipeline`, so this task is rarely used. This might change in the future, when parallel task execution might become possible.

## Example

``` klartext
pipeline:

    sequence:
        dump:
            input: "document.txt"
```

will simply run the `dump` task.

!!! note
    This task is also used run the top-level `pipeline`.