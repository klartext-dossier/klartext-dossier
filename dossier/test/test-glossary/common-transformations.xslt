<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.w3.org/1999/xhtml" xmlns:dm="http://www.hoelzer-kluepfel.de/dossier" xmlns:gls="http://klartext-dossier.org/glossary" exclude-result-prefixes="dm gls">

    <xsl:output method="xml" indent="yes"/>

    <xsl:key name="entries" match="entry" use="term"/>

    <!-- This is the default template. It copies every element that is not matched by another template. -->
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>
   

    <xsl:template match="content">
        <xsl:apply-templates/>
    </xsl:template>


    <xsl:template name="reference.link">
        <xsl:param name="target"/>
        <xsl:choose>
            <xsl:when test="//*[@id=$target]/@name">
                <a href="#{$target}"><xsl:value-of select="//*[@id=$target]/@name"/></a>
            </xsl:when>
            <xsl:when test="//*[@id=$target]/@title">
                <q><a href="#{$target}"><xsl:value-of select="//*[@id=$target]/@title"/></a></q>
            </xsl:when>
            <xsl:when test="//*[@id=$target]/name">
                <a href="#{$target}"><xsl:value-of select="normalize-space(//*[@id=$target]/name/text())"/></a>              
            </xsl:when>
            <xsl:otherwise>
                <span class="syntax-error"><xsl:value-of select="$target"/></span>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>


    <xsl:template match="xhtml:r">       
        <xsl:call-template name="reference.link">
            <xsl:with-param name="target"><xsl:value-of select="normalize-space(text())"/></xsl:with-param>
        </xsl:call-template>
    </xsl:template>    


    <xsl:template match="xhtml:a[@data-type='xref' and @data-xrefstyle='glossary']">       
        <xsl:variable name="term" select="normalize-space(text())"/>
        <xsl:choose>
            <xsl:when test="//term[gls:match(normalize-space(text()), $term)]">
                <xsl:variable name="ref" select="//term[gls:match(normalize-space(text()), $term)]/../term[1]/text()"/>
                <a href="#{dm:id(string($ref))}"><xsl:value-of select="."/></a>
            </xsl:when>
            <xsl:otherwise>
                <span class="syntax-error"><xsl:value-of select="$term"/></span>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>    


    <xsl:template name="toc.section">
        <xsl:param name="title" select="'Table of Contents'"/>
        <nav data-type="toc">
            <h1><xsl:value-of select="$title"/></h1>
        </nav>  
    </xsl:template>


    <xsl:template name="glossary.section">
        <section data-type="glossary">
            <h1><xsl:value-of select="//glossary/@title"/></h1>

            <xsl:if test="count(//glossary)>1">
                <xsl:for-each select="//glossary">
                    <section data-type="sect1">
                        <h1><xsl:value-of select="@name"/></h1>
                        <xsl:copy-of select="."/>        
                    </section>
                </xsl:for-each>
            </xsl:if>
            
            <xsl:if test="count(//glossary)=1">
                <xsl:copy-of select="//glossary"/>        
            </xsl:if>
        </section>
    </xsl:template>


    <xsl:template name="bibliography.section">
        <section data-type="bibliography">
            <h1><xsl:value-of select="//references/@name"/></h1>
            <section data-type="sect1">
                <xsl:copy-of select="//references"/>
            </section>
        </section>
    </xsl:template>

</xsl:stylesheet>
