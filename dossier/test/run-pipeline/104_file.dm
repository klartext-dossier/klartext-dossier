pipeline: name="Test File Task"

    // Create markdown content and directly save it to a file
    
    file: name="Create Input File"
        output: 
            104_file__o.test.md
        Das ist ein *Test*.