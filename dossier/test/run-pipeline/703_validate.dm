pipeline: name="Test validate Task"

    // Test validating XML against an non-existant schema file
    
    xml-validate:
        input: "703_validate__i.xml"
        schema: "not-found.xsd"
