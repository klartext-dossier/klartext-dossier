pipeline:

    markdown-to-xhtml::
        input: "document.md"

    xhtml-to-pdf:
        stylesheet: "htmlbook.less"
        output: "document.pdf"  