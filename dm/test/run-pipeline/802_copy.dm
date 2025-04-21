pipeline:

    // Copy a file to another, changing the encoding

    copy:
        input: "802_copy__i.md"
        output: encoding="u16" "802_copy__o.test.md"

    save:
        output: "802b_copy__o.test.md"