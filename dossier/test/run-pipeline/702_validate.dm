pipeline:

    // Test validating incorrect XML against schema file => TaskException
    
    xml-validate:
        input: "702_validate__i.xml"
        schema: "702_validate__i.xsd"
