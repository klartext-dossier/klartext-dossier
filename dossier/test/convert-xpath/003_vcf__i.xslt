<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:vcf="http://www.hoelzer-kluepfel.de/vcf">

    <xsl:output method="text"/>

    <xsl:template match="xml">
        <xsl:value-of select="vcf:ADR(@adr)"/>
    </xsl:template>

</xsl:stylesheet>