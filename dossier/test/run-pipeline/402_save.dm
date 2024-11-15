pipeline: name="Test Save Task"

    // Create a simple markdown content and save it with other encoding

    file: name="Create Input File"
        Das ist ein *Test*.
    
    save:
        output: encoding="u16" 
            402_save__o.test.md