<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/1999/xhtml" xmlns:kt="http://klartext-dossier.org/klartext-templates" extension-element-prefixes="kt">

    <xsl:output method="xml" indent="yes"/>

    <!-- This is the default template. It copies every element that is not matched by another template. -->
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="kt:for-each">
        <xsl:apply-templates select="kt:for-each()/*"/>
    </xsl:template>

    <xsl:template match="kt:value-of">
        <xsl:apply-templates select="kt:value-of()"/>
    </xsl:template>

    <xsl:template match="kt:copy-of">
        <xsl:copy-of select="kt:copy-of()"/>
    </xsl:template>

    <xsl:template match="kt:if">
        <xsl:apply-templates select="kt:if()/*"/>
    </xsl:template>

</xsl:stylesheet>
