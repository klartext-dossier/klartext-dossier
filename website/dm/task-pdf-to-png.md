# `pdf-to-png` task

The `pdf-to-png` task converts a PDF file to a set of images.

## Task attributes

| Attribute name | Default value | Description                                       |
| -------------- | ------------- | ------------------------------------------------- |
| name           | pdf-to-png    | The name of the task used for logging.            |
| pattern        | page-%s.png   | The pattern to name the images.                   |
| dpi            | 300           | The resolution of the images.                     |
| single         | false         | Create one image per page, instead of a zip-file. |

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

The task renders the input PDF as a set of PNG images. The `pattern` determines the name of each image.

If `single` is true, one image file will be created for each page in the PDF. Otherwise, a zip-file containing all images is written.

## Example

``` klartext
pipeline:

    pdf-to-png:
        input: "document.pdf"
        output: "images.zip"
```

will create the zip-file `images.zip` containing

- page-0.png
- page-1.png

...
