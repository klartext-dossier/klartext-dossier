""" Module providing the xhtml_document extension for Markdown.

    This code is largely based on the original xhtml_document extension found at: https://github.com/aleray/mdx_outline

    Below is part of the original module comment:

    XHTML Wrap Extension for Python-Markdown
    ========================================

    Adds a XHTML wrapper with an optional page title and CSS URL. Much like Jason
    Blevins' markdown-mode for Emacs (http://jblevins.org/projects/markdown-mode/).

    Copyright (c)2011 [Paul Provost](http://paulprovost.me)

    License: [BSD](http://www.opensource.org/licenses/bsd-license.php)
"""

from string import Template

import markdown


class XHTMLDocumentProcessor(markdown.postprocessors.Postprocessor):

    def run(self, text: str) -> str:

        templates = dict()
        templates['text'] = text
        templates['meta'] = ""

        if hasattr(self.md, 'Meta'):
            if 'title' in self.md.Meta:
                templates['title'] = Template('<title>$title</title>\n').safe_substitute(title=self.md.Meta['title'][0])
            else:
                templates['title'] = "<title> </title>"
            m = ''
            for key, values in self.md.Meta.items():
                m += Template('<meta name="$name" content="$content"/>\n        ').safe_substitute(name=key, content=values[0])
            if m:
                templates['meta'] = m

        doc  = Template('''\
<?xml version="1.0" encoding="UTF-8" ?>

<html xmlns="http://www.w3.org/1999/xhtml">

    <head>
        $title $meta
        <link rel="stylesheet" type="text/css" href="htmlbook.css"/>
    </head>

    <body data-type="book">
        $text
    </body>

</html>''')

        return doc.safe_substitute(templates)


class XHTMLDocumentExtension(markdown.Extension):

    """ Extension for xhtml_document.

        Wraps the document into an htmlbook compatible wrapper.

        Examples:

            The code:

                This is markdown.

            will be converted to:

                <html xmlns="http://www.w3.org/1999/xhtml">
                    <head>
                        <link rel="stylesheet" type="text/css" href="htmlbook.css"/>
                    </head>

                    <body data-type="book">
                        This is markdown.
                    </body>
                </html>
    """

    def extendMarkdown(self, md: markdown.Markdown) -> None:
        
        md.postprocessors.register(XHTMLDocumentProcessor(md), 'xhtml_wrap', 400)


def makeExtension(**kwargs):

    return XHTMLDocumentExtension(**kwargs)
