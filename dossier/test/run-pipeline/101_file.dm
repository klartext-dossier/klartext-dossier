pipeline: name="Test File Task"

    // Create a simple markdown content and pass it on to the next task.

    file: name="Create Input File"
        Das ist ein *Test*.
    
    save:
        output: "101_file__o.test.md"