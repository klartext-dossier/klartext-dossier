<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.w3.org/1999/xhtml" xmlns:dm="http://klartext-dossier.org/dossier">

    <xsl:output method="xml" indent="yes"/>
   
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="xhtml:h1[not(@id)] | xhtml:h2[not(@id)] | xhtml:h3[not(@id)] | xhtml:h4[not(@id)] | xhtml:h5[not(@id)]">
        <xsl:element name="{name(.)}">
            <xsl:attribute name="id">
                <xsl:value-of select="concat('_', dm:unique-id())"/>
            </xsl:attribute>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:element>
    </xsl:template>

</xsl:stylesheet>
