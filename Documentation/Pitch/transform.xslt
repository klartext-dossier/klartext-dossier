<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/1999/xhtml" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:re="http://exslt.org/regular-expressions" exclude-result-prefixes="re">

    <xsl:output method="xml" indent="yes"/>


    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>


    <xsl:template match="notes"/>


    <xsl:template match="presentation">
        <section class="presentation">
            <h3><xsl:value-of select="@title"/></h3>
            <h3 class="subtitle"><xsl:value-of select="@subtitle"/></h3>
            <img src="image-presentation-footer.png" alt=""/>
            <ul>
                <xsl:for-each select="section">
                    <li><a href="#section-{position()}"><xsl:value-of select="@title"/></a></li>
                </xsl:for-each>
            </ul>
            <xsl:if test="@author">
                <p class="author"><xsl:value-of select="@author"/></p>
            </xsl:if>
        </section>
        <xsl:apply-templates/>
    </xsl:template>


    <xsl:template match="section">
        <section class="section">
            <h3 id="section-{count(preceding-sibling::section)+1}"><xsl:value-of select="@title"/></h3>
            <img src="image-section-footer.png" alt=""/>
        </section>
        <xsl:apply-templates/>
    </xsl:template>


    <xsl:template match="slide[@master='contact']">
        <section class="contact">
            <h3><xsl:value-of select="@title"/></h3>
            <img src="image-portrait.png" alt="Portrait"/>
            <div class="text">
                <xsl:apply-templates/>
            </div>
        </section>
    </xsl:template>


    <xsl:template match="slide[@master='summary']">
        <section class="summary">
            <h3><xsl:value-of select="@title"/></h3>
            <div class="text">
                <xsl:apply-templates/>
            </div>
            <img src="image-summary-footer.png" alt=""/>
        </section>
    </xsl:template>


    <xsl:template match="slide[@master='text']">
        <section class="slide">
            <h3><xsl:value-of select="@title"/></h3>
            <div class="text">
                <xsl:apply-templates/>
            </div>
        </section>
    </xsl:template>


    <xsl:template match="slide[@master='table']">
        <section class="table">
            <h3><xsl:value-of select="@title"/></h3>
            <xsl:apply-templates select="*"/>
        </section>
    </xsl:template>


    <xsl:template match="slide[@master='objectives']">
        <section class="objectives">
            <h3><xsl:value-of select="@title"/></h3>
            <xsl:apply-templates select="*"/>
        </section>
    </xsl:template>


    <xsl:template match="slide[@master='activities']">
        <section class="activities">
            <h3><xsl:value-of select="@title"/></h3>
            <xsl:apply-templates select="*"/>
        </section>
    </xsl:template>


    <xsl:template match="slide[@master='image']">
        <section class="image">
            <h3><xsl:value-of select="@title"/></h3>
            <xsl:apply-templates select="*"/>
        </section>
    </xsl:template>


    <xsl:template match="slide[@master='diagram']">
        <section class="diagram">
            <h3><xsl:value-of select="@title"/></h3>
            <div class="diagram">
                <xsl:apply-templates select="*"/>
            </div>
        </section>
    </xsl:template>


    <xsl:template match="/root">

        <html>

            <head>
                <meta charset="utf-8"/>
            </head>
    
            <body>
                <xsl:apply-templates/>
            </body> 

        </html>

    </xsl:template>

</xsl:stylesheet>