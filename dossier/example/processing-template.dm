pipeline:

    include:
        input: "doc-use-specification.kt"
        input: "intended-use-statement.kt"
        input: "dossier.kt"
        input: "glossary.kt"

    if: test="debug"
        save:
            output: "test-included.xml"

    xml-transform:
        stylesheet: "common-transformations.xslt"
        stylesheet: "klartext-templates.xslt"

    if: test="debug"
        save:
            output: "test.xml"

    xml-transform:
        stylesheet: "kt-to-htmlbook.xslt"
        stylesheet: "glossary.xslt"
        stylesheet: "unique-ids.xslt"
        stylesheet: "table-of-contents.xslt"

    if: test="debug"
        save:
            output: "test.xhtml"

    xhtml-to-pdf:
        stylesheet: "htmlbook.less"
        stylesheet: test="debug" "htmlbook-debug.css"
        output: "doc-use-specification.pdf"
    