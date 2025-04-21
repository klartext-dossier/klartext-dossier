pipeline:

    // Load a file

    load: 
        input: encoding="u16" 
            501_load__i.md 
            
    save:
        output: encoding="utf-8" 
            501_load__o.test.md
