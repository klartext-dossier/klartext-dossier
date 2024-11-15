pipeline: name="Test XHTML-to-PDF Task"

    // Test generating PDF with a non-existent stylesheet => TaskException
    
    file:
        This is a *test*.

    markdown-to-xhtml:

    xhtml-to-pdf:
        stylesheet: "not-found.css"

