import logging, importlib


class TaskFactory:

    TASKS = {

        # Name,                 Class,                   Input,      Output,     Children,                           Attributes
        'code-highlight':     ( "CodeHighlightTask",     False,      False,      ['input', 'output'],                [] ),
        'copy':               ( "CopyTask",              True,       True,       ['input', 'output'],                [] ),
        'diagram-to-svg':     ( "DiagramTask",           None,       None,       ['input', 'output', 'stylesheet'],  [] ),
        'dump':               ( "DumpTask",              False,      None,       ['input'],                          [] ),
        'embed-svg':          ( "EmbedTask",             False,      None,       ['input'],                          [] ),
        'file':               ( "FileTask",              None,       False,      ['output'],                         [] ),
        'include':            ( "IncludeTask",           None,       False,      ['input', 'output'],                ['root'] ),
        'if':                 ( "IfTask",                None,       None,       None,                               ['test'] ),
        'klartext-to-xml':    ( "KlartextTask",          False,      False,      ['input', 'output'],                [] ),
        'load':               ( "LoadTask",              True,       None,       ['input'],                          [] ),
        'markdown-include':   ( "MarkdownIncludeTask",   False,      False,      ['input', 'output'],                [] ),
        'markdown-to-xhtml':  ( "MarkdownTask",          False,      False,      ['input', 'output'],                [] ),
        'pdf-to-png':         ( "PDFiumTask",            False,      False,      ['input', 'output'],                ['pattern', 'dpi', 'single'] ),
        'pngs-to-pptx':       ( "PowerPointTask",        False,      False,      ['input', 'output'],                [] ),
        'save':               ( "SaveTask",              None,       True,       ['output'],                         [] ),
        'sequence':           ( "SequenceTask",          None,       None,       None,                               [] ),      
        'xml-tidy':           ( "TidyXMLTask",           False,      False,      ['input', 'output', 'option'],      [] ),
        'xhtml-to-docx':      ( "DocxTask",              False,      False,      ['input', 'output', 'template'],    ['base-url'] ),
        'xhtml-to-pdf':       ( "PDFTask",               False,      False,      ['input', 'output', 'stylesheet'],  ['presentational-hints', 'base-url'] ),
        'xml-transform':      ( "TransformTask",         False,       None,      ['input', 'output', 'stylesheet'],  [] ),
        'xml-validate':       ( "ValidateTask",          False,      None,       ['input', 'schema'],                [] ),
    }

    module = importlib.import_module('dm.tasks')


    def createTask(element, name):

        logging.debug(f'Creating task "{name}"')

        task_class, input_required, output_required, allowed_children, allowed_attributes = TaskFactory.TASKS[name]

        task = getattr(TaskFactory.module, task_class)(element, name)
        
        if allowed_children is not None:
            task.checkAllowedElements(element, allowed_children)
        
        if allowed_attributes is not None:
            task.checkAllowedAttributes(element, allowed_attributes)

        if input_required is not None:
            task.getInputDocument(required=input_required)

        if output_required is not None:
            task.getOutputDocument(required=output_required)

        return task

