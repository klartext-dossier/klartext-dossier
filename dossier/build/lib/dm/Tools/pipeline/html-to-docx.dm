// Convert HTMLBook files to DOCX

pipeline:

    if: test="validate"
        xml-validate:
            schema: "htmlbook-ext.xsd"

    xml-transform:
        stylesheet: "htmlbook-to-docx.xslt"

    xhtml-to-docx: