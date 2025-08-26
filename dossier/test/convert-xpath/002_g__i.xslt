<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:gls="http://klartext-dossier.org/glossary">

    <xsl:output method="text"/>

    <xsl:template match="xml">
        <xsl:value-of select="gls:match(@name1, @name2)"/>
    </xsl:template>

</xsl:stylesheet>