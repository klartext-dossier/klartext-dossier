// Convert markdown-pp files to HTMLBook

pipeline:

    markdown-include:
    
    markdown-to-xhtml:

    code-highlight:

    xml-transform:
        stylesheet: "glossary.xslt"
        stylesheet: "unique-ids.xslt"
        stylesheet: "table-of-contents.xslt"

    if: test="validate"
        xml-validate:
            schema: "htmlbook.xsd"
