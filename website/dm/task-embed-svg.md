# `embed-svg` task

The `embed-svg` task an element to an embedded PNG image.

## Task attributes

| Attribute name | Default value | Description                            |
| -------------- | ------------- | -------------------------------------- |
| name           | copy          | The name of the task used for logging. |

## Task elements

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| input        | [1..1]       | The name of the input.                 |

Each `input` element can have the following attributes:

| Attribute name | Default value               | Description                     |
| -------------- | --------------------------- | ------------------------------- |
| encoding       | utf-8                       | The encoding of the input file. |

## Task behaviour

The task replaces SVG elements with embedded SVGs.

## Example

=== "Pipeline"
    ``` klartext
    pipeline:

        load: 
            input: "svg.html"

        embed-svg:
    ```

=== "svg.html"
    ``` html
    <html>
        <body>

            <svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
                <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
            </svg>

        </body>
    </html>
    ```

will be converted to

``` html
<html>
    <body>

        <img alt="image" src="/tmp/tmpnuv0xcr1.png" />

    </body>
</html>
```

!!! note "WIP"
    This is work in progress. In the future, the PNG will be embedded in the html file.
