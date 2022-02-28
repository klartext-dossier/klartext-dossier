pipeline: name="Test XHTML-to-PDF Task"

    // Test converting an incorrect XHTML file to PDF => no exception, as parser is tolerant...
    
    xhtml-to-pdf:
        input: "603_xhtml-to-pdf__i.xhtml"
        output: "603_xhtml-to-pdf__o.test.pdf"
        