pipeline: name="Test File Task"

    // Provide incorrect child attribute => TaskException
    
    file: name="Create Input File"
        output: foobar="something"
            108_file__o.test.md
        Das ist ein *Test*.