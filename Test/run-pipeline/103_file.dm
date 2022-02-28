pipeline: name="Test File Task"

    // Create content with unicode characters and save it to a UTF-16 encoded file
    
    file: name="Create Input File" 
        This is a file using unicode: ♥ ♠ ♣ ♦

    save:
        output: encoding="u16" "103_file__o.test.md"