import markdown

import mdx.dossier.diagrams


COMMON_EXTENSIONS = [
    'markdown.extensions.attr_list', 
    'markdown.extensions.def_list', 
    'markdown.extensions.fenced_code', 
    'markdown.extensions.meta', 
    'markdown.extensions.sane_lists', 
    'markdown.extensions.tables', 
    'customblocks',
    'mdx.dossier.admonition', 
    'mdx.dossier.checkbox', 
    'mdx.dossier.glossary', 
    'mdx.dossier.inline_tags',
    'mdx.dossier.outline', 
    'mdx.dossier.template_host', 
    'mdx.dossier.template_meta', 
    'mdx.dossier.template_net', 
    'mdx.dossier.toc', 
    'mdx.dossier.grid_tables',
    'python_markdown_comments',
    'pymdownx.fancylists'
]


EXTENSION_CONFIGS = {
    'customblocks': {
        'generators': {
            'mermaid': mdx.dossier.diagrams.mermaid_generator
        }
    }        
}


markdownInstance = markdown.Markdown(extensions=COMMON_EXTENSIONS+['mdx.dossier.xhtml_document', 'mdx.dossier.docbook_structure'], extension_configs=EXTENSION_CONFIGS)

def processMarkdown(md):

    return markdownInstance.reset().convert(md)


markdownContentInstance = markdown.Markdown(extensions=COMMON_EXTENSIONS+['mdx.dossier.xhtml_namespace'], extension_configs=EXTENSION_CONFIGS)

def processMarkdownContent(md):
    
    return markdownContentInstance.reset().convert(md)
