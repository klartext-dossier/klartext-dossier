pipeline:

    // Create content with unicode characters and save it to a UTF-16 encoded file
    
    file:
        This is a file using unicode: ♥ ♠ ♣ ♦

    save:
        output: encoding="u16" "103_file__o.test.md"