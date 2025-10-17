!import "http://klartext-dossier.org/klartext-templates" as kt

book:

    data: #ID1 name="foobar"

    kt::value-of: select="//data/@name"

    kt::value-of: select="//data"

    kt::value-of: select="//foobar"
