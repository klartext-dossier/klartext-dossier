import io, logging, os, pathlib

from lxml import etree, ElementInclude

from dm.exceptions import TaskException
from dm.utilities import tryLocatingToolsFile

from dm.tasks.Task import Task


def include_loader(href, parse, encoding=None, parser=None): 
    ref = href
    if '/:/' in href:
        if os.path.exists(os.path.join(os.path.curdir, os.path.basename(href))):
            ref = os.path.join(os.path.curdir, os.path.basename(href))
    return ElementInclude._lxml_default_loader(ref, parse, encoding, parser)


class TransformTask(Task):

    """ The xml-transform task.

        Transforms an XML document with an XSLT transformation.
    """

    def tryLoadingStylesheet(self, schema):
        try:
            with open(schema, 'r') as xsltfile:
                return etree.XSLT(etree.parse(xsltfile))
        except Exception as e:
            logging.error(f'{self.name} - cannot parse stylesheet file "{schema}"')            
            logging.error(f'{self.name} - {str(e)}')            
            raise

    def tryParsingXMLContent(self):
        try:
            xml = self.content.getXML()

            # TODO: Add this to all other tryParsingXMLContent methods!
            baseurl = None
            if len(self.input.filename) > 0:
                baseurl = pathlib.Path(os.path.abspath(self.input.filename)).as_posix()
            logging.debug(f'{self.name} - try resolving xincludes; base_url={baseurl}')
            ElementInclude.include(xml, loader=include_loader, base_url=baseurl)
            
            return xml
        except Exception as e:
            raise TaskException(f'{self.name} - cannot parse input file', e)   

    def run(self, context):
        self.stylesheets = self.getElement('stylesheet', multiple=True, required=True)
        self.load()
        for xslt_filename in self.stylesheets:
            xslt_file = tryLocatingToolsFile(xslt_filename, 'xslt', context.toolsdir())
            xslt = self.tryLoadingStylesheet(xslt_file)
            xml = self.tryParsingXMLContent()
            logging.info(f'{self.name} - applying transformation "{xslt_filename}"')
            self.content.data = io.BytesIO(xslt(xml))
            for entry in xslt.error_log:
                logging.error(entry)            
        self.save()

