pipeline:

    include:
        input: "test-glossary.kt"

    save:
        output: "test.xml"

    xml-transform:
        stylesheet: "transform.xslt"
        // stylesheet: "unique-ids.xslt"
        // stylesheet: "table-of-contents.xslt"

    save:
        output: "test.html"

    xhtml-to-pdf:
        stylesheet: "htmlbook.css"
        stylesheet: "htmlbook-debug.css"
        output: "test-glossary.pdf"
