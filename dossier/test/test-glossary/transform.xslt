<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.w3.org/1999/xhtml" xmlns:dm="http://klartext-dossier.org/dossier" xmlns:gls="http://klartext-dossier.org/glossary">

    <xsl:output method="xml" indent="yes"/>

    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="content|document">
        <xsl:apply-templates/>
    </xsl:template>

    <xsl:template match="definition">
        <dd>
            <xsl:apply-templates/>
        </dd>
    </xsl:template>

    <xsl:template match="xhtml:a[@data-type='xref' and @data-xrefstyle='glossary']">
        <xsl:copy-of select="gls:lookup(.)"/>
    </xsl:template>    

    <xsl:template match="entry">
        <xsl:if test="gls:used(.)">
            <dt id="{gls:link(.)}"><xsl:value-of select="gls:term(term[1])"/></dt>    
            <xsl:apply-templates select="definition"/>
        </xsl:if>
    </xsl:template>

    <xsl:template match="glossary">
        <section data-type="glossary">
            <h1><xsl:value-of select="@title"/></h1>

            <dl>
                <xsl:apply-templates select="entry">        
                    <xsl:sort select="term[1]"/>
                </xsl:apply-templates>
            </dl>
        </section>
    </xsl:template>

    <!-- Create the document structure -->
    <xsl:template match="/root">

        <html lang="en_US">

            <head>
                <meta charset="utf-8"/>
            </head>
    
            <body data-type="book">                

                <section data-type="chapter">
                    <h1>Content</h1>
        	        <xsl:apply-templates select="document/content"/>
                </section>

                <xsl:apply-templates select="//glossary"/>
            </body> 

        </html>

    </xsl:template>

</xsl:stylesheet>
