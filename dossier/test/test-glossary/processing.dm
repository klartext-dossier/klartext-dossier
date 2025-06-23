pipeline:

    include:
        input: "test-glossary.kt"

    save:
        output: "test.xml"

    xml-transform:
        stylesheet: "transform.xslt"
        stylesheet: "glossary.xslt"

    save:
        output: "test.html"

    xhtml-to-pdf:
        stylesheet: "htmlbook.less"
        stylesheet: "htmlbook-debug.css"
        output: "test-glossary.pdf"
