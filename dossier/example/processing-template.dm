pipeline:

    include:
        input: "doc-use-specification.kt"
        input: "intended-use-statement.kt"
        input: "dossier.kt"

    xml-transform:
        stylesheet: "common-transformations.xslt"
        stylesheet: "kt-to-docbook.xslt"
        stylesheet: "glossary.xslt"
        stylesheet: "unique-ids.xslt"
        stylesheet: "table-of-contents.xslt"

    save:
        output: "test.xml"

    xhtml-to-pdf:
        stylesheet: "htmlbook.less"
        output: "doc-use-specification.pdf"
    