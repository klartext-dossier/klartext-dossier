pipeline:

    include:
        input: "Dossier.kt"

    if: test="dump"
        save:
            output: "test.xml"

    xml-transform:
        stylesheet: "transform.xslt"
    
    code-highlight:
    
    if: test="dump"
        save:   
            output: "test.html"
        
    xhtml-to-pdf:
        stylesheet: "htmlbook.css"
        stylesheet: "slides.css"
        output: "Dossier.pdf"