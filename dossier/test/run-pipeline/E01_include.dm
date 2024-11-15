pipeline: name="Test klartext-include Task"

    // Include multiple klartext files

    include:
        input: "E01_include_1__i.kt"
        input: "E01_include_2__i.kt"
        output: "E01_include__o.test.xml"