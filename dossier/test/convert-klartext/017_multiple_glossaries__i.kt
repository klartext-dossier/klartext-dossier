!import "https://klartext-dossier.org/glossaries/medical-device-regulation" as mdr
!import "https://klartext-dossier.org/glossaries/iso-13485" as qm

root:

    glossary: #mdr

        entry:
            term: "Medical Device"

            definition:
                A device with a medical purpose.

    tag: #mdr:foobar
        This is a {mdr:medical device} according to the MDR, while this is a {qm:medical device} according to ISO 13485.

    link> mdr:foobar