!import "https://klartext-dossier.org/sample/glossary_a" as glsa
!import "https://klartext-dossier.org/sample/glossary_b" as glsb

document:

    glossary: title="Recursive"

        entry:
            term: "Rec-A"

            definition:
                Uses {Rec-B}.
                
        entry:
            term: "Rec-B"

            definition:
                Uses {Rec-A}.
                
        entry:
            term: "Rec-1"

            definition:
                Uses {Rec-2}.
                
        entry:
            term: "Rec-2"

            definition:
                Uses {Rec-3}.
                
        entry:
            term: "Rec-3"

            definition:
                Uses {Rec-1}.
                
    glossary: #glsa title="Glossary A"

        entry:
            term: "Sample Term"
            term: "Sample Terms"

            definition:
                Sample definition A, uses {glsb::Indirect Term}

        entry:
            term: "Really Unused Term"

            definition:
                Sample definition

        entry:
            term: "Actually Unused Term"

            definition:
                Sample definition, uses {glsa::Actually Unused Term}


    glossary: #glsb title="Glossary B"

        entry:
            term: "Sample Term"

            definition:
                Sample definition B

        entry:
            term: "Indirect Term"

            definition:
                Sample definition

        entry:
            term: "Unspecified Term"

            definition:
                Sample definition

    glossary: title="Glossary C"

        entry:
            term: "Sample Term"

            definition:
                Sample definition C

        entry:
            term: "Recursive Term 1"
            
            definition:
                Uses {recursive term 2}

        entry:
            term: "Recursive Term 2"
            
            definition:
                Uses {recursive term 1}

        entry:
            term: "Term-With-Hyphen"
            
            definition:
                Has hyphens.
                
    content:
        This is 
        
        - a {glsa::sample terms}
        - b {glsb::sample term}
        - c {sample term}
        - d {unspecified term}
        - e {recursive term 1}
        - f {foobar}
        - g {term-with-hyphen}
        // - h {Rec-B}