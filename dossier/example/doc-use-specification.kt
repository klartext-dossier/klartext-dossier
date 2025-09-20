!import "http://klartext-dossier.org/klartext-templates" as kt
!import "http://www.klartext-dossier.org/medical-device-file" as md

book: [en]

    titlepage:
        title: Use Specification for /r/device/

    table-of-contents:
        title: Table of Contents

    chapter:
        title:
            kt::value-of: select="//md:device/@name"

        kt::for-each: select="//md:intended-user"
            section:
                title:
                    kt::value-of: select="@name"

                kt::for-each: select="//md:clinical-function"
                    section:
                        title:
                            kt::value-of: select="@name"

    bibliography:
        title: Bibliography

    glossary:
        title: Glossary
