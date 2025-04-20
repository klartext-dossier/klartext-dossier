import logging, os, pathlib

import tinycss2
import cssselect2

from lxml import etree
from lxml import ElementInclude # type: ignore[attr-defined]

from dm.exceptions import TaskException
from dm.utilities import tryLocatingToolsFile
from dm.tasks.Content import Content
from dm.tasks.Task import Task
from dm.diagram import Diagram


def include_loader(href, parse, encoding=None, parser=None): 
    ref = href
    if '/:/' in href:
        if os.path.exists(os.path.join(os.path.curdir, os.path.basename(href))):
            ref = os.path.join(os.path.curdir, os.path.basename(href))
    return ElementInclude._lxml_default_loader(ref, parse, encoding, parser)


class DiagramTask(Task):

    """ The diagram-to-svg task.

        Transforms a diagram to an SVG element.
    """

    def tryLoadingStylesheet(self, schema):
        try:
            with open(schema, 'r') as cssfile:
                return tinycss2.parse_stylesheet(cssfile.read(), skip_comments=True, skip_whitespace=True)
        except Exception as e:
            raise TaskException(f'{self.name} - cannot parse stylesheet file "{schema}"', e)            


    def tryParsingXMLContent(self):
        try:
            xml = self.content.getXML()
            baseurl = None
            if len(self.input.filename) > 0:
                baseurl = pathlib.Path(os.path.dirname(os.path.abspath(self.input.filename))).as_uri()
            logging.debug(f'{self.name} - try resolving xincludes; base_url={baseurl}')
            ElementInclude.include(xml, loader=include_loader, base_url=baseurl)
            return xml
        except Exception as e:
            raise TaskException(f'{self.name} - cannot parse input file', e)   


    def tryParsingStylesheets(self, context):
        matcher = cssselect2.Matcher()

        for css_filename in self.stylesheets:
            css_file = tryLocatingToolsFile(css_filename, 'css', context.toolsdir())
            css = self.tryLoadingStylesheet(css_file)

            for rule in css:
                selectors = cssselect2.compile_selector_list(rule.prelude)
                selector_string = tinycss2.serialize(rule.prelude)
                content_string = tinycss2.serialize(rule.content)
                payload = (selector_string, content_string)
                for selector in selectors:
                    matcher.add_selector(selector, payload)
        return matcher


    def tryApplyingStylesheets(self, xml, matcher):
        wrapper = cssselect2.ElementWrapper.from_xml_root(xml)
        for element in wrapper.iter_subtree():
            tag = element.etree_element.tag
            if tag.startswith(Diagram.DIAGRAM_NAMESPACE):
                tag = element.etree_element.tag.split('}')[-1]
                logging.debug(f'{self.name} - found tag "{tag}"')

                matches = matcher.match(element)
                if matches:
                    styles = {}
                    for match in matches:
                        _, _, _, payload = match
                        _, content_string = payload
                        for property in content_string.split(';'):
                            pos = property.find(':')
                            if pos > 0:
                                styles[property[:pos].strip()] = property[pos+1:].strip()

                    attr = ''
                    for key, val in styles.items():
                        attr += f'{key}: {val}; '
                    logging.debug(f'{self.name} - computed style "{attr.strip()}"')
                    element.etree_element.set('style', attr.strip())
        return xml


    def tryConvertingToSVG(self, xml, context):

        diagram = Diagram(xml)

        return diagram.toSVG(context)


    def run(self, context):
        self.stylesheets = ['diagram.css']
        self.stylesheets.extend(self.getMultipleElements('stylesheet', required=False))
        self.load()

        matcher = self.tryParsingStylesheets(context)
        xml = self.tryParsingXMLContent()
        xml = self.tryApplyingStylesheets(xml, matcher)
        xml = self.tryConvertingToSVG(xml, context)

        self.content.setData(etree.tostring(xml, encoding=Content.DEFAULT_ENCODING))
        self.content.encoding = Content.DEFAULT_ENCODING

        self.save()

