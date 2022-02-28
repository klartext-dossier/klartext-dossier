import logging

from tidylib import tidy_document
from dm.exceptions import TaskException
from dm.tasks.Task import Task


class TidyXMLTask(Task):

    """ The tidy-xml task.

        Pretty-prints an XML file.
    """

    TIDY_OPTIONS = {
        'numeric-entities': True,
        'quiet': True,
        'add-meta-charset': True,
        'add-xml-decl': True,
        'input-xml': True,
        'output-xml': True,
        'coerce-endtags': True,
        'sort-attributes': 'alpha',
        'tidy-mark': True,
        'vertical-space': False,
        'wrap': 0,
        'indent': 'no',
        'doctype': 'omit',
        'quote-ampersand': False,
        'new-inline-tags': "g,ref"
    }

    def tryParseOptions(self):
        options = self.TIDY_OPTIONS       
        for option in self.element.iterfind('option'):
            self.checkAllowed(option, elements=[], attributes=['name', 'value'])
            name = option.get('name', None)
            value = option.get('value', None)
            if name is None:
                raise TaskException(f'{self.name} - option requires a "name" attribute!')
            if value is None:
                raise TaskException(f'{self.name} - option "{name}" requires a value!')
            logging.debug(f'{self.name} - setting tidy option "{name}" to "{value}"')
            options[name] = value
        return options

    def run(self, context):
        self.load()

        options = self.tryParseOptions()
        
        pretty, errors = tidy_document(self.content.getText(), options)

        if errors:
            logging.error(errors)
            raise TaskException(f'{self.name} - cannot pretty-print XML content!')

        self.content.setText(pretty)

        self.save()

