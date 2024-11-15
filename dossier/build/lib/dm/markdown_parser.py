import markdown

import mdx.diagrams


COMMON_EXTENSIONS = [
    'markdown.extensions.attr_list', 
    'markdown.extensions.def_list', 
    'markdown.extensions.fenced_code', 
    'markdown.extensions.meta', 
    'markdown.extensions.sane_lists', 
    'markdown.extensions.tables', 
    'customblocks',
    'mdx.glossary', 
    'mdx.inline_tags',
    'mdx.template_host', 
    'mdx.template_meta', 
    'mdx.template_net', 
    'mdx.checkbox', 
    'mdx.dossier.outline', 
    'mdx.dossier.toc', 
    'mdx.dossier.grid_tables',
    'mdx.dossier.admonition', 
    'python_markdown_comments',
    'pymdownx.fancylists',
    'pymdownx.smartsymbols'
]


EXTENSION_CONFIGS = {
    'customblocks': {
        'generators': {
            'mermaid': mdx.diagrams.mermaid_generator
        }
    }        
}


markdownInstance = markdown.Markdown(extensions=COMMON_EXTENSIONS+['mdx.dossier.xhtml_document', 'mdx.docbook_structure'], extension_configs=EXTENSION_CONFIGS)

def processMarkdown(md):

    return markdownInstance.reset().convert(md)


markdownContentInstance = markdown.Markdown(extensions=COMMON_EXTENSIONS+['mdx.xhtml_namespace'], extension_configs=EXTENSION_CONFIGS)

def processMarkdownContent(md):
    
    return markdownContentInstance.reset().convert(md)
