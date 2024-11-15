<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:dm="http://www.hoelzer-kluepfel.de/dossier" exclude-result-prefixes="xhtml dm">

    <xsl:output method="xml" indent="yes"/>

    <xsl:strip-space elements="text()"/>

    <!-- FMC SPECIFIC! -->
    <xsl:template match="xhtml:span[@class='template']">
        <style color="#4169E1">
            <xsl:apply-templates/>
        </style>
    </xsl:template>

    <xsl:template match="xhtml:blockquote[@class='template']">
        <box color="#4169E1">
            <xsl:apply-templates/>
        </box>
    </xsl:template>

    <xsl:template match="xhtml:div[@class='template']">
        <paragraph>
            <style color="#4169E1">
                <xsl:apply-templates/>
            </style>
        </paragraph>
    </xsl:template>
    
    <xsl:template match="xhtml:div[@class='reference']//xhtml:a">
        <xsl:apply-templates/>
   </xsl:template>

    <xsl:template match="xhtml:div[@class='reference']">
        <paragraph style="Intense Quote">
            <xsl:apply-templates/>
        </paragraph>
    </xsl:template>

    <xsl:template match="xhtml:div[@class='tag']">
        <paragraph style="Caption">
            <xsl:apply-templates/>
        </paragraph>
    </xsl:template>

    <xsl:template match="xhtml:div[@class='name']">
        <paragraph style="Quote">
            <xsl:apply-templates/>
        </paragraph>
    </xsl:template>
    <!--  -->


    <xsl:template match="*/text()[not(normalize-space(.)) and not(preceding-sibling::xhtml:*)]"/>

    <xsl:template match="*/text()[normalize-space(.) or preceding-sibling::xhtml:*]">
        <run><xsl:value-of select="dm:simplify(.)"/></run>
    </xsl:template>

    <xsl:template match="xhtml:div">
        <paragraph>
            <xsl:apply-templates/>
        </paragraph>
    </xsl:template>

    <xsl:template match="xhtml:strong">
        <style class="b">
            <xsl:apply-templates/>
        </style>
    </xsl:template>

    <xsl:template match="xhtml:a">
        <style class="Subtle Reference">
            <xsl:apply-templates/>
        </style>
    </xsl:template>

    <xsl:template match="xhtml:em">
        <style class="i">
            <xsl:apply-templates/>
        </style>
    </xsl:template>

    <xsl:template match="xhtml:q">
        <run><xsl:text>“</xsl:text></run>
        <xsl:apply-templates/>
        <run><xsl:text>”</xsl:text></run>
    </xsl:template>

    <xsl:template match="xhtml:code">
        <style class="code">
            <xsl:apply-templates/>
        </style>
    </xsl:template>

    <xsl:template match="xhtml:span[@class='underline']">
        <style class="ul">
            <xsl:apply-templates/>
        </style>
    </xsl:template>

    <xsl:template match="xhtml:span[@class='line-through']">
        <style class="strike">
            <xsl:apply-templates/>
        </style>
    </xsl:template>

    <xsl:template match="xhtml:sub">
        <style class="sub">
            <xsl:apply-templates/>
        </style>
    </xsl:template>

    <xsl:template match="xhtml:sup">
        <style class="sup">
            <xsl:apply-templates/>
        </style>
    </xsl:template>

    <xsl:template match="xhtml:p">
        <paragraph>
            <xsl:apply-templates/>
        </paragraph>
    </xsl:template>

    <xsl:template match="xhtml:li">
        <xsl:variable name="level">
            <xsl:if test="(count(ancestor::xhtml:ol)+count(ancestor::xhtml:ul))>1">
                <xsl:text> </xsl:text><xsl:value-of select="count(ancestor::xhtml:ol)+count(ancestor::xhtml:ul)"/>
            </xsl:if>
        </xsl:variable>
        <xsl:variable name="style">
            <xsl:if test="parent::xhtml:ol">
                <xsl:text>List Number</xsl:text>
            </xsl:if>
            <xsl:if test="parent::xhtml:ul">
                <xsl:text>List Bullet</xsl:text>
            </xsl:if>
        </xsl:variable>
        <paragraph style="{concat($style, $level)}">
            <xsl:apply-templates/>
        </paragraph>
    </xsl:template>

    <xsl:template match="xhtml:dd">
        <paragraph>
            <xsl:apply-templates/>
        </paragraph>
    </xsl:template>

    <xsl:template match="xhtml:dt">
        <paragraph>
            <style class="b">
                <xsl:apply-templates/>
            </style>
        </paragraph>
    </xsl:template>

    <xsl:template match="xhtml:ol|xhtml:ul|xhtml:dl">
        <xsl:apply-templates/>       
    </xsl:template>

    <xsl:template match="xhtml:caption">
        <paragraph style="Caption">
            <xsl:apply-templates/>
        </paragraph>
    </xsl:template>

    <xsl:template match="xhtml:td">
        <td>
            <xsl:copy-of select="@*"/>
            <xsl:apply-templates/>
        </td>
    </xsl:template>

    <xsl:template match="xhtml:th">
        <th>
            <xsl:copy-of select="@*"/>
            <xsl:apply-templates/>
        </th>
    </xsl:template>

    <xsl:template match="xhtml:tr">
        <tr>
            <xsl:copy-of select="@*"/>
            <xsl:apply-templates select="xhtml:th|xhtml:td"/>
        </tr>
    </xsl:template>

    <xsl:template match="xhtml:table">
        <xsl:apply-templates select="xhtml:caption"/>
        <table style="Table Grid">
            <xsl:apply-templates select="xhtml:tr|xhtml:thead/xhtml:tr|xhtml:tbody/xhtml:tr"/>
        </table>
    </xsl:template>

    <xsl:template match="xhtml:section[@data-type='sect4']">
        <heading level="5"><xsl:value-of select="xhtml:header/xhtml:h4|xhtml:h4"/></heading>
        <xsl:apply-templates select="*[not(self::xhtml:h4) and not(self::xhtml:header/xhtml:h4)]"/>
    </xsl:template>

    <xsl:template match="xhtml:section[@data-type='sect3']">
        <heading level="4"><xsl:value-of select="xhtml:header/xhtml:h3|xhtml:h3"/></heading>
        <xsl:apply-templates select="*[not(self::xhtml:h3) and not(self::xhtml:header/xhtml:h3)]"/>
    </xsl:template>

    <xsl:template match="xhtml:section[@data-type='sect2']">
        <heading level="3"><xsl:value-of select="xhtml:header/xhtml:h2|xhtml:h2"/></heading>
        <xsl:apply-templates select="*[not(self::xhtml:h2) and not(self::xhtml:header/xhtml:h2)]"/>
    </xsl:template>

    <xsl:template match="xhtml:section[@data-type='sect1']">
        <heading level="2"><xsl:value-of select="xhtml:header/xhtml:h1|xhtml:h1"/></heading>
        <xsl:apply-templates select="*[not(self::xhtml:h1) and not(self::xhtml:header/xhtml:h1)]"/>
    </xsl:template>

    <xsl:template match="xhtml:section[@data-type='chapter']|xhtml:section[@data-type='appendix']">
        <heading level="1"><xsl:value-of select="xhtml:header/xhtml:h1|xhtml:h1"/></heading>
        <xsl:apply-templates select="*[not(self::xhtml:h1) and not(self::xhtml:header/xhtml:h1)]"/>
    </xsl:template>

    <xsl:template name="header.attributes">
        <xsl:for-each select="xhtml:header/xhtml:p[@data-type='subtitle']">
            <paragraph style="Subtitle">
                <run><xsl:value-of select="."/></run>
            </paragraph>
        </xsl:for-each>

        <xsl:for-each select="xhtml:header/xhtml:p[@data-type='author']">
            <paragraph>
                <run style="Subtle Emphasis"><xsl:value-of select="."/></run>
            </paragraph>
        </xsl:for-each>
    </xsl:template>

    <xsl:template match="xhtml:section[@data-type='halftitlepage']">
        <xsl:if test="xhtml:header/xhtml:h1|xhtml:h1">
            <paragraph>
                <run style="Book Title"><xsl:value-of select="xhtml:header/xhtml:h1|xhtml:h1"/></run>
            </paragraph>
        </xsl:if>

        <xsl:call-template name="header.attributes"/>

        <xsl:apply-templates select="*[not(self::xhtml:h1) and not(self::xhtml:header)]"/>
        
        <break class="page"/>
    </xsl:template>

    <xsl:template match="xhtml:section[@data-type='titlepage']">
        <xsl:if test="xhtml:header/xhtml:h1|xhtml:h1">
            <paragraph style="Title">
                <run><xsl:value-of select="xhtml:header/xhtml:h1|xhtml:h1"/></run>
            </paragraph>
        </xsl:if>

        <xsl:call-template name="header.attributes"/>

        <xsl:apply-templates select="*[not(self::xhtml:h1) and not(self::xhtml:header)]"/>
        
        <break class="page"/>
    </xsl:template>

    <xsl:template match="div[@data-type='part']">
        <!-- TODO -->
    </xsl:template>

    <xsl:template match="xhtml:section[contains('|preface|introduction|copyright-page|dedication|foreword|acknowledgments|afterword|conclusion|colophon|glossary|bibliography|appendix', concat(concat('|', @data-type), '|'))]">
        <xsl:if test="xhtml:header/xhtml:h1|xhtml:h1">
            <heading level="1"><xsl:value-of select="xhtml:header/xhtml:h1|xhtml:h1"/></heading>
        </xsl:if>

        <xsl:call-template name="header.attributes"/>

        <xsl:apply-templates select="*[not(self::xhtml:h1) and not(self::xhtml:header/xhtml:h1)]"/>

        <break class="page"/>
    </xsl:template>

    <xsl:template match="xhtml:nav">
        <xsl:if test="xhtml:header/xhtml:h1|xhtml:h1">
            <heading level="1"><xsl:value-of select="xhtml:header/xhtml:h1|xhtml:h1"/></heading>
        </xsl:if>
        <nav/>
        <break class="page"/>
    </xsl:template>

    <xsl:template match="xhtml:header">
        <!-- TODO -->
    </xsl:template>

    <xsl:template match="xhtml:h5">
        <paragraph>
            <style class="b">
                <xsl:apply-templates/>
            </style>
        </paragraph>
    </xsl:template>

    <xsl:template match="xhtml:div[@data-type='warning']">
        <box color="#F44336">
            <xsl:apply-templates/>
        </box>
    </xsl:template>

    <xsl:template match="xhtml:div[@data-type='note']">
        <box color="#FFEB3B">
            <xsl:apply-templates/>
        </box>
    </xsl:template>

    <xsl:template match="xhtml:div[@data-type='note']">
        <box color="#FFEB3B">
            <xsl:apply-templates/>
        </box>
    </xsl:template>

    <xsl:template match="xhtml:div[@data-type='caution']">
        <box color="#33FFBD">
            <xsl:apply-templates/>
        </box>
    </xsl:template>

    <xsl:template match="xhtml:div[@data-type='important']">
        <box color="#DBFF33">
            <xsl:apply-templates/>
        </box>
    </xsl:template>

    <xsl:template match="xhtml:div[@data-type='tip']">
        <box color="#75FF33">
            <xsl:apply-templates/>
        </box>
    </xsl:template>

    <xsl:template match="xhtml:div[@data-type='example']">
        <box color="#F0F0F0">
            <xsl:apply-templates/>
        </box>
    </xsl:template>

    <xsl:template match="xhtml:body[@data-type='book']">
        <xsl:if test="xhtml:header/xhtml:h1|xhtml:h1">
            <heading level="0"><xsl:value-of select="xhtml:header/xhtml:h1|xhtml:h1"/></heading>
        </xsl:if>

        <xsl:apply-templates select="*[not(self::xhtml:h1) and not(self::xhtml:header/xhtml:h1)]"/>
        
    </xsl:template>

    <!-- <img src="image-life-cycle-overview.png" alt="Software Engineering Life Cycle Overview" width="100%" class="bordered"/> -->

    <xsl:template match="xhtml:img">
        <xsl:variable name="src" select="@src"/>
        <image src="{$src}" width="{@width}" height="{@height}"/>
        <xsl:if test="@alt">
            <paragraph style="Caption">
                <run><xsl:value-of select="@alt"/></run>
            </paragraph>
        </xsl:if>
    </xsl:template>

    <xsl:template match="xhtml:html">
        <document>
            <xsl:apply-templates select="xhtml:body[@data-type='book']"/>
        </document>
    </xsl:template>

</xsl:stylesheet>
