import io

from lxml import etree

from dm.exceptions import TaskException


class Content:

    DEFAULT_ENCODING = 'utf-8'

    def __init__(self):
        self.data = io.BytesIO()
        self.encoding = None

    def setText(self, text, encoding=DEFAULT_ENCODING):
        self.data = io.BytesIO(text.encode(encoding))
        self.encoding = encoding

    def getText(self):
        if self.encoding is not None:
            return self.data.getvalue().decode(self.encoding)
        return self.data.getvalue()

    def setData(self, data):
        self.data = io.BytesIO(data)
        self.encoding = None

    def getData(self, data):
        return self.data

    def getXML(self):
        try:
            return etree.parse(self.data, parser=etree.XMLParser())
        except Exception as e:
            raise TaskException(f'Cannot parse content as XML', e)