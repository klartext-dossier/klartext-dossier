<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.w3.org/1999/xhtml" xmlns:gls="http://klartext-dossier.org/glossary" exclude-result-prefixes="gls">

    <xsl:output method="xml" indent="yes"/>

    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

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
        <dd data-type="glossdef">
            <xsl:apply-templates/>
        </dd>
    </xsl:template>

    <xsl:template match="xhtml:a[@data-type='xref' and @data-xrefstyle='glossary']">
        <xsl:copy-of select="gls:lookup(.)"/>
    </xsl:template>    

    <xsl:template match="entry">
        <xsl:if test="gls:used(.)">
            <dt id="{gls:link(.)}" data-type="glossterm"><dfn><xsl:value-of select="gls:term(term[1])"/></dfn></dt>    
            <xsl:apply-templates select="definition"/>
        </xsl:if>
    </xsl:template>

    <xsl:template match="glossary">
        <section data-type="sect1">
            <h1><xsl:value-of select="name"/></h1>
            <dl>
                <xsl:apply-templates select="entry">        
                    <xsl:sort select="term[1]"/>
                </xsl:apply-templates>
            </dl>
        </section>
    </xsl:template>

</xsl:stylesheet>
