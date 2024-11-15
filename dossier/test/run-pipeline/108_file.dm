pipeline: name="Test File Task"

    // Provide incorrect child element => TaskException
    
    file: name="Create Input File"
        output-file: 
            108_file__o.test.md
        Das ist ein *Test*.