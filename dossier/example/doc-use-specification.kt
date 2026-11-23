!import "http://klartext-dossier.org/klartext-templates" as kt
!import "http://klartext-dossier.org/medical-device-file" as md
!import "http://www.w3.org/1999/xhtml" as html

book: [en]

    titlepage:
        title: Use Specification for /r/device/

    table-of-contents:
        title: Table of Contents

    chapter:
        title:
            kt::value-of: select="//md:device/@name"

        kt::if: test="//md:intended-use-summary"
            section:
                title: Intended Use Summary

                kt::copy-of: select="//md:intended-use-summary/html:*"
                    
        section:
            title: Medical Purpose

            kt::copy-of: select="//md:medical-purpose/html:*"

            kt::if: test="//md:medical-purpose/md:clinical-function"
                The device achieves its purpose by providing the following clinical functions:

                dl:
                    kt::for-each: select="//md:medical-purpose/md:clinical-function"
                        dt:
                            kt::value-of: select="@name"
                        dd:
                            kt::copy-of: select="html:*"

        section:
            title: Medical Indication

            kt::copy-of: select="//md:medical-indication/html:*"

        section:
            title: Patient Groups

            kt::for-each: select="//md:patient-group"
                section:
                    title:
                        kt::value-of: select="@name"
                    
                    kt::copy-of: select="html:*"

        section:
            title: Intended Users

            kt::for-each: select="//md:intended-user"
                section:
                    title:
                        kt::value-of: select="@name"

    bibliography:
        title: Bibliography

    glossary:
        title: Glossary
