# User Manual

This klartext user manual explains the concepts making up the klartext markup language. The examples are always show in the form of the klartext input, and in the XML content that is created by parsing the klartext file.

## Tags

Tags are the basic building blocks of the klartext markup language. A tag is annotated by its name, followed by a colon:

=== "klartext input"
    ``` klartext
    article:
    ```

=== "XML output"
    ``` xml
    <article/>
    ```

Tags can be nested. Nested tags are intended by four spaces, or a tab:

=== "klartext input"
    ``` klartext
    article:

        section:

        section:
    ```

=== "XML output"
    ``` xml
    <article>

        <section/>

        <section/>

    </article>
    ```

In this example, the tag `section` contains two nested tags named `section`.

The scope of a tag is defined by the intendation level. A tag ends when another tag is defined on the same level:

=== "klartext input"
    ``` klartext
    article:

        section:

            paragraph:

            paragraph:
            
        section:
    ```

=== "XML output"
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

Tags can have attributes. Attributes are defined by their name and content:

=== "klartext input"
    ``` klartext
    article: title="About Klartext" language="en"
    ```

=== "XML output"
    ``` xml
    <article title="About Klartext" language="en"/>
    ```

## IDs

A very common attribute for a tag is an ID. There are two ways to add an ID. The first uses a normal attribute:

=== "klartext input"
    ``` klartext
    article: id="ARTICLE1"
    ```

=== "XML output"
    ``` xml
    <article id="ARTICLE1"/>
    ```

The second way uses a slightly abbreviated syntax:

=== "klartext input"
    ``` klartext
    article: #ARTICLE1
    ```

=== "XML output"
    ``` xml
    <article id="ARTICLE1"/>
    ```

## Links

The most common use for IDs is to provide an anchor for linking to a tag. Links can be defined in this way:

=== "klartext input"
    ``` klartext
    article: #ARTICLE1

        reference> ARTICLE1
    ```

=== "XML output"
    ``` xml
    <article id="ARTICLE1">
        <reference ref="ARTICLE1"></reference>
    </article>
    ```

Link is a tag that is not followed by a colon, but by a &gt; symbol. It is followed immediately by the ID of the tag to link to.

In addition to the ID, links can have any number of attributes:

=== "klartext input"
    ``` klartext
    article: #ARTICLE1

        reference> ARTICLE1 page="25"
    ```

=== "XML output"
    ``` xml
    <article id="ARTICLE1">
        <reference ref="ARTICLE1" page="25"></reference>
    </article>
    ```

## Content

Tags can have content. The content is expressed in the form of Markdown:

=== "klartext input"
    ``` klartext
    article:

        This is the _content_ of the **article**.

        This is the second paragraph.
    ```

=== "XML output"
    ``` xml
    <article>
        <p xmlns="http://www.w3.org/1999/xhtml">This is the <em>content</em> of the <strong>article</strong>.</p>
        <p xmlns="http://www.w3.org/1999/xhtml">This is the second paragraph.</p>
    </article>
    ```

Usually, content is in separate, indented paragraphs below the tag. In simple cases, you can define a single paragraph of content immediately behind the tag:

=== "klartext input"
    ``` klartext
    article: This is the _content_ of the **article**.
    ```

=== "XML output"
    ``` xml
    <article>
        <p xmlns="http://www.w3.org/1999/xhtml">This is the <em>content</em> of the <strong>article</strong>.</p>
    </article>
    ```

You can suppress the markdown conversion by using quotes:

=== "klartext input"
    ``` klartext
    article: "This is the _content_ of the **article**."
    ```

=== "XML output"
    ``` xml
    <article>This is the _content_ of the **article**.</article>
    ```



## Inline tags

## Glossary entries

## Namespaces
