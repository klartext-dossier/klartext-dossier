pipeline:

    load:
        input: "ugly.xml"

    xml-tidy:
        option: name="indent" value="true"
        option: name="add-xml-decl" value="true"
        output: "pretty.xml"