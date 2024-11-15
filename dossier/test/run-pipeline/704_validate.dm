pipeline: name="Test validate Task"

    // Test validating XML against an incorrect schema file
    
    xml-validate:
        input: "704_validate__i.xml"
        schema: "704_validate__i.xsd"
