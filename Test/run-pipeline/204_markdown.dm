pipeline: name="Test Markdown Task"

    // Conversion from a u16 encoded markdown file to an xhtml file
    
    markdown-to-xhtml: 
        input: encoding="u16" "204_markdown__i.md"
        output: "204_markdown__o.test.xhtml"
