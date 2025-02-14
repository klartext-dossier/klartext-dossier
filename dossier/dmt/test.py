import os, difflib

from diff_pdf_visually import pdfdiff

import dm.context, dm.pipeline, dm.utilities


def run_conversion_pipeline(input, input_format, output_format, options):

    context = dm.context.Context(toolsdir=options['toolsdir'])
    context.set_flags(['validate'])
    pipeline_file = dm.utilities.tryLocatingToolsFile(f'{input_format}-to-{output_format}.dm', 'pipeline', options['toolsdir'])
    
    if len(pipeline_file) > 0:
        context.set_basedir(os.path.dirname(pipeline_file))

    with open(pipeline_file, 'r', encoding="utf-8") as pipe:
        with context:
            pipeline = dm.pipeline.Pipeline(pipe)
            task = pipeline.run(input, 'utf-8', None, None, context)
        return task.content.data


def compare_bytes(a, b):

    diff = list(difflib.diff_bytes(difflib.unified_diff, a.readlines(), b.readlines()))
    
    return (len(diff) == 0, diff)


def compare_pdf(a, b):
    
    return pdfdiff(a, b, verbosity=0), []


def compare_text(a, b):

    diff = list(difflib.unified_diff(a.readlines(), b.readlines())) 
    
    return (len(diff) == 0, diff)


def compare_md(a, b):

    list_a = [ line.decode('utf-8').rstrip() for line in a.readlines() ]
    list_b = [ line.decode('utf-8').rstrip() for line in b.readlines() ]

    diff = list(difflib.unified_diff(list_a, list_b))    
    return (len(diff) == 0, diff)


def compare_html(a, b):

    list_a = [ line.decode('utf-8').rstrip() for line in a.readlines() ]
    list_b = [ line.decode('utf-8').rstrip() for line in b.readlines() ]

    diff = list(difflib.unified_diff(list_a, list_b))    
    return (len(diff) == 0, diff)


def compare_xml(a, b):

    list_a = [ line.decode('utf-8').rstrip() for line in a.readlines() ]
    list_b = [ line.decode('utf-8').rstrip() for line in b.readlines() ]

    diff = list(difflib.unified_diff(list_a, list_b))    
    return (len(diff) == 0, diff)


COMPARATORS = {
    'html':     compare_html,
    'md':       compare_md,
    'pdf':      compare_pdf,
    'xml':      compare_xml
}