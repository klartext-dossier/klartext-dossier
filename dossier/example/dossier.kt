!import "http://www.klartext-dossier.org/medical-device-file" as md

dossier:

    information-model: #MD

        md::device: #DEVICE name="Generic Dialysis System"

            !include "intended-use-statement.kt"


    document-model: name="Technical Documentation"

        document: #APP name="Application Specification"

        document: #RA name="Risk Analysis"

        file: name="Risk Management File"

            include> APP
            include> RA
