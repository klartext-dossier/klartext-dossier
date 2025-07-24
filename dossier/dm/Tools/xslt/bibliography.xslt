<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.w3.org/1999/xhtml" xmlns:re="http://exslt.org/regular-expressions" exclude-result-prefixes="re">

    <xsl:output method="xml" indent="yes"/>
   
    <!-- This is the default template. It copies every element that is not matched by another template. -->
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="references">
        <xsl:variable name="refs">
            <xsl:for-each select="reference">
                <xsl:variable name="ref"><xsl:value-of select="@id"/></xsl:variable>
                <xsl:if test="//xhtml:a[re:test(@href, $ref, 'i')]">
                    <xsl:value-of select="$ref"/>
                </xsl:if>
            </xsl:for-each>
        </xsl:variable>

        <xsl:if test="'' != $refs">
            <dl>
                <xsl:for-each select="reference">
                    <xsl:sort select="@name" data-type="text"/>
                    <xsl:variable name="ref"><xsl:value-of select="@id"/></xsl:variable>
                    <xsl:if test="//xhtml:a[re:test(@href, $ref, 'i')]">
                        <dt id="{$ref}"><xsl:value-of select="@name"/></dt>
                        <xsl:if test="id">
                            <dd><xsl:value-of select="id"/></dd>
                        </xsl:if>
                        <dd><xsl:value-of select="title"/></dd>
                        <xsl:if test="version">
                            <dd>Version: <xsl:value-of select="version"/></dd>
                        </xsl:if>
                        <xsl:if test="edition">
                            <dd>Edition: <xsl:value-of select="edition"/></dd>
                        </xsl:if>                    
                    </xsl:if>
                </xsl:for-each>
            </dl>
        </xsl:if>
    </xsl:template>

</xsl:stylesheet>
