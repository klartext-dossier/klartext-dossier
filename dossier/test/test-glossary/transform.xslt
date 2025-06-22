<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.w3.org/1999/xhtml">

    <xsl:output method="xml" indent="yes"/>

    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="content|document">
        <xsl:apply-templates/>
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
