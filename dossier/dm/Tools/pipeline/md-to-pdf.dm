// Convert markdown files to PDF

pipeline:

    markdown-to-xhtml:

    code-highlight:

    xml-transform:
        stylesheet: "glossary.xslt"
        stylesheet: "unique-ids.xslt"
        stylesheet: "table-of-contents.xslt"

    if: test="validate"
        xml-validate:
            schema: "htmlbook-ext.xsd"

    xhtml-to-pdf:
        stylesheet: "htmlbook.css"
