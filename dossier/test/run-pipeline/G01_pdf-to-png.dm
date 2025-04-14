pipeline:

    // Test generating PNG
    
    file:
        This is **test** file containing _markdown_ code.

    markdown-to-xhtml:

    xhtml-to-pdf:
        stylesheet: "htmlbook.css"

    pdf-to-png: single="true"

    save:
        output: "G01_pdf-to-png__o.test.zip"