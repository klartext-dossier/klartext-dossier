pipeline: name="Test xml-transform Task"

    // Transform XML using stylesheets

    markdown-to-xhtml:
        This is a test!
        
    xml-transform:
        stylesheet: "glossary.xslt"
        stylesheet: "unique-ids.xslt"
        stylesheet: "table-of-contents.xslt"
