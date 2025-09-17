<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.w3.org/1999/xhtml" xmlns:ktt="http://klartext-dossier.org/klartext-templates" xmlns:exsl="http://exslt.org/common" extension-element-prefixes="exsl ktt">

    <xsl:output method="xml" indent="yes"/>

    <xsl:template match="ktt:for-each">
        <xsl:apply-templates select="ktt:for-each()/*"/>
    </xsl:template>

    <xsl:template match="ktt:value-of">
        <xsl:value-of select="ktt:value-of()"/>
    </xsl:template>


    <!-- This is the default template. It copies every element that is not matched by another template. -->
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <!-- Remove the p nodes in custom elements -->
    <xsl:template match="title/xhtml:p|author/xhtml:p|subtitle/xhtml:p">
        <xsl:for-each select="@*|node()">
            <xsl:copy>
                <xsl:copy-of select="@*" />
                <xsl:apply-templates />
            </xsl:copy>
        </xsl:for-each>
    </xsl:template>

    <!-- Omit the book's title in the body, as it is moved to the head -->
    <xsl:template match="book/title"/>

    <!-- Table of contents -->
    <xsl:template match="table-of-contents">
        <nav data-type="toc">
            <xsl:if test="title">
                <h1>
                    <xsl:apply-templates select="title/xhtml:p"/>
                </h1>
            </xsl:if>
        </nav>
    </xsl:template>


    <!-- Section titles -->
    <xsl:template match="section/title|section/header/title">
        <xsl:element name="h{count(ancestor::section)}">
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template>

    <!-- Sections -->
    <xsl:template match="section">
        <section data-type="sect{count(ancestor::section)+1}">
            <xsl:apply-templates/>
        </section>
    </xsl:template>

    <!-- Parts -->
    <xsl:template match="part">
        <div data-type="part">
            <xsl:apply-templates/>
        </div>
    </xsl:template>

    <!-- Subtitles and authors in headers -->
    <xsl:template match="subtitle|author">
        <p data-type="{local-name()}">
            <xsl:apply-templates/>
        </p>
    </xsl:template>

    <!-- Headers of book elements -->
    <xsl:template match="chapter/header|appendix/header|bibliography/header|glossary/header|preface/header|foreword/header|introduction/header|halftitlepage/header|titlepage/header|copyright-page/header|dedication/header|colophon/header|acknowledgments/header|afterword/header|conclusion/header|part/header|index/header|section/header">
        <h1>
            <xsl:apply-templates select="title/*"/>
        </h1>
        <xsl:apply-templates select="subtitle"/>
        <xsl:apply-templates select="author"/>
    </xsl:template>

    <!-- Titles of book elements -->
    <xsl:template match="chapter/title|appendix/title|bibliography/title|glossary/title|preface/title|foreword/title|introduction/title|halftitlepage/title|titlepage/title|copyright-page/title|dedication/title|colophon/title|acknowledgments/title|afterword/title|conclusion/title|part/title|index/title">
        <h1>
            <xsl:apply-templates/>
        </h1>
    </xsl:template>

    <!-- Bibliography -->
    <xsl:template match="bibliography">
        <section data-type="bibliography">
            <xsl:apply-templates/>
            <xsl:copy-of select="//references"/>
        </section>
    </xsl:template>

    <!-- Glossary -->
    <xsl:template match="glossary">
        <section data-type="glossary">
            <xsl:apply-templates/>
            <xsl:copy-of select="/root/glossary"/>
        </section>
    </xsl:template>

    <!-- Other book elements -->
    <xsl:template match="chapter|appendix|preface|foreword|introduction|halftitlepage|titlepage|copyright-page|dedication|colophon|acknowledgments|afterword|conclusion|index">
        <section data-type="{local-name()}">
            <xsl:apply-templates/>
        </section>
    </xsl:template>

    <!-- Transform the book element into an XHTML document -->
    <xsl:template match="book">
        <html>
            <xsl:if test="@xml:lang">
                <xsl:attribute name="lang">
                    <xsl:value-of select="@xml:lang"/>
                </xsl:attribute>    
            </xsl:if>
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
