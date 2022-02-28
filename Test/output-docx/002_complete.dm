pipeline: name="Convert htmlbook to docx"

    xml-transform:
        input: "002_complete__i.html"
        stylesheet: "htmlbook-to-docx.xslt"
        output: "002_complete__o.xml"

    xhtml-to-docx:
        output: "002_complete__o.docx"
