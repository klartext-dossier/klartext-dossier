import logging, xmlschema

from dm.exceptions import TaskException
from dm.utilities import tryLocatingToolsFile
from dm.tasks.Task import Task


class ValidateTask(Task):

    """ The xml-validate task.

        Validates an XML document against XSD schema files.
    """

    def tryLoadingSchema(self, schema):
        try:
            return xmlschema.XMLSchema(schema)                    
        except Exception as e:
            raise TaskException(f'{self.name} - cannot parse schema file "{schema}"', e)
        
    def tryValidatingXML(self, schema, xml):
        try:
            schema.validate(xml)
        except xmlschema.XMLSchemaValidationError as e:
            logging.error(f'{self.name} - invalid XML:{e}')
            raise

    def run(self, context):
        self.schemas = self.getMultipleElements('schema', required=True)
        self.load()
        for schema_filename in self.schemas:
            schema_file = tryLocatingToolsFile(schema_filename, 'xsd', context.toolsdir())
            schema = self.tryLoadingSchema(schema_file)
            xml = self.content.getXML()
            self.tryValidatingXML(schema, xml)
            logging.info(f'{self.name} - XML file is valid')
