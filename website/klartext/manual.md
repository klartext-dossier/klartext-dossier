# User Manual

This `klartext` user manual explains the concepts making up the `klartext` markup language. The examples are always show in the form of the `klartext` input, and in the XML content that is created by parsing the `klartext` file.

## Tags

Tags are the basic building blocks of the `klartext` markup language. A tag is annotated by its name, followed by a colon:

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
    To be valid, a `klartext` file must have exactly one top-level tag with no indentation. In the examples here, this is the `article` tag.

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
        <p>This is the <em>content</em> of the <strong>article</strong>.</p>
        <p>This is the second paragraph.</p>
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
        <p>This is the <em>content</em> of the <strong>article</strong>.</p>
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

Within the Markdown content, inline tags can be added with an abbreviated syntax:

=== "klartext input"
    ``` klartext
    article: This is an /q/inline tag/.
    ```

=== "XML output"
    ``` xml
    <article>
        <p>This is an <q>inline tag</q>.</p>
    </article>
    ```

## Glossary entries

There is a special shortcut syntax for terms defined in a glossary:

=== "klartext input"
    ``` klartext
    article: This is a {glossary} entry.
    ```

=== "XML output"
    ``` xml
    <article>
        <p>This is a <a data-type="xref" data-xrefstyle="glossary" href="#glossary">glossary</a> entry.</p>
    </article>
    ```

## Namespaces

It is possible to define namespaces for tags used in `klartext`:

=== "klartext input"
    ``` klartext
    !import "http://www.klartext-dossier.org/example" as ex

    ex::tag:

        ex::subtag:

        subtag: This is the content.
    ```

=== "XML output"
    ``` xml
    <ex:tag xmlns:ex="http://www.klartext-dossier.org/example">
        <ex:subtag xmlns:ex="http://www.klartext-dossier.org/example"></ex:subtag>
        <subtag>
            <p>This is the content.</p>
        </subtag>
    </ex:tag>
    ```

Namespaces can also be used to make sure that IDs are unique within a scope:

=== "klartext input"
    ``` klartext
    !import "http://www.klartext-dossier.org/example" as ex
    !import "http://www.klartext-dossier.org/foobar" as foo

    tag: #ex

        subtag: #ex::subid

        another: #foo::subid
    ```

=== "XML output"
    ``` xml
    <tag id="5ca887e102362bf87d99968ef3410b06">
        <subtag id="5ca887e102362bf87d99968ef3410b06__subid">
        </subtag>
        <another id="443d4219c8274b65b61ba7347889ade8__subid">
        </another>
    </tag>
    ```


## Includes

`klartext` files allow to include other `klartext` files:

=== "klartext input"
    ``` klartext
    !include "file_to_include.kt"
    ```

=== "XML output"
    ``` xml
    <article>
        <p>This is the content of the included file.</p>
    </article>
    ```
