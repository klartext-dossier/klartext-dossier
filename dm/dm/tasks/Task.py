""" Module providing the base task.
"""

import io, logging, os
from typing import List 
from lxml import etree

from dm.exceptions import TaskException
from dm.tasks.Content import Content


class File:

    def __init__(self) -> None:
        self.filename : str = ''
        self.encoding : str|None = None


class Task:

    """ The base class for tasks.

        This class provides the basic functions shared by all tasks.
    """

    def __init__(self, element: etree._Element, name: str) -> None:

        """ Initializer.

            Args:
                element: The xml element instantiating the task.
                name:    The name of the task.
        """

        self.element = element
        self.name = name

        self.input = File()
        self.content = Content()
        self.output = File()

        logging.debug(f'{self.name} - init')

    def basedir(self) -> str | None:

        """ The base directory.

            If an input file is used by the task, the base directory is the path to the input file.

            Returns:
                The base directory of the task, or None if no input file is used.
        """

        if len(self.input.filename) > 0:
            return os.path.dirname(self.input.filename)
        
        return None


    def getAttribute(self, attribute: str, required: bool = False, default: str|None = None) -> str | None:

        """ Get a task attribute.

            Args:
                attribute: The name of the attribute to retrieve.
                required:  Indicates that the attribute is required.
                default:   The default value of the attribute.

            Returns:
                The value of the attribute, if avaiable. Otherwise, the default value is returned.

            Raises:
                TaskException: if the attribute is not defined, no default value has been provided, but the attribute is required.
        """

        value = self.element.get(attribute, default)
        if required and value is None:
            raise TaskException(f'{self.name} - required attribute "{attribute}" not set')
        logging.debug(f'{self.name} - "{attribute}" set to "{value}"!')
        return value


    def checkNumberOfElements(self, name: str, multiple: bool, required: bool) -> None:
        
        """ Checks whether the correct number of child elements are provided.

            Args:
                name:     The name of the child elements to check.
                multiple: Indicates that the child element may be provided multiple times.
                required: Indicates that the child element has to be provided at least once.

            Raises:
                TaskException: if an incorrect number of child elements is provided.
        """

        nr = len(self.element.findall(name))
        if 0 == nr and required:
            raise TaskException(f'{self.name} - requires element "{name}" not set')
        if nr>1 and not multiple:
            raise TaskException(f'{self.name} - "{name}" can only be defined once')


    def getElement(self, name : str, required: bool = False) -> str | None: 

        """ Get a task subelement.

            Args:
                name:     The name of the subelement to retrieve.
                required: Indicates that the subelement is required.

            Returns:
                The value of the subelement, if avaiable. Otherwise, None will be returned.

            Raises:
                TaskException: if the subelement is not defined, but the subelement is required.
        """

        self.checkNumberOfElements(name, False, required)

        text = self.element.findtext(name)
        if required and not text:
            raise TaskException(f'{self.name} - required element "{name}" not set')
        if text:
            text=text.strip()
        logging.debug(f'{self.name} - "{name}" set to "{text}"!')
        return text


    def getMultipleElements(self, name: str, required: bool = False) -> List[str]: 

        """ Get a task's subelements.

            Args:
                name:     The name of the subelements to retrieve.
                required: Indicates that the subelement is required.

            Returns:
                A list of the values of the subelements. Can be an empty list if no subelements are available.

            Raises:
                TaskException: if the subelement is not defined, but the subelement is required.
        """

        self.checkNumberOfElements(name, True, required)

        value = []
        for child in self.element.findall(name):
            if child.text:
                value.append(child.text.strip())
        if required and 0 == len(value):
            raise TaskException(f'{self.name} - requires element "{name}" not set')
        logging.debug(f'{self.name} - "{name}" set to "{value}"!')
        return value


    def checkInputDocument(self, required : bool = False):

        """ Checks a task's input document.

            Args:
                required: Indicates that the input document is required.

            Raises:
                TaskException: if the input document is required, but not provided
        """

        self.checkNumberOfElements('input', multiple=False, required=required)

        child = self.element.find('input')        
        if child is not None and child.text:
            self.checkAllowedAttributes(child, ['encoding'])
            self.input.filename = child.text.strip()
            self.input.encoding = child.get('encoding', Content.DEFAULT_ENCODING)
            logging.debug(f'{self.name} - "input" set to "{self.input.filename}", encoding="{self.input.encoding}"')


    def checkOutputDocument(self, required : bool = False):

        """ Checks a task's output document.

            Args:
                required: Indicates that the output document is required.

            Raises:
                TaskException: if the output document is required, but not provided
        """

        self.checkNumberOfElements('output', multiple=False, required=required)

        child = self.element.find('output')
        if child is not None and child.text:
            self.checkAllowedAttributes(child, ['encoding'])
            self.output.filename = child.text.strip()
            self.output.encoding = child.get('encoding', None)
            logging.debug(f'{self.name} - "output" set to "{self.output.filename}", encoding="{self.output.encoding}"')


    def checkAllowedElements(self, element : etree._Element, elements : List[str]) -> None:

        """ Checks that only allowed child elements are provided.

            Args:
                element:  The element defining a task.
                elements: The list of allowed element names.

            Raises:
                TaskException: if the element defining a task contains subelements that are not allowed.
        """

        for child in element:
            if child.tag not in elements:
                raise TaskException(f'{self.name} - element "{self.element.tag}" does not allow child "{child.tag}"!')


    def checkAllowedAttributes(self, element : etree._Element, attributes : List[str]) -> None:
 
        """ Checks that only allowed attributes are provided.

            Args:
                element:    The element defining a task.
                attributes: The list of allowed attribute names.

            Raises:
                TaskException: if the element defining a task contains attributes that are not allowed.
        """

        for attribute in element.attrib.keys():
            if attribute not in attributes:
                raise TaskException(f'{self.name} - element "{self.element.tag}" does not allow attribute "{str(attribute)}"!')


    def load(self) -> None:

        """ Loads the input document.

            Raises:
                TaskException: if the input document can not be loaded.
        """
        
        try:
            if len(self.input.filename) > 0:
                with open(self.input.filename, 'rb') as infile:
                    logging.info(f'{self.name} - loading {self.input.filename}')
                    self.content.data = io.BytesIO(infile.read())
                    self.content.encoding = self.input.encoding
        except Exception as e:
             raise TaskException(f'{self.name} - cannot load file "{self.input.filename}"', e)


    def save(self) -> None:

        """ Saves the output document.

            Raises:
                TaskException: if the output document can not be saved.
        """

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
