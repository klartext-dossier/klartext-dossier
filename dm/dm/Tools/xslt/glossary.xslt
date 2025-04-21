<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.w3.org/1999/xhtml">

    <xsl:output method="xml" indent="yes"/>
   
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="xhtml:section[@data-type='glossary']/xhtml:dl">
        <xsl:element name="dl">
            <xsl:attribute name="data-type">glossary</xsl:attribute>
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template>

    <xsl:template match="xhtml:dfn">
        <xsl:apply-templates/>
    </xsl:template>

    <xsl:template match="xhtml:section[@data-type='glossary']/xhtml:dl/xhtml:dt">
        <dt id="{@id}" data-type="glossterm">
            <dfn><xsl:apply-templates/></dfn>
        </dt>
    </xsl:template>

    <xsl:template match="xhtml:section[@data-type='glossary']/xhtml:dl/xhtml:dd">
        <dd data-type="glossdef">
            <xsl:apply-templates/>
        </dd>
    </xsl:template>

</xsl:stylesheet>
