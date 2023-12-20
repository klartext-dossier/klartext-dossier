import markdown, python_markdown_comments
import mdx.dossier.mdx_grid_tables
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
    mdx.dossier.mdx_grid_tables.GridTableExtension(),
    python_markdown_comments.CommentsExtension()
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

    # convert empty input into a comment
    if len(md.strip()) == 0:    
        md = '<!-- -->'
    
    # convert markdown to xhtml
    return markdownInstance.reset().convert(md)


markdownContentInstance = markdown.Markdown(extensions=COMMON_EXTENSIONS+['mdx.dossier.xhtml_namespace'], extension_configs=EXTENSION_CONFIGS)

def processMarkdownContent(md, plain=False):
    
    # return quoted one-line content unmodified (with the quotes removed)
    if plain:
        if md.startswith('"') and md.endswith('"'):
            return md[1:-1]

    # convert markdown to xhtml
    return markdownContentInstance.reset().convert(md)
