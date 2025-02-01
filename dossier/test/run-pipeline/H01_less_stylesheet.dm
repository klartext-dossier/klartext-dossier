pipeline: name="Test less Stylesheet"

    // Test generating PNG
    
    file:
        This is **test** file containing _markdown_ code.

    markdown-to-xhtml:

    xhtml-to-pdf:
        stylesheet: font-size="25pt" "htmlbook.less"

    save:
        output: "H01_less_stylesheet__o.test.pdf"