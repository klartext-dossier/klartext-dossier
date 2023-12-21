import logging

from lxml import etree

from dm.utilities import tryLocatingToolsFile


class Diagram:

    DIAGRAM_NAMESPACE = '{http://www.hoelzer-kluepfel.de/diagram}'
    SVG_NAMESPACE = '{http://www.w3.org/2000/svg}'
    XHTML_NAMESPACE = '{http://www.w3.org/1999/xhtml}'

    def __init__(self, xml):
        self.xml = xml


    def toPixels(self, value, dpi):
        if value.endswith('cm'):
            return int(int(value[:-2])*dpi*100/254)
        else:
            return int(value)


    def relativeSize(self, value, base):
        value = value.strip()
        if value.endswith('%'):
            value = float(value[:-1]) * base / 100.0
        return int(value)


    def isTextStyle(self, key):
        # TODO: add complete list
        return key.startswith('text-') or key.startswith('font-') or ('dominant-baseline' == key)

    
    def isDrawStyle(self, key):
        # TODO: add complete list
        return key in ['stroke', 'fill', 'stroke-width', 'filter', 'stroke-dasharray', 'marker-end', 'marker-start', 'rx', 'ry']


    def textStyles(self, element):

        ts = dict()

        for entry in element.get('style', '').split(';'):
            if ':' in entry:
                key, value = entry.split(':', maxsplit=1)
                key = key.strip()
                value = value.strip()
                if self.isTextStyle(key):
                    ts[key] = value
                
        for key, value in element.items():
            if self.isTextStyle(key):
                ts[key] = value
                del element.attrib[key]

        if not 'font-size' in ts:
            ts['font-size'] = '16px'
        if not 'text-anchor' in ts:
            ts['text-anchor'] = 'middle'
        if not 'dominant-baseline' in ts:
            ts['dominant-baseline'] = 'middle'

        return ts


    def drawStyles(self, element):

        es = dict()

        for entry in element.get('style', '').split(';'):
            if ':' in entry:
                key, value = entry.split(':', maxsplit=1)
                key = key.strip()
                value = value.strip()
                if self.isDrawStyle(key):
                    es[key] = value
                
        for key, value in element.items():
            if self.isDrawStyle(key):
                if key in ['marker-end', 'marker-start']:
                    if not value.startswith('url(#'):
                        value = f'url(#{value})'
                es[key] = value
                del element.attrib[key]

        return es


    def joinStyles(self, styles):
        style = ''
        for key, value in styles.items():
            style += f'{key}:{value};'
        
        return style


    def extractGeometry(self, element, child, width, height):

        geo = dict()
        for key, value in element.items():
            if key in ['width', 'left', 'right', 'center', 'x1', 'x2', 'x']:
                geo[key] = self.relativeSize(value, width)
            elif key in ['height', 'top', 'bottom', 'middle', 'y1', 'y2', 'y', 'r']:
                geo[key] = self.relativeSize(value, height)
            else:
                child.set(key, value)

        return geo


    def checkRectGeometry(self, geo):
        
        if 'left' in geo:
            if 'width' in geo:
                geo['x'] = geo['left']
            elif 'right' in geo:
                geo['x'] = min(geo['left'], geo['right'])
                geo['width'] = abs(geo['right'] - geo['left'])
        elif 'right' in geo:
            if 'width' in geo:
                geo['x'] = geo['right'] - geo['width']
        elif 'center' in geo:
            if 'width' in geo:
                geo['x'] = geo['center'] - geo['width'] / 2
            
        if 'top' in geo:
            if 'height' in geo:
                geo['y'] = geo['top']
            elif 'bottom' in geo:
                geo['y'] = min(geo['top'], geo['bottom'])
                geo['height'] = abs(geo['bottom'] - geo['top'])
        elif 'bottom' in geo:
            if 'height' in geo:
                geo['y'] = geo['bottom'] - geo['height']
        elif 'middle' in geo:
            if 'height' in geo:
                geo['y'] = geo['middle'] - geo['height'] / 2
        
        # TODO: check for invalid geometry

        return geo
        

    def setRectGeometry(self, element, child, width, height, offset_x, offset_y):
        
        geo = self.extractGeometry(element, child, width, height)
        geo = self.checkRectGeometry(geo)
           
        x = geo['x'] + offset_x
        y = geo['y'] + offset_y
        w = geo['width']
        h = geo['height']

        child.set('x', str(x))
        child.set('y', str(y))
        child.set('width', str(w))
        child.set('height', str(h))

        return (x, y, w, h)


    def checkLineGeometry(self, geo):

        if 'x1' in geo:
            if 'x2' not in geo:
                geo['x2'] = geo['x1']
        if 'x2' in geo:
            if 'x1' not in geo:
                geo['x1'] = geo['x2']
            
        if 'y1' in geo:
            if 'y2' not in geo:
                geo['y2'] = geo['y1']
        if 'y2' in geo:
            if 'y1' not in geo:
                geo['y1'] = geo['y2']
            
        # TODO: check for invalid geometry

        return geo


    def setLineGeometry(self, element, child, width, height, offset_x, offset_y):

        geo = self.extractGeometry(element, child, width, height)
        geo = self.checkLineGeometry(geo)
           
        x1 = geo['x1'] + offset_x
        y1 = geo['y1'] + offset_y
        x2 = geo['x2'] + offset_x
        y2 = geo['y2'] + offset_y

        child.set('x1', str(x1))
        child.set('y1', str(y1))
        child.set('x2', str(x2))
        child.set('y2', str(y2))

        return (x1, y1, x2, y2)


    def checkCircleGeometry(self, geo):

        if 'x' in geo:
            geo['cx'] = geo['x']
            
        if 'y' in geo:
            geo['cy'] = geo['y']
            
        # TODO: check for invalid geometry

        return geo


    def setCircleGeometry(self, element, child, width, height, offset_x, offset_y):

        geo = self.extractGeometry(element, child, width, height)
        geo = self.checkCircleGeometry(geo)
           
        cx = geo['cx'] + offset_x
        cy = geo['cy'] + offset_y
        r = geo['r'] + offset_x

        child.set('cx', str(cx))
        child.set('cy', str(cy))
        child.set('r', str(r))

        return (cx, cy, r)


    def checkTextGeometry(self, geo):
        
        if 'left' in geo:
            geo['x'] = geo['left']
        elif 'right' in geo:
            geo['x'] = geo['right']
        elif 'center' in geo:
            geo['x'] = geo['center']
            
        if 'top' in geo:
            geo['y'] = geo['top']            
        elif 'bottom' in geo:
            geo['y'] = geo['bottom']
        elif 'middle' in geo:
            geo['y'] = geo['middle']
        
        # TODO: check for invalid geometry

        return geo


    def setTextGeometry(self, element, child, width, height, offset_x, offset_y):

        geo = self.extractGeometry(element, child, width, height)
        geo = self.checkTextGeometry(geo)
           
        x = geo['x'] + offset_x
        y = geo['y'] + offset_y

        child.set('x', str(x))
        child.set('y', str(y))

        return (x, y)


    def appendChildren(self, svg, diagram, offset_x, offset_y, width, height):
        for element in diagram.iterchildren(self.DIAGRAM_NAMESPACE+'*'):
            tag = element.tag.split(self.DIAGRAM_NAMESPACE)[-1]

            t = None
            if 'rect' == tag:
                child = etree.Element(self.SVG_NAMESPACE+'rect')
                child_x, child_y, child_w, child_h = self.setRectGeometry(element, child, width, height, offset_x, offset_y)
                child.set('style', self.joinStyles(self.drawStyles(child)))
                text = element.get('text', '')
                if len(text) > 0:
                    del element.attrib['text']
                    t = etree.Element(self.SVG_NAMESPACE+'text')
                    t.set('x', str(child_x + child_w/2))
                    t.set('y', str(child_y + child_h/2))
                    t.set('style', self.joinStyles(self.textStyles(element)))                
                    t.text = text
            elif 'line' == tag:
                child = etree.Element(self.SVG_NAMESPACE+'line')
                self.setLineGeometry(element, child, width, height, offset_x, offset_y)
                child.set('style', self.joinStyles(self.drawStyles(child)))
            elif 'circle' == tag:
                child = etree.Element(self.SVG_NAMESPACE+'circle')
                (child_x, child_y, _) = self.setCircleGeometry(element, child, width, height, offset_x, offset_y)
                child.set('style', self.joinStyles(self.drawStyles(child)))
                text = element.get('text', '')
                if len(text) > 0:
                    del element.attrib['text']
                    t = etree.Element(self.SVG_NAMESPACE+'text')
                    t.set('x', str(child_x))
                    t.set('y', str(child_y))
                    t.set('style', self.joinStyles(self.textStyles(element)))                
                    t.text = text
            elif 'text' == tag:
                child = etree.Element(self.SVG_NAMESPACE+'text')
                child_x, child_y = self.setTextGeometry(element, child, width, height, offset_x, offset_y)
                child.set('x', str(child_x))
                child.set('y', str(child_y))
                child.set('style', self.joinStyles(self.textStyles(element)))                
                child.text = element.get('text', '')
            else:
                logging.warn(f'diagram - ignoring invalid element "{tag}"')
                continue


            # append svg elements
            svg.append(child)
            if t is not None:
                svg.append(t)                    

            # allow nested elements
            if 'rect' == tag:
                self.appendChildren(svg, element, child_x, child_y, child_w, child_h)


    def includeStandardDefs(self, svg, context):

        svg_file = tryLocatingToolsFile('diagram-defs.svg', 'svg', context.tools_dir())
        logging.debug(f'diagram - including diagram definitions from "{svg_file}"')
        xml = etree.parse(svg_file, parser=etree.XMLParser())

        svg.append(xml.getroot())


    def toSVG(self, context):

        for diagram in self.xml.iter(self.DIAGRAM_NAMESPACE+'diagram'):

            dpi = int(diagram.get('dpi', '96'))
            width = self.toPixels(diagram.get('width', '32cm'), dpi)
            height = self.toPixels(diagram.get('height', '18cm'), dpi)

            logging.debug(f'diagram-to-svg - embedding image width="{width}", height="{height}", dpi="{dpi}"')

            svg = etree.Element(self.SVG_NAMESPACE+'svg')
            svg.set('width', str(width))
            svg.set('height', str(height))

            self.includeStandardDefs(svg, context)

            self.appendChildren(svg, diagram, 0, 0, width, height)

            diagram.getparent().replace(diagram, svg)

        return self.xml
