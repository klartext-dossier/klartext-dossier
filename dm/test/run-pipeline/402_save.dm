pipeline:

    // Create a simple markdown content and save it with other encoding

    file:
        Das ist ein *Test*.
    
    save:
        output: encoding="u16" 
            402_save__o.test.md