<!-- This stylesheet creates a table of contents. 

     When applied to an HTMLBook file, the stylesheet will replace the '<nav data-type="toc"/>" element
     with a table of contents based on the chapters and sections of the HTMLBook document.

-->

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.w3.org/1999/xhtml">

    <xsl:output method="xml" indent="yes"/>
   
    <!-- This is the default template. It copies every element that is not matched by another template. -->
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <!-- Do not generate TOC entries for sect3 sections. -->
    <xsl:template match="xhtml:section[@data-type='sect3']" mode="toc"/>

    <!-- Generate TOC entries for sect2 sections. -->
    <xsl:template match="xhtml:section[@data-type='sect2']" mode="toc">
        <xsl:param name="chapter_nr"/>
        <xsl:param name="sect1_nr"/>
        <xsl:variable name="sect2_nr"><xsl:value-of select="count(preceding-sibling::xhtml:section[@data-type='sect2']) + 1"/></xsl:variable>

        <li class="sect2">
            <a data-nr="{$chapter_nr}.{$sect1_nr}.{$sect2_nr}"><xsl:attribute name="href">#<xsl:value-of select="xhtml:h2/@id|xhtml:header/xhtml:h2/@id"/></xsl:attribute><xsl:value-of select="xhtml:h2|xhtml:header/xhtml:h2"/></a>
        </li>    
    </xsl:template>

    <!-- Generate TOC entries for sect1 sections. -->
    <xsl:template match="xhtml:section[@data-type='sect1']" mode="toc">
        <xsl:param name="chapter_nr"/>
        <xsl:variable name="sect1_nr"><xsl:value-of select="count(preceding-sibling::xhtml:section[@data-type='sect1']) + 1"/></xsl:variable>
        <li class="sect1">
            <a data-nr="{$chapter_nr}.{$sect1_nr}"><xsl:attribute name="href">#<xsl:value-of select="xhtml:h1/@id|xhtml:header/xhtml:h1/@id"/></xsl:attribute><xsl:value-of select="xhtml:h1|xhtml:header/xhtml:h1"/></a>

            <xsl:if test="xhtml:section[@data-type='sect2']">
                <ol>
                    <xsl:apply-templates select="xhtml:section[@data-type='sect2']" mode="toc">
                        <xsl:with-param name="chapter_nr" select="$chapter_nr"/>
                        <xsl:with-param name="sect1_nr" select="$sect1_nr"/>
                    </xsl:apply-templates>
                </ol>
            </xsl:if>
        </li>
    </xsl:template>

    <!-- Generate TOC entries for chapters. -->
    <xsl:template match="xhtml:section[@data-type='chapter']" mode="toc">        
        <xsl:variable name="chapter_nr"><xsl:value-of select="count(preceding-sibling::xhtml:section[@data-type='chapter']) + 1"/></xsl:variable>

        <li class="chapter">
            <a data-nr="{$chapter_nr}"><xsl:attribute name="href">#<xsl:value-of select="xhtml:h1/@id|xhtml:header/xhtml:h1/@id"/></xsl:attribute><xsl:value-of select="xhtml:h1|xhtml:header/xhtml:h1"/></a>

            <xsl:if test="xhtml:section[@data-type='sect1']">
                <ol>
                    <xsl:apply-templates select="xhtml:section[@data-type='sect1']" mode="toc">
                        <xsl:with-param name="chapter_nr" select="$chapter_nr"/>
                    </xsl:apply-templates>
                </ol>
            </xsl:if>
        </li>
    </xsl:template>

    <!-- Generate TOC entries for parts. -->
    <xsl:template match="xhtml:div[@data-type='part']" mode="toc">        
        <xsl:variable name="part_nr"><xsl:number format="I" select="count(preceding-sibling::xhtml:div[@data-type='part']) + 1"/></xsl:variable>

        <li class="part">
            <a data-nr="{$part_nr}"><xsl:attribute name="href">#<xsl:value-of select="xhtml:h1/@id|xhtml:header/xhtml:h1/@id"/></xsl:attribute><xsl:value-of select="xhtml:h1|xhtml:header/xhtml:h1"/></a>

            <xsl:if test="xhtml:section[@data-type='chapter']">
                <ol>
                    <xsl:apply-templates select="xhtml:section[@data-type='chapter']" mode="toc"/>
                </ol>
            </xsl:if>
        </li>
    </xsl:template>

    <!-- Generate TOC entries for appendices. -->
    <xsl:template match="xhtml:section[@data-type='appendix']" mode="toc">
        <xsl:variable name="chapter_nr"><xsl:value-of select="substring('ABCDEFGHIJKLMNOPQRSTUVWXYZ', count(preceding-sibling::xhtml:section[@data-type='appendix']) + 1, 1)"/></xsl:variable>
        <li class="chapter">
            <a data-nr="{$chapter_nr}"><xsl:attribute name="href">#<xsl:value-of select="xhtml:h1/@id|xhtml:header/xhtml:h1/@id"/></xsl:attribute><xsl:value-of select="xhtml:h1|xhtml:header/xhtml:h1"/></a>
        </li>
    </xsl:template>

    <!-- Generate TOC entries for glossary and bibliography. -->
    <xsl:template match="xhtml:section[contains('glossary bibliography', @data-type)]" mode="toc">
        <li class="chapter">
            <a><xsl:attribute name="href">#<xsl:value-of select="xhtml:h1/@id|xhtml:header/xhtml:h1/@id"/></xsl:attribute><xsl:value-of select="xhtml:h1|xhtml:header/xhtml:h1"/></a>
        </li>
    </xsl:template>

    <!-- Replace the <nav> element with the generated TOC. -->
    <xsl:template match="xhtml:nav">
        <nav data-type="toc">
            <xsl:copy-of select="xhtml:h1"/>
            <ol>
                <xsl:apply-templates select="/xhtml:html/xhtml:body/xhtml:div[@data-type='part']" mode="toc"/>
                <xsl:apply-templates select="/xhtml:html/xhtml:body/xhtml:section[@data-type='chapter']" mode="toc"/>
                <xsl:apply-templates select="/xhtml:html/xhtml:body/xhtml:section[contains('appendix glossary bibliography', @data-type)]" mode="toc"/>
            </ol>
        </nav>
    </xsl:template>

</xsl:stylesheet>
