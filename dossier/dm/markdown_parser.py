import markdown

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
    'mdx.outline', 
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


markdownInstance = markdown.Markdown(extensions=COMMON_EXTENSIONS+['mdx.xhtml_document', 'mdx.htmlbook'], extension_configs=EXTENSION_CONFIGS)

def processMarkdown(md: str) -> str:

    return markdownInstance.reset().convert(md)


markdownContentInstance = markdown.Markdown(extensions=COMMON_EXTENSIONS+['mdx.xhtml'], extension_configs=EXTENSION_CONFIGS)

def processMarkdownContent(md: str) -> str:
    
    return markdownContentInstance.reset().convert(md)
