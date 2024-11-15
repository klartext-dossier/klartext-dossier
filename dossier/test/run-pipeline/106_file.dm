pipeline: name="Test File Task"

    // Provide two output files => TaskException
    
    file: name="Create Input File"
        output: 
            106_file__o.test.md
        output: 
            106b_file__o.test.md
        Das ist ein *Test*.