# `include` task

The `include` task allows to combine several input files into an interal XML structure.

## Task attributes

| Attribute name | Default value | Description                            |
| -------------- | ------------- | -------------------------------------- |
| root           | root          | The root tag of the XML structure.     |

## Task elements

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| input        | [1..n]       | The file name/pattern to include.      |
| output       | [0..1]       | The name of the output file. Optional. |

Note that you can use Unix-style file name globbing to include several files with one pattern.

Each `input` element can have the following attributes:

| Attribute name | Default value               | Description                                                           |
| -------------- | --------------------------- | --------------------------------------------------------------------- |
| tag            | content                     | The name of the tag under which included markdow content will be put. |
| format         | _extension of the filename_ | The format of the include file. One of ['kt', 'md'].                  |
| encoding       | utf-8                       | The encoding of the input file.                                       |

Each `output` element can have the following attributes:

| Attribute name | Default value               | Description                      |
| -------------- | --------------------------- | -------------------------------- |
| encoding       | utf-8                       | The encoding of the output file. |

## Task behaviour

The specified include files will be read, parsed, and combined to one XML structure.

## Example

``` klartext
pipeline:

    include: root="top"
        input: tag="sub" "document.md"
        input: "**/*.kt"
```

will result in an XML structure like

``` xml
<top>
    <sub>
        <!-- content of docment.md, converted into xhtml -->
    </sub>
    <!-- content of the matching .kt files, converted into xhtml -->
</top>
```
