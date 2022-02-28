// Convert HTMLBook files to PDF

pipeline:

    if: test="validate"
        xml-validate:
            schema: "htmlbook-ext.xsd"

    code-highlight:

    xml-transform:
        stylesheet: "unique-ids.xslt"
        stylesheet: "table-of-contents.xslt"

    if: test="validate"
        xml-validate:
            schema: "htmlbook-ext.xsd"

    xhtml-to-pdf:
        stylesheet: "htmlbook.css"