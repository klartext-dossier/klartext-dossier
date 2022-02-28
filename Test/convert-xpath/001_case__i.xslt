<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:dm="http://www.hoelzer-kluepfel.de/dossier">

    <xsl:output method="text"/>

    <xsl:template match="xml">
        <xsl:value-of select="dm:lower-case(@name)"/>,<xsl:value-of select="dm:upper-case(@name)"/>,<xsl:value-of select="dm:sentence-case(@name)"/>
    </xsl:template>

</xsl:stylesheet>