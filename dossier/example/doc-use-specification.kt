!import "http://klartext-dossier.org/klartext-templates" as ktt
!import "http://www.klartext-dossier.org/medical-device-file" as md

book: [en]

    titlepage:
        title: Use Specification for /r/device/ 

    table-of-contents:
        title: Table of Contents

    chapter:
        title:
            ktt::value-of: select="//md:device/@name"            

        ktt::for-each: select="//md:intended-user"
            section:
                title: 
                    ktt::value-of: select="@name"

    bibliography:
        title: Bibliography

    glossary:
        title: Glossary
