<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:dm="http://klartext-dossier.org/dossier">

    <xsl:output method="text"/>

    <xsl:template match="xml">
        <xsl:value-of select="dm:match-g(@name1, @name2)"/>
    </xsl:template>

</xsl:stylesheet>