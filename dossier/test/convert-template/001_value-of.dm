pipeline:

    include:
        input: "001_value-of.kt"

    xml-transform:
        stylesheet: "kt-to-htmlbook.xslt"

    save:
        output: "001_value-of.test.xml"