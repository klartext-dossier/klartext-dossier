!import "http://www.klartext-dossier.org/medical-device-file" as md

dossier:

    information-model: #MD

        md::device: #DEVICE name="Generic Dialysis System"

            md::intended-use: 
                The /r/DEVICE/ is a dialysis machine for chronic haemodialysis treatments.


    document-model: name="Technical Documentation"

        document: #RA name="Risk Analysis"

        file: name="Risk Management File"

            include> RA
