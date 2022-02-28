pipeline: name="Test Save Task"

    // Create a simple markdown content and save it

    file: name="Create Input File"
        Das ist ein *Test*.
    
    save:
        output: "401_save__o.test.md"