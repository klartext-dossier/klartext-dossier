!import "http://www.klartext-dossier.org/medical-device-file" as md

dossier:

    information-model:

        md::device: #device name="Generic Dialysis System"

            md::intended-use> gds-intended-use


    document-model: name="Technical Documentation"

        document: #APP name="Application Specification"

        document: #RA name="Risk Analysis"

        file: name="Risk Management File"

            include> APP
            include> RA
