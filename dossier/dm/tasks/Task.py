import io, logging, os

from dm.exceptions import TaskException
from dm.tasks.Content import Content


class File:

    def __init__(self):
        self.filename = ''
        self.encoding = None


class Task:

    """ The base class for tasks.

        This class provides the basic functions shared by all tasks.
    """

    def __init__(self, element, name):
        self.element = element
        self.name = name

        self.input = File()
        self.content = Content()
        self.output = File()

        logging.debug(f'{self.name} - init')

    def basedir(self):
        if len(self.input.filename) > 0:
            return os.path.dirname(self.input.filename)
        return None

    def getAttribute(self, attribute, required=False, default=None):
        value = self.element.get(attribute, default)
        if required and value is None:
            raise TaskException(f'{self.name} - required attribute "{attribute}" not set')
        logging.debug(f'{self.name} - "{attribute}" set to "{value}"!')
        return value

    def checkNumberOfElements(self, name, multiple, required):
        nr = len(self.element.findall(name))
        if 0 == nr and required:
            raise TaskException(f'{self.name} - requires element "{name}" not set')
        if nr>1 and not multiple:
            raise TaskException(f'{self.name} - "{name}" can only be defined once')

    def getElement(self, name, required=False, multiple=False, default=None, attribute=None):
        # TODO: Fix handling of default value (which currently is never returned)
        self.checkNumberOfElements(name, multiple, required)
        if multiple:
            value = []
            for child in self.element.findall(name):
                if attribute is None:
                    value.append(child.text.strip())
                else:
                    value.append(child.get(attribute))
            if required and 0 == len(value):
                raise TaskException(f'{self.name} - requires element "{name}" not set')
            logging.debug(f'{self.name} - "{name}" set to "{value}"!')
            return value
        else:
            value = self.element.findtext(name)
            if required and not value:
                raise TaskException(f'{self.name} - required element "{name}" not set')
            if value:
                value=value.strip()
            logging.debug(f'{self.name} - "{name}" set to "{value}"!')
            return value
        return default

    def getInputDocument(self, required=False):
        self.checkNumberOfElements('input', multiple=False, required=required)

        child = self.element.find('input')        
        if child is not None:
            self.checkAllowedAttributes(child, ['encoding'])
            self.input.filename = child.text.strip()
            self.input.encoding = child.get('encoding', Content.DEFAULT_ENCODING)
            logging.debug(f'{self.name} - "input" set to "{self.input.filename}", encoding="{self.input.encoding}"')

    def getOutputDocument(self, required=False):
        self.checkNumberOfElements('output', multiple=False, required=required)

        child = self.element.find('output')
        if child is not None:
            self.checkAllowedAttributes(child, ['encoding'])
            self.output.filename = child.text.strip()
            self.output.encoding = child.get('encoding', None)
            logging.debug(f'{self.name} - "output" set to "{self.output.filename}", encoding="{self.output.encoding}"')

    def checkAllowedElements(self, element, elements):
        for child in element:
            if child.tag not in elements:
                raise TaskException(f'{self.name} - element "{self.element.tag}" does not allow child "{child.tag}"!')

    def checkAllowedAttributes(self, element, attributes):
        for attribute in element.attrib.keys():
            if attribute not in attributes:
                raise TaskException(f'{self.name} - element "{self.element.tag}" does not allow attribute "{attribute}"!')

    def load(self):
        try:
            if len(self.input.filename) > 0:
                with open(self.input.filename, 'rb') as infile:
                    logging.info(f'{self.name} - loading {self.input.filename}')
                    self.content.data = io.BytesIO(infile.read())
                    self.content.encoding = self.input.encoding
        except Exception as e:
             raise TaskException(f'{self.name} - cannot load file "{self.input.filename}"', e)

    def save(self):
        try:
            if len(self.output.filename) > 0:
                with open(self.output.filename, 'wb') as outfile:
                    if self.output.encoding is None:
                        self.output.encoding = self.content.encoding
                    logging.info(f'{self.name} - saving {self.output.filename}, encoding="{self.output.encoding}"')
                    if self.output.encoding == self.content.encoding:                    
                        outfile.write(self.content.data.getvalue())
                    else:
                        outfile.write(self.content.data.getvalue().decode(self.content.encoding).encode(self.output.encoding))

        except Exception as e:
             raise TaskException(f'{self.name} - cannot save file "{self.output.filename}"', e)
