pipeline: name="Test validate Task"

    // Test validating correct XML against schema file
    
    xml-validate:
        input: "701_validate__i.xml"
        schema: "701_validate__i.xsd"
