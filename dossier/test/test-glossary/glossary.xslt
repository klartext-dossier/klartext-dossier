<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.w3.org/1999/xhtml" xmlns:re="http://exslt.org/regular-expressions" xmlns:dm="http://www.hoelzer-kluepfel.de/dossier" exclude-result-prefixes="re dm">

    <!-- Import the common transformation stylesheet -->
    <xsl:import href="common-transformations.xslt"/>
    
    <xsl:output method="xml" indent="yes"/>

    <xsl:key name="entries" match="entry" use="dm:lower-case(normalize-space(string(term/text())))"/>

    <xsl:template match="definition/origin[1]">
        <div class="reference">
            <xsl:variable name="target" select="@ref"/>
            <a href="#{$target}"><xsl:value-of select="normalize-space(//reference[@id=$target]/@name)"/></a>
            <xsl:if test="@section">
                <xsl:text>, </xsl:text>
                <xsl:value-of select="@section"/>
            </xsl:if>            
        </div>
    </xsl:template>


    <xsl:template match="definition">
        <dd>
            <xsl:apply-templates/>
        </dd>
    </xsl:template>


    <xsl:template name="check.use">
        <xsl:param name="term-to-check"/>
        <xsl:param name="depth" select="1"/>        
        <xsl:variable name="ref">#<xsl:value-of select="dm:id(string($term-to-check))"/></xsl:variable>
        <xsl:choose>
            <xsl:when test="//xhtml:a[dm:match-g(@href, $ref)]">
                <xsl:value-of select="$term-to-check"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:for-each select="//glossary/entry">
                    <xsl:variable name="entry-to-check" select="term[1]"/>
                    <xsl:for-each select="definition//xhtml:a[@data-type='xref' and @data-xrefstyle='glossary']">
                        <xsl:variable name="used-text" select="string(.)"/>
                        <xsl:variable name="term-used-in-entry" select="key('entries', dm:lower-case($used-text))/term[1]"/>
                        <xsl:if test="re:test(normalize-space($term-used-in-entry), $term-to-check, 'i')">
                            <xsl:if test="$depth &lt; 5">
                                <xsl:call-template name="check.use">
                                    <xsl:with-param name="term-to-check" select="$entry-to-check"/>
                                    <xsl:with-param name="depth" select="$depth+1"/>
                                </xsl:call-template>
                            </xsl:if>
                        </xsl:if>
                    </xsl:for-each>
                </xsl:for-each>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>


    <xsl:template match="entry">
        <xsl:variable name="term"><xsl:value-of select="normalize-space(term[1]/text())"/></xsl:variable>

        <xsl:variable name="used">
            <xsl:call-template name="check.use">
                <xsl:with-param name="term-to-check" select="$term"/>
            </xsl:call-template>
        </xsl:variable>

        <xsl:if test="$used != ''">
            <dt id="{dm:id(string($term))}">
                <xsl:value-of select="$term"/>
            </dt>
            <xsl:apply-templates select="definition"/>        
        </xsl:if>
    </xsl:template>


    <xsl:template match="glossary">
        <dl data-type="glossary">
            <xsl:apply-templates select="entry">
                <xsl:sort select="term/text()" order="ascending"/>
            </xsl:apply-templates>
        </dl>
    </xsl:template>

</xsl:stylesheet>
