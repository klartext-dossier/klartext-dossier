""" Module providing the markdown parser.
"""

import markdown, logging

import mdx.mermaid


COMMON_EXTENSIONS = [
    'markdown.extensions.attr_list', 
    'markdown.extensions.def_list', 
    'markdown.extensions.fenced_code', 
    'markdown.extensions.meta', 
    'markdown.extensions.sane_lists', 
    'markdown.extensions.tables', 
    'customblocks',
    'pymdownx.fancylists',
    'python_markdown_comments',
    'klartext.glossary', 
    'klartext.inline', 
    'mdx.checkbox', 
    'mdx.toc', 
    'mdx.admonition', 
]


EXTENSION_CONFIGS = {
    'customblocks': {
        'generators': {
            'mermaid': mdx.mermaid.mermaid_generator
        }
    }        
}


markdownFileInstance = markdown.Markdown(extensions=COMMON_EXTENSIONS+['mdx.htmlbook'], extension_configs=EXTENSION_CONFIGS)

def processMarkdownFile(md: str) -> str:
    
    """ Converts a markdown file.

        Parses a markdown file with the extensions necessary to create HTMLBook compliant xhtml.

        Args:
            md: The markdown input.

        Returns:
            The markdown file converted to xhtml.
    """

    # do not pass empty content, or the XML parser will fail
    if len(md.strip()) == 0:    
        md = '<!-- -->'

    return markdownFileInstance.reset().convert(md)


markdownContentInstance = markdown.Markdown(extensions=COMMON_EXTENSIONS+['mdx.xhtml'], extension_configs=EXTENSION_CONFIGS)

def processMarkdownContent(md: str) -> str:

    """ Converts markdown content.

        Parses markdown content with the extensions necessary to create a segment of HTMLBook compliant xhtml. 

        Args:
            md: The markdown input.

        Returns:
            The markdown content converted to xhtml.
    """

    return markdownContentInstance.reset().convert(md)
