# `diagram-to-svg` task

The `diagram-to-svg` task transforms a diagram to an SVG element.

## Task attributes

| Attribute name | Default value  | Description                            |
| -------------- | -------------- | -------------------------------------- |
| name           | diagram-to-svg | The name of the task used for logging. |

## Task elements

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| input        | [1..1]       | The name of the input.                 |
| output       | [0..1]       | The name of the output file. Optional. |
| stylesheet   | [0..n]       | Additional stylesheets.                |

Each `input` element can have the following attributes:

| Attribute name | Default value               | Description                     |
| -------------- | --------------------------- | ------------------------------- |
| encoding       | utf-8                       | The encoding of the input file. |

Each `output` element can have the following attributes:

| Attribute name | Default value               | Description                      |
| -------------- | --------------------------- | -------------------------------- |
| encoding       | utf-8                       | The encoding of the output file. |

## Task behaviour

The task replaces diagrams in the `http://www.hoelzer-kluepfel.de/diagram` namespace with a SVG rendering.

!!! note "WIP"
    This is work in progress:

    - the namespace needs to be changed to klartext-dossier.org
    - the diagram language needs to be documented
    - diagramming functions need to be added
    - etc.

## Example

n/a
