<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.w3.org/1999/xhtml">

    <xsl:output method="xml" indent="yes"/>

    <!-- This is the default template. It copies every element that is not matched by another template. -->
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <!-- Remove the p nodes in titles -->
    <xsl:template match="title/xhtml:p">
        <xsl:for-each select="@*|node()">
            <xsl:copy>
                <xsl:copy-of select="@*" />
                <xsl:apply-templates />
            </xsl:copy>
        </xsl:for-each>
    </xsl:template>

    <!-- Omit the book's title in the body, as it is moved to the head -->
    <xsl:template match="book/title"/>

    <xsl:template match="table-of-contents">
        <nav data-type="toc">
            <xsl:if test="title">
                <h1>
                    <xsl:apply-templates select="title/xhtml:p"/>
                </h1>
            </xsl:if>
        </nav>
    </xsl:template>

    <xsl:template match="chapter/title|sect1/title">
        <h1>
            <xsl:apply-templates/>
        </h1>
    </xsl:template>

    <xsl:template match="chapter|sect1">
        <section data-type="{local-name()}">
            <xsl:apply-templates/>
        </section>
    </xsl:template>

    <!-- Transform the book element into an XHTML document -->
    <xsl:template match="book">
        <html>
            <head>
                <xsl:if test="title">
                    <h1>
                        <xsl:apply-templates select="title/xhtml:p"/>
                    </h1>
                </xsl:if>
            </head>

            <body data-type="book">
                <xsl:apply-templates/>
            </body>
        </html>
    </xsl:template>

    <!-- Start processing from the root element -->
    <xsl:template match="/root">
        <xsl:apply-templates select="book"/>
    </xsl:template>

</xsl:stylesheet>
