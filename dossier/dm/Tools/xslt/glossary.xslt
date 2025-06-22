<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.w3.org/1999/xhtml" xmlns:gls="http://klartext-dossier.org/glossary">

    <xsl:output method="xml" indent="yes"/>

    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="definition">
        <dd data-type="glossdef">
            <dfn><xsl:apply-templates/></dfn>
        </dd>
    </xsl:template>

    <xsl:template match="xhtml:a[@data-type='xref' and @data-xrefstyle='glossary']">
        <xsl:copy-of select="gls:lookup(.)"/>
    </xsl:template>    

    <xsl:template match="entry">
        <xsl:if test="gls:used(.)">
            <dt id="{gls:link(.)}" data-type="glossterm"><xsl:value-of select="gls:term(term[1])"/></dt>    
            <xsl:apply-templates select="definition"/>
        </xsl:if>
    </xsl:template>

    <xsl:template match="glossary">
        <section data-type="glossary">
            <h1><xsl:value-of select="@title"/></h1>

            <dl data-type="glossary">
                <xsl:apply-templates select="entry">        
                    <xsl:sort select="term[1]"/>
                </xsl:apply-templates>
            </dl>
        </section>
    </xsl:template>

</xsl:stylesheet>
