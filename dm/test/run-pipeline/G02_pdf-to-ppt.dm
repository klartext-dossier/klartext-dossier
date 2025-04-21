pipeline:

    // Test generating PPT

    pdf-to-png: dpi="96"
        input: "G02_pdf-to-ppt__i.pdf"

    pngs-to-pptx:

    save:
        output: "G02_pdf-to-ppt__o.pptx"