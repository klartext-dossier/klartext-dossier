pipeline:

    xml-transform:
        input: "test.html"
        stylesheet: "htmlbook-to-docx.xslt"
        output: "test.xml"

    xhtml-to-docx:
        output: "test.docx"
