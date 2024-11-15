import logging, tempfile

from lxml import etree
from cairosvg import svg2png

from dm.exceptions import TaskException
from dm.tasks.Content import Content
from dm.tasks.Task import Task
from dm.diagram import Diagram


class EmbedTask(Task):

    """ The embed-svg task.

        Embeds SVG elements.
    """

    def tryParsingXMLContent(self):
        try:
            xml = self.content.getXML()
            return xml
        except Exception as e:
            raise TaskException(f'{self.name} - cannot parse input file', e)   


    def tryEmbeddingSVG(self, xml, context):
        for svg in xml.iter(Diagram.SVG_NAMESPACE+'svg'):

            png = tempfile.NamedTemporaryFile(suffix='.png')
            context.add_tempfile(png.name, png)
            logging.debug(f'{self.name} - embedding SVG element to {png.name}')

            svg2png(bytestring=etree.tostring(svg, encoding='utf-8'), write_to=png)
            png.seek(0)

            img = etree.Element('img')
            img.set('alt', svg.get('name', 'image'))
            img.set('src', png.name)

            svg.getparent().replace(svg, img)

        return xml


    def run(self, context):
        self.load()

        xml = self.tryParsingXMLContent()
        xml = self.tryEmbeddingSVG(xml, context)

        self.content.setData(etree.tostring(xml, encoding=Content.DEFAULT_ENCODING))
        self.content.encoding = Content.DEFAULT_ENCODING

        self.save()

