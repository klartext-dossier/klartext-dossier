pipeline:

    include:
        input: "doc-use-specification.kt"
        input: "intended-use-statement.kt"
        input: "dossier.kt"
        input: "glossary.kt"

    save:
        output: "test-included.xml"

    xml-transform:
        stylesheet: "common-transformations.xslt"
        stylesheet: "kt-to-htmlbook.xslt"

    save:
        output: "test.xml"

    xml-transform:
        stylesheet: "glossary.xslt"
        stylesheet: "unique-ids.xslt"
        stylesheet: "table-of-contents.xslt"

    save:
        output: "test.xhtml"

    xhtml-to-pdf:
        stylesheet: "htmlbook.less"
        output: "doc-use-specification.pdf"
    