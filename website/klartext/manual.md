# User Manual

## Tags

Tags are the basic building blocks of the klartext markup language. A tag is annotated by its name, followed by a colon:

=== "klartext"
    ``` klartext
    article:
    ```

=== "XML"
    ``` xml
    <article/>
    ```

Tags can be nested. Nested tags are intended by four spaces, or a tab:

=== "klartext"
    ``` klartext
    article:

        section:

        section:
    ```

=== "XML"
    ``` xml
    <article>

        <section/>

        <section/>

    </article>
    ```

In this example, the tag `section` contains two nested tags named `section`.

The scope of a tag is defined by the intendation level. A tag ends when another tag is defined on the same level:

=== "klartext"
    ``` klartext
    article:

        section:

            paragraph:

            paragraph:
            
        section:
    ```

=== "XML"
    ``` xml
    <article>

        <section>

            <paragraph/>

            <paragraph/>

        </section>

        <section/>

    </article>
    ```

!!! note
    To be valid, a klartext file must have exactly one top-level tag with no indentation. In the examples here, this is the `article` tag.

## Attributes

## IDs

## Links

## Content

## Inline tags

## Glossary entries

## Namespaces
