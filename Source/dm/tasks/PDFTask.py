import logging, os

from weasyprint import HTML, CSS, default_url_fetcher
from weasyprint.text.fonts import FontConfiguration
from dm.exceptions import TaskException
from dm.utilities import tryLocatingToolsFile
from dm.tasks.Task import Task
from dm.tasks.IfTask import evaluate


class PDFTask(Task):

    """ The xhtml-to-pdf task.

        This task converts an XHTML file to PDF with a CSS stylesheet transformation.
    """   

    def url_fetcher(self, url):
        if url.startswith('file:') and url.endswith('.css'):
            logging.info(f'{self.name} - looking up "{url}""')
            try:
                css_file = tryLocatingToolsFile(os.path.basename(url), 'css', self.tools_dir)
                return dict(filename=css_file, file_obj=open(css_file, 'rb'), mime_type='text/css', encoding='UTF-8')
            except:
                pass
        return default_url_fetcher(url)

    def tryLoadingStylesheets(self, context):
        csss = []
        font_config = FontConfiguration()
        for i in range(len(self.stylesheets)):
            stylesheet = self.stylesheets[i]
            test = self.tests[i]
            filename = tryLocatingToolsFile(stylesheet, 'css', context.tools_dir())
            if test:
                if evaluate(test, context):
                    logging.info(f'{self.name} - applying stylesheet "{filename}" as {test} is True')
                    csss.append(CSS(filename=filename, font_config=font_config))
                else:
                    logging.info(f'{self.name} - skipping stylesheet "{filename}" as {test} is False')
            else:
                logging.info(f'{self.name} - applying stylesheet "{filename}"')
                csss.append(CSS(filename=filename, font_config=font_config))

        return (csss, font_config)

    def tryParsingXHTML(self):
        try:
            return HTML(file_obj=self.content.data, encoding=self.content.encoding, base_url=self.base_url, url_fetcher=self.url_fetcher)
        except Exception as e:
            raise TaskException(f'{self.name} - cannot parse XHTML content', e)

    def tryWritingPDF(self, html, csss, font_config):
        try:
            return html.write_pdf(stylesheets=csss, font_config=font_config, presentational_hints=self.presentational_hints)
        except Exception as e:
            raise TaskException(f'{self.name} - cannot write PDF', e)

    def run(self, context):
        self.tools_dir = None
        self.presentational_hints = 'true' == self.getAttribute('presentational-hints', default='true').lower()
        self.stylesheets = self.getElement('stylesheet', multiple=True, default=['htmlbook.css'])
        self.tests = self.getElement('stylesheet', multiple=True, attribute='test')
        self.base_url = self.getAttribute('base-url', default='.')

        self.load()
        self.tools_dir = context.tools_dir() # to pass to the url_fetcher
        (csss, font_config) = self.tryLoadingStylesheets(context)
        html = self.tryParsingXHTML()
        self.content.setData(self.tryWritingPDF(html, csss, font_config))
        self.save()
