# `pngs-to-pptx` task

The `pngs-to-pptx` task converts a set of images to a pptx file.

## Task attributes

| Attribute name | Default value  | Description                            |
| -------------- | -------------- | -------------------------------------- |
| name           | pngs-to-pptx   | The name of the task used for logging. |

## Task elements

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| input        | [1..1]       | The name of the input.                 |
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

The task converts the input, a zip-file containing a set of png images, to a powerpoint pptx-file. Each image will result in a slide in the powerpoint presentation.

## Example

n/a
