pipeline: name="Convert htmlbook to docx    "

    xml-transform:
        input: "001_example__i.html"
        stylesheet: "htmlbook-to-docx.xslt"
        output: "001_example__o.xml"

    xhtml-to-docx:
        output: "001_example__o.docx"
