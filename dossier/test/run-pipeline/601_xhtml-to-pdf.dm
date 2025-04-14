pipeline:

    // Test generating PDF
    
    file:
        This is a *test*.

    markdown-to-xhtml:

    xhtml-to-pdf:
        stylesheet: "htmlbook.css"

    save:
        output: "601_xhtml-to-pdf__o.test.pdf"