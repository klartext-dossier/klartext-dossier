import logging, importlib


class TaskFactory:

    TASKS = {

        # Name,                 Class,                   Input,      Output,     Children,                           Attributes
        'code-highlight':     ( "CodeHighlightTask",     False,      False,      ['input', 'output'],                ['name'] ),
        'copy':               ( "CopyTask",              True,       True,       ['input', 'output'],                ['name'] ),
        'diagram-to-svg':     ( "DiagramTask",           None,       None,       ['input', 'output', 'stylesheet'],  ['name'] ),
        'dump':               ( "DumpTask",              False,      None,       ['input'],                          ['name'] ),
        'embed-svg':          ( "EmbedTask",             False,      None,       ['input'],                          ['name'] ),
        'file':               ( "FileTask",              None,       False,      ['output'],                         ['name'] ),
        'include':            ( "IncludeTask",           None,       False,      ['input', 'output'],                ['name', 'root'] ),
        'if':                 ( "IfTask",                None,       None,       None,                               ['name', 'test'] ),
        'klartext-to-xml':    ( "KlartextTask",          False,      False,      ['input', 'output'],                ['name'] ),
        'load':               ( "LoadTask",              True,       None,       ['input'],                          ['name'] ),
        'markdown-include':   ( "MarkdownIncludeTask",   False,      False,      ['input', 'output'],                ['name'] ),
        'markdown-to-xhtml':  ( "MarkdownTask",          False,      False,      ['input', 'output'],                ['name'] ),
        'pdf-to-png':         ( "PDFiumTask",            False,      False,      ['input', 'output'],                ['name', 'pattern', 'dpi', 'single'] ),
        'pngs-to-pptx':       ( "PowerPointTask",        False,      False,      ['input', 'output'],                ['name'] ),
        'save':               ( "SaveTask",              None,       True,       ['output'],                         ['name'] ),
        'sequence':           ( "SequenceTask",          None,       None,       None,                               ['name'] ),      
        'xml-tidy':           ( "TidyXMLTask",           False,      False,      ['input', 'output', 'option'],      ['name'] ),
        'xhtml-to-docx':      ( "DocxTask",              False,      False,      ['input', 'output', 'template'],    ['name', 'base-url'] ),
        'xhtml-to-pdf':       ( "PDFTask",               False,      False,      ['input', 'output', 'stylesheet'],  ['name', 'presentational-hints', 'base-url'] ),
        'xml-transform':      ( "TransformTask",         False,       None,      ['input', 'output', 'stylesheet'],  ['name'] ),
        'xml-validate':       ( "ValidateTask",          False,      None,       ['input', 'schema'],                ['name'] ),
    }

    module = importlib.import_module('dm.tasks')


    def createTask(element, name):

        logging.debug(f'Creating task "{name}"')

        task_class, input_required, output_required, allowed_children, allowed_attributes = TaskFactory.TASKS[name]

        task = getattr(TaskFactory.module, task_class)(element, name)
        
        # TODO: Split into two methods to allow checking seperately!
        if (allowed_children is not None) and (allowed_attributes is not None):
            task.checkAllowed(element, allowed_children, allowed_attributes)

        if input_required is not None:
            task.getInputDocument(required=input_required)

        if output_required is not None:
            task.getOutputDocument(required=output_required)

        return task

